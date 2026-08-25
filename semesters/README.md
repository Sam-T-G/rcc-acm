# Semesters

One folder per semester. Anything tied to a date, a person, or a term lives here: goals, calendar, budget, meeting notes, event folders, the retrospective, and the handoff. Evergreen rules and how-tos live in [docs/](../docs/README.md). The full lifecycle rules are in [semester-lifecycle.md](../docs/01-governance/semester-lifecycle.md).

## Folder names

`YYYY-term`, lowercase: `2026-fall`, `2027-spring`, `2027-summer`. Fall runs late August to mid December. Spring runs mid February to early June.

Never create a semester folder by hand. Run the script so the copy matches the template and the index below stays current.

## Index

| Semester | Folder | Status |
|---|---|---|
| Fall 2025 | [2025-fall](2025-fall/) | partial (backfilled August 2026; retrospective and handoff have [TBD] gaps) |
| Spring 2026 | [2026-spring](2026-spring/) | partial (backfilled August 2026; retrospective and handoff have [TBD] gaps) |
| Fall 2026 | [2026-fall](2026-fall/) | active |
<!-- new-semester.sh inserts rows above this line. Keep this comment. -->

Status is one of `planning` (folder exists, semester has not started), `active`, `partial` (semester ended but `retrospective.md` or `handoff.md` still carries `[TBD]`), or `closed` (retrospective and handoff are filled in and merged). A note in parentheses after the status is fine. Edit the status by hand when it changes.

## Three phases

| Phase | When | What the officer team does | Where it is written down |
|---|---|---|---|
| Open | Weeks 0 to 2 | Renew the club, confirm the room, set goals, fill the calendar and budget, record counts | `goals.md`, `calendar.md`, `budget.md`, `roster.md` |
| Run | Every week | Meeting notes, event folders, budget rows, decision-log entries | `meetings/`, `events/`, `budget.md` |
| Close | Last 2 weeks | Retrospective, elections, handoff, next semester's folder, one PR | `retrospective.md`, `handoff.md` |

The working checklist for each phase is [_template/README.md](_template/README.md). Every semester folder starts as a copy of it.

## Scripts

Run these from the repo root. They refuse to overwrite anything that already exists.

| Command | What it does |
|---|---|
| `scripts/new-semester.sh 2027-spring` | Copies `_template/` to `semesters/2027-spring/`, fills in the semester name, adds a row to the index above |
| `scripts/new-event.sh 2027-spring 2027-03-10 club-rush` | Creates `events/2027-03-10-club-rush/` with `plan.md`, `run-sheet.md`, and `retro.md` from [templates/](../templates/), and adds a calendar row |
| `scripts/new-meeting.sh 2027-spring 2027-02-18` | Creates `meetings/2027-02-18.md` from [templates/meeting-notes.md](../templates/meeting-notes.md) |
| `scripts/check.sh` | Pre-PR check: leftover placeholders and semester literals, personal-data patterns, em dashes, broken relative links, files over 1 MB, leftover template fill markers, and markdownlint if installed. It also counts open `[TBD]` markers without failing on them. |

Source: [new-semester.sh](../scripts/new-semester.sh), [new-event.sh](../scripts/new-event.sh), [new-meeting.sh](../scripts/new-meeting.sh), [check.sh](../scripts/check.sh).

## Changing the template

`_template/` is a contract. If a file in it is wrong, fix `_template/` and log the change in the [decision log](../docs/01-governance/decision-log.md). Do not patch a single semester's copy and leave the template broken. See [maintenance-rules.md](../docs/01-governance/maintenance-rules.md).

The literal strings `SEMESTER_LABEL` and `SEMESTER_SLUG` belong only in `_template/` (and may appear in `templates/`). The scripts replace them when they copy a file. If `check.sh` reports one anywhere else, someone copied a folder by hand.
