<!-- Index of every template in this folder. Copy a template to the path in the "Copy to" column, fill each fill marker and [TBD], then open a PR. Never patch a copy to fix a template; fix the template here and log it. -->

# Templates

Templates are contracts for ACM @ RCC. Every semester folder is built from them, so a future officer can open any past semester and find the same headings in the same order.

## How to use one

1. Copy the file to the path in the table below, or run the script named there.
2. Fill every `<!-- fill: ... -->` comment and every `[TBD]`. Delete the comment once the field is filled.
3. Leave `[TBD]` only where you do not know. Never guess a date, dollar amount, name, or room.
4. Open a PR. `scripts/check.sh` flags leftover fill markers outside `templates/` and `semesters/_template/`, em dashes, and private data, and counts open `[TBD]` markers.

If a template is wrong or missing a field, change it here, add a [decision record](decision-record.md) to the [decision log](../docs/01-governance/decision-log.md), and leave existing copies alone. See [maintenance rules](../docs/01-governance/maintenance-rules.md), rule 3.

## Index

| Template | Use it when | Copy to |
| --- | --- | --- |
| [meeting-notes.md](meeting-notes.md) | Before every weekly meeting | `semesters/<YYYY-term>/meetings/YYYY-MM-DD.md` (or run `scripts/new-meeting.sh`) |
| [event-plan.md](event-plan.md) | An event, trip, or workshop gets a go decision | `semesters/<YYYY-term>/events/YYYY-MM-DD-slug/plan.md` (or run `scripts/new-event.sh`) |
| [event-run-sheet.md](event-run-sheet.md) | The week before an event, once the plan is final | `semesters/<YYYY-term>/events/YYYY-MM-DD-slug/run-sheet.md` (created by `scripts/new-event.sh`) |
| [event-retro.md](event-retro.md) | Within one week after an event | `semesters/<YYYY-term>/events/YYYY-MM-DD-slug/retro.md` (created by `scripts/new-event.sh`) |
| [decision-record.md](decision-record.md) | Any binding choice: budget, policy, go/no-go, template change | Append as an entry in `docs/01-governance/decision-log.md` |
| [semester-goals.md](semester-goals.md) | First two weeks of a semester | `semesters/<YYYY-term>/goals.md` (the semester template already holds a copy) |
| [officer-handoff.md](officer-handoff.md) | Semester close, and any time an officer leaves | `semesters/<YYYY-term>/handoff.md` (the semester template already holds a copy) |
| [funding-line-item.md](funding-line-item.md) | Each line of an ASRCC funding request, before the late-April deadline | One section per line item in `semesters/<YYYY-term>/budget.md` |
| [workshop-outline.md](workshop-outline.md) | Planning any hands-on session | `semesters/<YYYY-term>/events/YYYY-MM-DD-slug/workshop.md`; promote to `docs/03-playbooks/` once it has run twice |
| [announcement.md](announcement.md) | Anything posted to members or the campus | Draft in `semesters/<YYYY-term>/events/YYYY-MM-DD-slug/announcement.md`, then post |

## Conventions shared by every template

- Dates are ISO `YYYY-MM-DD`. Times include AM or PM.
- People appear by role (Chair, Treasurer, Advisor) unless the person has consented to being named in this public repo. See the [privacy policy](../docs/01-governance/privacy-and-public-repo-policy.md).
- Attendance is a count, never a list of names.
- Dollar amounts are fine. Bank and trust account numbers are not.
- Fill markers look like `<!-- fill: what goes here -->`. They render invisibly on GitHub, so read the raw file when filling one in.

Related: [semester lifecycle](../docs/01-governance/semester-lifecycle.md), [semesters/README.md](../semesters/README.md), [event checklist](../docs/02-operations/event-checklist.md).
