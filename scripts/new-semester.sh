#!/usr/bin/env bash
# Create semesters/<YYYY-term>/ from semesters/_template/ and add it to the index.
#
# Usage: scripts/new-semester.sh <YYYY-term>
# Example: scripts/new-semester.sh 2027-spring
#
# What it does:
#   1. Copies semesters/_template/ to semesters/<YYYY-term>/ (refuses if it exists).
#   2. Replaces SEMESTER_LABEL ("Spring 2027") and SEMESTER_SLUG ("2027-spring") in every copied file.
#   3. Inserts a row into the index table in semesters/README.md.
# Works with bash 3.2 (macOS default) and Linux bash. Run from anywhere; paths resolve from the script.
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/new-semester.sh <YYYY-term>

  <YYYY-term>   lowercase, e.g. 2026-fall, 2027-spring, 2027-summer, 2027-winter

Copies semesters/_template/ to semesters/<YYYY-term>/, fills in the semester name,
and adds a row to the index in semesters/README.md. Refuses to overwrite an existing folder.
USAGE
}

die() { printf 'new-semester.sh: %s\n' "$*" >&2; exit 1; }

if [ "$#" -ne 1 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  usage; [ "$#" -eq 1 ] && exit 0; exit 2
fi

slug="$1"
slug_re='^[0-9]{4}-(fall|spring|summer|winter)$'
[[ "$slug" =~ $slug_re ]] || die "bad semester name '$slug' (want YYYY-fall, YYYY-spring, YYYY-summer, or YYYY-winter)"

year="${slug%-*}"
term="${slug#*-}"
term_cap="$(printf '%s' "${term:0:1}" | tr '[:lower:]' '[:upper:]')${term:1}"
label="$term_cap $year"

root="$(cd "$(dirname "$0")/.." && pwd)"
template="$root/semesters/_template"
dest="$root/semesters/$slug"
index="$root/semesters/README.md"
marker='<!-- new-semester.sh inserts rows above this line. Keep this comment. -->'

[ -d "$template" ] || die "template folder not found: $template"
[ -f "$index" ] || die "index not found: $index"
[ -e "$dest" ] && die "refusing to overwrite: $dest already exists"
grep -qF "$marker" "$index" || die "marker line missing from semesters/README.md; add it under the index table:
$marker"
if grep -qF "[$slug]($slug/)" "$index"; then
  die "semesters/README.md already has a row for $slug"
fi

cp -R "$template" "$dest"

# Replace the two literals in every regular file of the copy (no sed -i: BSD and GNU differ).
while IFS= read -r -d '' f; do
  tmp="$f.tmp.$$"
  sed -e "s/SEMESTER_LABEL/$label/g" -e "s/SEMESTER_SLUG/$slug/g" "$f" > "$tmp"
  mv "$tmp" "$f"
done < <(find "$dest" -type f -print0)

row="| $label | [$slug]($slug/) | planning |"
tmp="$index.tmp.$$"
awk -v row="$row" -v marker="$marker" '$0 == marker { print row } { print }' "$index" > "$tmp"
mv "$tmp" "$index"

printf 'created semesters/%s/ (%s)\n' "$slug" "$label"
printf 'added index row to semesters/README.md\n'
printf 'next: open semesters/%s/README.md and start the Open checklist\n' "$slug"
