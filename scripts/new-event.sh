#!/usr/bin/env bash
# Create an event folder inside a semester from the three event templates.
#
# Usage: scripts/new-event.sh <YYYY-term> <YYYY-MM-DD> <slug>
# Example: scripts/new-event.sh 2027-spring 2027-03-10 club-rush
#
# Creates semesters/<YYYY-term>/events/<YYYY-MM-DD>-<slug>/ with
#   plan.md       from templates/event-plan.md
#   run-sheet.md  from templates/event-run-sheet.md
#   retro.md      from templates/event-retro.md
# and adds a row to semesters/<YYYY-term>/calendar.md. Refuses to overwrite.
# Works with bash 3.2 (macOS default) and Linux bash. Run from anywhere; paths resolve from the script.
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/new-event.sh <YYYY-term> <YYYY-MM-DD> <slug>

  <YYYY-term>    existing semester folder, e.g. 2027-spring
  <YYYY-MM-DD>   event date
  <slug>         lowercase words joined by hyphens, e.g. club-rush

Creates semesters/<YYYY-term>/events/<YYYY-MM-DD>-<slug>/{plan.md,run-sheet.md,retro.md}
from templates/ and adds a row to that semester's calendar.md.
USAGE
}

die() { printf 'new-event.sh: %s\n' "$*" >&2; exit 1; }

if [ "$#" -eq 1 ] && { [ "$1" = "-h" ] || [ "$1" = "--help" ]; }; then usage; exit 0; fi
if [ "$#" -ne 3 ]; then usage; exit 2; fi

sem="$1"; date="$2"; slug="$3"
sem_re='^[0-9]{4}-(fall|spring|summer|winter)$'
date_re='^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
slug_re='^[a-z0-9]+(-[a-z0-9]+)*$'
[[ "$sem" =~ $sem_re ]] || die "bad semester name '$sem' (want e.g. 2027-spring)"
[[ "$date" =~ $date_re ]] || die "bad date '$date' (want YYYY-MM-DD)"
[[ "$slug" =~ $slug_re ]] || die "bad slug '$slug' (lowercase letters, digits, single hyphens)"

root="$(cd "$(dirname "$0")/.." && pwd)"
semdir="$root/semesters/$sem"
tdir="$root/templates"
dest="$semdir/events/$date-$slug"
calendar="$semdir/calendar.md"
marker='<!-- new-event.sh inserts rows above this line. Keep this comment. -->'

[ -d "$semdir" ] || die "semester folder not found: semesters/$sem (run scripts/new-semester.sh $sem first)"
for t in event-plan.md event-run-sheet.md event-retro.md; do
  [ -f "$tdir/$t" ] || die "template missing: templates/$t"
done
[ -e "$dest" ] && die "refusing to overwrite: $dest already exists"

year="${sem%-*}"; term="${sem#*-}"
label="$(printf '%s' "${term:0:1}" | tr '[:lower:]' '[:upper:]')${term:1} $year"

# Templates live in templates/, so their relative links resolve from there. The copy sits four
# levels down, so rewrite link targets: "../X" becomes "<up>/X", a bare "Y.md" becomes
# "<up>/templates/Y.md", and links to the sibling event templates point at the local copies.
# The event date fills the "Date(s)", "Date:", and "Date held:" markers; other date fields stay blank.
# The template's first-line instruction comment is dropped so the copy starts at the heading.
up='../../../..'
up_re="$(printf '%s' "$up" | sed 's/\./\\./g')"
mkdir -p "$dest"
strip_header() { # drop the template's first-line "copy this file to ..." comment and the blank line after it
  awk 'NR == 1 && /^<!-- .*Copy to semesters\// { skip = 1; next }
       NR == 2 && skip && /^$/ { next }
       { print }' "$1"
}
copy() { # copy <template> <target>
  strip_header "$tdir/$1" | sed -e "s/SEMESTER_LABEL/$label/g" -e "s/SEMESTER_SLUG/$sem/g" \
      -e "s~^\(| Date(s) |[[:space:]]*\)<!-- fill: YYYY-MM-DD, or a range -->~\1$date~" \
      -e "s~^\(- Date: \)<!-- fill: YYYY-MM-DD -->~\1$date~" \
      -e "s~^\(- Date held: \)<!-- fill: YYYY-MM-DD -->~\1$date~" \
      -e "s|](\.\./|](${up}/|g" \
      -e "s|](\./|](${up}/templates/|g" \
      -e "s|](\([A-Za-z0-9_-][A-Za-z0-9_./-]*\)\([)#]\)|](${up}/templates/\1\2|g" \
      -e "s|^\(\[[^]]*\]:[[:space:]]*\)\.\./|\1${up}/|" \
      -e "s|](${up_re}/templates/event-plan\.md|](plan.md|g" \
      -e "s|](${up_re}/templates/event-run-sheet\.md|](run-sheet.md|g" \
      -e "s|](${up_re}/templates/event-retro\.md|](retro.md|g" \
      > "$dest/$2"
}
copy event-plan.md plan.md
copy event-run-sheet.md run-sheet.md
copy event-retro.md retro.md

printf 'created semesters/%s/events/%s-%s/ (plan.md, run-sheet.md, retro.md)\n' "$sem" "$date" "$slug"

if [ -f "$calendar" ] && grep -qF "$marker" "$calendar"; then
  row="| $date | [$slug](events/$date-$slug/plan.md) | event | [TBD] | planned |"
  tmp="$calendar.tmp.$$"
  awk -v row="$row" -v marker="$marker" '$0 == marker { print row } { print }' "$calendar" > "$tmp"
  mv "$tmp" "$calendar"
  printf 'added calendar row to semesters/%s/calendar.md (set the owner)\n' "$sem"
else
  printf 'note: calendar marker not found in semesters/%s/calendar.md; add the row by hand\n' "$sem"
fi
printf 'next: fill plan.md, then walk docs/02-operations/event-checklist.md\n'
