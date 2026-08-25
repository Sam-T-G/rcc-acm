# Playbooks

Runbooks for the things ACM @ RCC does more than once. Every playbook has the same shape: purpose, when it runs, who owns it, a T-minus checklist, a day-of run sheet, and what to do after. A "What went wrong before" section appears only when a real retro exists for that event type.

Playbooks are evergreen. Dates, names, and budgets for a specific run live in `semesters/<YYYY-term>/events/`, never here.

## Index

| Playbook | What it covers | Owner role | Typical timing |
|---|---|---|---|
| [Weekly meeting](weekly-meeting.md) | The Thursday 12:50 to 1:50 PM meeting in BLCIS A-210 | Chair (Vice Chair as backup) | Every week classes are in session |
| [Workshop](workshop.md) | A hands-on session with a defined outcome (Build or Learn pillar) | Workshop lead, Chair signs off | Any week; plan 4 weeks out |
| [Club Rush](club-rush.md) | The campus tabling event where most new members sign up | Outreach owner (an officer the Chair assigns) | Early each semester; date set by Student Activities |
| [Hackathon trip](hackathon-trip.md) | Taking a group to an off-campus hackathon (Cal Hacks pattern) | Trip lead plus Treasurer | Plan 8 or more weeks out; funding request first |
| [ICPC regional site](icpc-regional-site.md) | RCC as a host site and as a competing school for the Southern California ICPC regional | Chair plus faculty coach | Registration in early fall, contest in November |
| [ACM AI Hackathon](acm-ai-hackathon.md) | The club's own hackathon | Event lead plus Treasurer | Date [TBD] |
| [Guest speaker](guest-speaker.md) | Hosting an alumni, faculty, or industry speaker | Chair or assigned officer | 1 to 2 per semester; invite 6 weeks out |

## How to use a playbook

1. Create the event folder with `scripts/new-event.sh` (arguments are documented in [semesters/README.md](../../semesters/README.md)). You get `plan.md`, `run-sheet.md`, and `retro.md` from [templates/](../../templates/).
2. Copy the playbook's T-minus checklist into `plan.md` and the run sheet into `run-sheet.md`. Fill in real dates.
3. Work the checklist. Anything that needs money or a go/no-go call gets a line in the [decision log](../01-governance/decision-log.md).
4. After the event, fill in `retro.md`. If the playbook was wrong or missing a step, open a PR against the playbook. That is how these files stay true.

## Operations docs every playbook depends on

| Topic | Doc |
|---|---|
| Booking a room (advisor submits in 25Live, students cannot) | [room-booking.md](../02-operations/room-booking.md) |
| Event forms and the campus event checklist | [event-checklist.md](../02-operations/event-checklist.md) |
| Discord and Instagram announcements | [communications.md](../02-operations/communications.md) |
| Counting attendance (counts only, no names in the repo) | [attendance-tracking.md](../02-operations/attendance-tracking.md) |
| ASRCC money and acknowledgment rules | [asrcc-funding.md](../02-operations/asrcc-funding.md) |
| Getting paid back | [reimbursements.md](../02-operations/reimbursements.md) |
| Code of conduct at every event | [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) |

## Adding a playbook

- One file per event type, kebab-case name, in this folder.
- Use the same headings: Purpose, When, Owner, T-minus checklist, Day-of run sheet, After. Add "What went wrong before" only with a link to a real retro in a semester folder.
- Add a row to the index table above.
- Keep it evergreen (maintenance rule 1 in [maintenance-rules.md](../01-governance/maintenance-rules.md)). Link into a semester folder for dated examples.
