#!/usr/bin/env bash
# Create a meeting-notes file inside a semester from templates/meeting-notes.md.
#
# Usage: scripts/new-meeting.sh <YYYY-term> <YYYY-MM-DD>
# Example: scripts/new-meeting.sh 2027-spring 2027-02-18
#
# Creates semesters/<YYYY-term>/meetings/<YYYY-MM-DD>.md. Refuses to overwrite.
# Works with bash 3.2 (macOS default) and Linux bash. Run from anywhere; paths resolve from the script.
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/new-meeting.sh <YYYY-term> <YYYY-MM-DD>

  <YYYY-term>    existing semester folder, e.g. 2027-spring
  <YYYY-MM-DD>   meeting date

Creates semesters/<YYYY-term>/meetings/<YYYY-MM-DD>.md from templates/meeting-notes.md.
USAGE
}

die() { printf 'new-meeting.sh: %s\n' "$*" >&2; exit 1; }

if [ "$#" -eq 1 ] && { [ "$1" = "-h" ] || [ "$1" = "--help" ]; }; then usage; exit 0; fi
if [ "$#" -ne 2 ]; then usage; exit 2; fi

sem="$1"; date="$2"
sem_re='^[0-9]{4}-(fall|spring|summer|winter)$'
date_re='^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
[[ "$sem" =~ $sem_re ]] || die "bad semester name '$sem' (want e.g. 2027-spring)"
[[ "$date" =~ $date_re ]] || die "bad date '$date' (want YYYY-MM-DD)"

root="$(cd "$(dirname "$0")/.." && pwd)"
semdir="$root/semesters/$sem"
template="$root/templates/meeting-notes.md"
dest="$semdir/meetings/$date.md"

[ -d "$semdir" ] || die "semester folder not found: semesters/$sem (run scripts/new-semester.sh $sem first)"
[ -f "$template" ] || die "template missing: templates/meeting-notes.md"
[ -e "$dest" ] && die "refusing to overwrite: $dest already exists"

year="${sem%-*}"; term="${sem#*-}"
label="$(printf '%s' "${term:0:1}" | tr '[:lower:]' '[:upper:]')${term:1} $year"

# The template lives in templates/, so its relative links resolve from there. The copy sits three
# levels down, so rewrite link targets: "../X" becomes "<up>/X" and a bare "Y.md" becomes
# "<up>/templates/Y.md". The meeting date fills the title and the "Date" row; other date fields stay blank.
# The template's first-line instruction comment is dropped so the copy starts at the heading.
up='../../..'
mkdir -p "$semdir/meetings"
strip_header() { # drop the template's first-line "copy this file to ..." comment and the blank line after it
  awk 'NR == 1 && /^<!-- .*Copy to semesters\// { skip = 1; next }
       NR == 2 && skip && /^$/ { next }
       { print }' "$1"
}
strip_header "$template" | sed -e "s/SEMESTER_LABEL/$label/g" -e "s/SEMESTER_SLUG/$sem/g" \
    -e "s~^\(# [^<]*\)<!-- fill: YYYY-MM-DD -->~\1$date~" \
    -e "s~^\(| Date |[[:space:]]*\)<!-- fill: YYYY-MM-DD -->~\1$date~" \
    -e "s|](\.\./|](${up}/|g" \
    -e "s|](\./|](${up}/templates/|g" \
    -e "s|](\([A-Za-z0-9_-][A-Za-z0-9_./-]*\)\([)#]\)|](${up}/templates/\1\2|g" \
    -e "s|^\(\[[^]]*\]:[[:space:]]*\)\.\./|\1${up}/|" \
    > "$dest"

printf 'created semesters/%s/meetings/%s.md\n' "$sem" "$date"
printf 'next: fill in the date, attendance count, decisions, and action items; commit within 48 hours\n'
