#!/usr/bin/env bash
# Bundle one deck and, with --push, publish it to the gh-pages branch under decks/<slug>/.
#
# Usage: scripts/publish-deck.sh <deck.html> <slug> [--push] [--no-check]
# Example: scripts/publish-deck.sh semesters/2026-fall/meetings/2026-09-24-deck.html 2026-09-24 --push
#
# The deck is checked with deck-kit/check.mjs, bundled into one file with deck-kit/bundle.mjs
# (stylesheet, engine, and images inlined; GSAP and fonts stay on their CDNs), and written to
# site/decks/<slug>/index.html (gitignored). With --push that one folder is replaced on gh-pages
# and nothing else is touched, so every other deck stays exactly as published.
# GitHub Pages then serves it at https://sam-t-g.github.io/rcc-acm/decks/<slug>/.
# --no-check skips the check; use it only to preview a deck that is still being written.
# Works with bash 3.2 (macOS default) and Linux bash. Run from anywhere; paths resolve from the script.
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/publish-deck.sh <deck.html> <slug> [--push] [--no-check]

  <deck.html>  the source deck, e.g. semesters/2026-fall/decks/2026-09-24-first-meeting.html
  <slug>       the folder it is served from: lowercase letters, digits, and hyphens
  --push       also replace decks/<slug>/ on the gh-pages branch on origin
  --no-check   skip deck-kit/check.mjs (preview only; --push refuses it)
USAGE
}

die() { printf 'publish-deck.sh: %s\n' "$*" >&2; exit 1; }

deck=""; slug=""; push=0; check=1
for a in "$@"; do
  case "$a" in
    -h|--help) usage; exit 0;;
    --push) push=1;;
    --no-check) check=0;;
    -*) usage >&2; exit 2;;
    *) if [ -z "$deck" ]; then deck="$a"; elif [ -z "$slug" ]; then slug="$a"; else usage >&2; exit 2; fi;;
  esac
done
[ -n "$deck" ] && [ -n "$slug" ] || { usage >&2; exit 2; }
printf '%s' "$slug" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' || die "slug must be lowercase letters, digits, and hyphens: $slug"
[ "$push" -eq 0 ] || [ "$check" -eq 1 ] || die "--push needs the check; drop --no-check"

deck_abs="$(cd "$(dirname "$deck")" && pwd)/$(basename "$deck")"
[ -f "$deck_abs" ] || die "no deck at $deck"
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
case "$deck_abs" in "$root"/*) ;; *) die "the deck must live inside this repo";; esac
deck_rel="${deck_abs#"$root"/}"

if [ "$check" -eq 1 ]; then
  node deck-kit/check.mjs "$deck_rel" || die "check failed; fix the deck, or preview with --no-check"
fi

out="site/decks/$slug"
rm -rf "$out"
mkdir -p "$out"
node deck-kit/bundle.mjs "$deck_rel" "$out/index.html"

# A bundled deck must not reach for a local file the bundler could not inline.
if grep -Eo '(src|href)="[^"]+"' "$out/index.html" | grep -Ev '"(https?:|data:|#|mailto:)' | grep -q .; then
  grep -Eo '(src|href)="[^"]+"' "$out/index.html" | grep -Ev '"(https?:|data:|#|mailto:)' | sed 's/^/  unresolved: /' >&2
  die "the bundle still points at local files"
fi

printf 'built %s/index.html from %s\n' "$out" "$deck_rel"
[ "$push" -eq 1 ] || exit 0

remote="$(git remote get-url origin)"
owner_repo="$(printf '%s' "$remote" | sed -E 's#^(https://github.com/|git@github.com:)##; s#\.git$##')"
owner="$(printf '%s' "${owner_repo%%/*}" | tr '[:upper:]' '[:lower:]')"
url="https://$owner.github.io/${owner_repo#*/}/decks/$slug/"

source_rev="$(git rev-parse --short HEAD)"
[ -z "$(git status --porcelain -- "$deck_rel" deck-kit)" ] || source_rev="$source_rev with uncommitted changes"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

if git ls-remote --exit-code --heads origin gh-pages >/dev/null 2>&1; then
  git clone --quiet --branch gh-pages --single-branch "$remote" "$tmp"
else
  git init --quiet "$tmp"
  git -C "$tmp" checkout --quiet --orphan gh-pages
  git -C "$tmp" remote add origin "$remote"
fi

touch "$tmp/.nojekyll"   # serve files as-is; no Jekyll processing
rm -rf "$tmp/decks/$slug"
mkdir -p "$tmp/decks/$slug"
cp "$out/index.html" "$tmp/decks/$slug/index.html"
git -C "$tmp" add -A
if git -C "$tmp" diff --cached --quiet; then
  printf 'gh-pages already has this build; nothing to push\n'
  exit 0
fi
git -C "$tmp" commit --quiet -m "Publish deck $slug from $source_rev ($deck_rel)"
git -C "$tmp" push --quiet origin gh-pages
printf 'pushed decks/%s to gh-pages; GitHub Pages serves it at %s\n' "$slug" "$url"
