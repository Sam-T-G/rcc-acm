# Events - Fall 2025

One folder per event, named `YYYY-MM-DD-slug` (for example `2027-03-10-club-rush`). Each folder has three files:

| File | Written | Purpose |
|---|---|---|
| `plan.md` | before | what, when, where, who, budget line, room booking, announcement |
| `run-sheet.md` | day before | minute-by-minute for the day, who does what, what to bring |
| `retro.md` | within a week after | attendance, cost, what to change |

## Create a folder

From the repo root:

```sh
scripts/new-event.sh 2025-fall YYYY-MM-DD slug
```

It copies [event-plan.md](../../../templates/event-plan.md), [event-run-sheet.md](../../../templates/event-run-sheet.md), and [event-retro.md](../../../templates/event-retro.md) from `templates/`, adds a row to [calendar.md](../calendar.md), and refuses to overwrite an existing folder. Slugs are lowercase words joined by hyphens.

## Before the event

Walk the [event checklist](../../../docs/02-operations/event-checklist.md). The advisor books the room ([room-booking.md](../../../docs/02-operations/room-booking.md)). If ASRCC money is involved, the plan names the budget line and the event acknowledges ASRCC.

## Playbooks

Repeatable event types have a playbook in [docs/03-playbooks/](../../../docs/03-playbooks/README.md). Start from the playbook, then fill `plan.md` with this semester's specifics.

## Photos and media

Photos of people need written consent before they go anywhere public. Large files go in the club's shared drive and get linked from `retro.md`; nothing over 1 MB is committed here.

## Event folders this semester

| Folder | Event | Status |
|---|---|---|
| [2025-10-24-cal-hacks-12/](2025-10-24-cal-hacks-12/plan.md) | Cal Hacks 12.0, October 24 to 26, 2025, San Francisco; 11 members accepted | backfilled; actuals [TBD] |

RCC also hosted a site for the ICPC Southern California Regional Contest on November 15, 2025 (Martin Luther King Jr. Teaching and Learning Center). No folder exists for it yet. If records exist (RCC teams, attendance, cost), create `2025-11-15-icpc-socal-regional/` from the templates and follow the [ICPC regional site playbook](../../../docs/03-playbooks/icpc-regional-site.md).

The ACM AI Hackathon has brand assets in `assets/` but its date and term are [TBD]. If it ran in Fall 2025, add a folder.
