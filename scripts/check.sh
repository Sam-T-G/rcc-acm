#!/usr/bin/env bash
# Local pre-PR check for this repo. Prints a summary and exits nonzero on any hit.
#
# Usage: scripts/check.sh
#
# Checks:
#   1. Leftover double-brace placeholders (from the shared-base materialize step) anywhere.
#   2. SEMESTER_LABEL / SEMESTER_SLUG outside semesters/_template/ (a folder copied by hand).
#      templates/ is skipped too, in case a template ever carries one on purpose.
#   3. Em dashes (U+2014) in .md files. Use periods, colons, semicolons, parens, or "and".
#   4. Personal info patterns: US phone numbers, @student.rccd.edu addresses, @gmail.com addresses.
#      A line that must carry one on purpose (an office number, a policy example) can opt out by
#      containing the text pii-ok, for example in an HTML comment at the end of the line.
#      assets/ and SVG files are skipped: path coordinates look like phone numbers.
#   5. Broken relative Markdown links in .md files (http, https, mailto, and #anchors are skipped).
#   6. Files larger than 1 MB.
#   7. markdownlint-cli2, only if it is installed (global binary or npx cache). CI runs it regardless.
#   8. Open [TBD] markers in .md files, counted. Informational only; never fails the check.
#   9. Leftover template fill markers (<!-- fill: ... -->) in .md files outside templates/ and semesters/_template/.
#      Informational by default (fresh scaffolds from the scripts carry them). Pass --strict to fail on them,
#      which the semester Close checklist requires before the close PR.
# Works with bash 3.2 (macOS default) and Linux bash. Run from anywhere; paths resolve from the script.
set -euo pipefail

strict=0
for a in "$@"; do
  case "$a" in
    --strict) strict=1;;
    -h|--help) sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) printf 'usage: scripts/check.sh [--strict]\n  --strict  also fail on leftover <!-- fill: ... --> markers (required before a semester close PR)\n' >&2; exit 2;;
  esac
done

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

# Regexes as variables: bash 3.2 handles quoted regexes inconsistently in [[ =~ ]].
scheme_re='^[A-Za-z][A-Za-z0-9+.-]*:'
token_re='\{\{[A-Z_]+\}\}'
phone_re='(\+?1[ .-]?)?(\([0-9]{3}\)|[0-9]{3})[ .-]?[0-9]{3}[ .-][0-9]{4}'
mail_re='[A-Za-z0-9._%+-]+@(student\.rccd\.edu|gmail\.com)'
emdash="$(printf '\342\200\224')"

n_tokens=0; n_semlit=0; n_emdash=0; n_pii=0; n_links=0; n_big=0; n_md=0; n_tbd=0; n_fill=0
lint_result="skipped (markdownlint-cli2 not installed)"

all_files() { # every tracked-looking file, NUL separated
  find . -type f -not -path './.git/*' -not -path '*/node_modules/*' -print0
}
md_files() {
  find . -type f -name '*.md' -not -path './.git/*' -not -path '*/node_modules/*' -print0
}

hit() { printf '  %s\n' "$*"; }

# 1. leftover double-brace placeholders (anywhere; the materialize step should have removed them all)
printf '1. leftover placeholders\n'
while IFS= read -r -d '' f; do
  while IFS= read -r line; do
    [ -n "$line" ] && { hit "$f:$line"; n_tokens=$((n_tokens+1)); }
  done < <(LC_ALL=C grep -nIE "$token_re" "$f" 2>/dev/null || true)
done < <(all_files)

# 2. SEMESTER_LABEL / SEMESTER_SLUG outside semesters/_template (backtick spans ignored; templates and scripts skipped)
printf '2. semester literals outside semesters/_template and templates\n'
while IFS= read -r -d '' f; do
  case "$f" in ./semesters/_template/*|./templates/*|./scripts/*) continue;; esac
  while IFS= read -r line; do
    [ -n "$line" ] && { hit "$f:$line"; n_semlit=$((n_semlit+1)); }
  done < <(sed 's/`[^`]*`//g' "$f" | LC_ALL=C grep -nE 'SEMESTER_(LABEL|SLUG)' 2>/dev/null || true)
done < <(md_files)

# 3. em dashes in .md files
printf '3. em dashes (U+2014) in .md files\n'
while IFS= read -r -d '' f; do
  while IFS= read -r line; do
    [ -n "$line" ] && { hit "$f:$line"; n_emdash=$((n_emdash+1)); }
  done < <(LC_ALL=C grep -nF "$emdash" "$f" 2>/dev/null || true)
done < <(md_files)

# 4. personal info patterns (lines containing pii-ok are skipped; assets/ and SVG files are not prose)
printf '4. personal info patterns (phone, @student.rccd.edu, @gmail.com)\n'
while IFS= read -r -d '' f; do
  case "$f" in ./assets/*|*.svg) continue;; esac
  while IFS= read -r line; do
    [ -n "$line" ] || continue
    case "$line" in *pii-ok*) continue;; esac
    hit "$f:$line"; n_pii=$((n_pii+1))
  done < <(LC_ALL=C grep -nIE "$phone_re|$mail_re" "$f" 2>/dev/null || true)
done < <(all_files)

# 5. broken relative links in .md files
printf '5. broken relative links in .md files\n'
extract_links() { # prints "<line>\t<target>" for inline links and reference definitions, skipping code
  awk '
    BEGIN { fence = 0 }
    {
      if ($0 ~ /^[ \t]*(```|~~~)/) { fence = !fence; next }
      if (fence) next
      line = $0
      gsub(/`[^`]*`/, "", line)
      while (match(line, /\]\([^)]*\)/)) {
        print NR "\t" substr(line, RSTART + 2, RLENGTH - 3)
        line = substr(line, RSTART + RLENGTH)
      }
      if ($0 ~ /^[ \t]*\[[^]]+\]:[ \t]+/) {
        ref = $0
        sub(/^[ \t]*\[[^]]+\]:[ \t]+/, "", ref)
        sub(/[ \t].*$/, "", ref)
        print NR "\t" ref
      }
    }' "$1"
}
while IFS= read -r -d '' f; do
  dir="$(dirname "$f")"
  while IFS=$'\t' read -r lineno target; do
    [ -n "$target" ] || continue
    target="${target#<}"; target="${target%%>*}"   # <path> form
    target="${target%% *}"                          # drop "title"
    target="${target%%#*}"                          # drop #anchor
    [ -n "$target" ] || continue
    [[ "$target" =~ $scheme_re ]] && continue
    target="$(printf '%s' "$target" | sed 's/%20/ /g')"
    case "$target" in
      /*) path=".$target";;
      *)  path="$dir/$target";;
    esac
    if [ ! -e "$path" ]; then
      hit "$f:$lineno: $target"; n_links=$((n_links+1))
    fi
  done < <(extract_links "$f")
done < <(md_files)

# 6. files over 1 MB
printf '6. files over 1 MB\n'
while IFS= read -r -d '' f; do
  hit "$f"; n_big=$((n_big+1))
done < <(find . -type f -size +1048576c -not -path './.git/*' -not -path '*/node_modules/*' -print0)

# 7. markdownlint-cli2 if available
printf '7. markdownlint-cli2\n'
lint_cmd=""
if command -v markdownlint-cli2 >/dev/null 2>&1; then
  lint_cmd="markdownlint-cli2"
elif command -v npx >/dev/null 2>&1 && npx --no-install markdownlint-cli2 --version >/dev/null 2>&1; then
  lint_cmd="npx --no-install markdownlint-cli2"
fi
if [ -n "$lint_cmd" ]; then
  if $lint_cmd '**/*.md' '#node_modules' '#.git' 2>&1 | sed 's/^/  /'; then
    lint_result="passed"
  else
    lint_result="failed"; n_md=1
  fi
fi

# 8. open [TBD] markers (informational; the to-do list, not a failure)
printf '8. open [TBD] markers in .md files (informational)\n'
n_tbd_files=0
while IFS= read -r -d '' f; do
  c="$( (LC_ALL=C grep -o '\[TBD' "$f" 2>/dev/null || true) | wc -l | tr -d ' ')"
  if [ "$c" -gt 0 ]; then
    n_tbd=$((n_tbd+c)); n_tbd_files=$((n_tbd_files+1))
  fi
done < <(md_files)
hit "$n_tbd markers in $n_tbd_files files; list them with: grep -rn '\[TBD' --include='*.md' ."

# 9. leftover template fill markers outside templates/ and semesters/_template/ (a copied template never got filled in)
printf '9. leftover fill markers (<!-- fill: ... -->) outside templates and semesters/_template\n'
while IFS= read -r -d '' f; do
  case "$f" in ./semesters/_template/*|./templates/*) continue;; esac
  while IFS= read -r line; do
    [ -n "$line" ] && { hit "$f:$line"; n_fill=$((n_fill+1)); }
  done < <(LC_ALL=C grep -nF '<!-- fill:' "$f" 2>/dev/null || true)
done < <(md_files)

total=$((n_tokens + n_semlit + n_emdash + n_pii + n_links + n_big + n_md))
[ "$strict" -eq 1 ] && total=$((total + n_fill))
printf '\nsummary\n'
printf '  leftover placeholders ........ %d\n' "$n_tokens"
printf '  semester literals ............ %d\n' "$n_semlit"
printf '  em dashes .................... %d\n' "$n_emdash"
printf '  personal info patterns ....... %d\n' "$n_pii"
printf '  broken relative links ........ %d\n' "$n_links"
printf '  files over 1 MB .............. %d\n' "$n_big"
printf '  markdownlint ................. %s\n' "$lint_result"
if [ "$strict" -eq 1 ]; then printf '  leftover fill markers ........ %d\n' "$n_fill"; else printf '  leftover fill markers ........ %d (informational; --strict fails on them)\n' "$n_fill"; fi
printf '  open [TBD] markers ........... %d (informational; does not fail the check)\n' "$n_tbd"
if [ "$total" -eq 0 ]; then
  printf 'OK: nothing to fix\n'
  exit 0
fi
printf 'FAIL: %d problem(s). Fix them, then run scripts/check.sh again.\n' "$total"
exit 1
