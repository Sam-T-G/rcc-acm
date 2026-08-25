# Events - Fall 2026

One folder per event, named `YYYY-MM-DD-slug` (for example `2027-03-10-club-rush`). Each folder has three files:

| File | Written | Purpose |
|---|---|---|
| `plan.md` | before | what, when, where, who, budget line, room booking, announcement |
| `run-sheet.md` | day before | minute-by-minute for the day, who does what, what to bring |
| `retro.md` | within a week after | attendance, cost, what to change |

## Create a folder

From the repo root:

```sh
scripts/new-event.sh 2026-fall YYYY-MM-DD slug
```

It copies [event-plan.md](../../../templates/event-plan.md), [event-run-sheet.md](../../../templates/event-run-sheet.md), and [event-retro.md](../../../templates/event-retro.md) from `templates/`, adds a row to [calendar.md](../calendar.md), and refuses to overwrite an existing folder. Slugs are lowercase words joined by hyphens.

## Before the event

Walk the [event checklist](../../../docs/02-operations/event-checklist.md). The advisor books the room ([room-booking.md](../../../docs/02-operations/room-booking.md)). If ASRCC money is involved, the plan names the budget line and the event acknowledges ASRCC.

## Playbooks

Repeatable event types have a playbook in [docs/03-playbooks/](../../../docs/03-playbooks/README.md). Start from the playbook, then fill `plan.md` with this semester's specifics.

## Photos and media

Photos of people need written consent before they go anywhere public. Large files go in the club's shared drive and get linked from `retro.md`; nothing over 1 MB is committed here.

## Event folders this semester

None yet. Planned events and the playbook each one starts from:

| Event | Date | Playbook | Folder |
|---|---|---|---|
| Cal Hacks 13.0 (Fall 2026, San Francisco) | [TBD] | [hackathon-trip.md](../../../docs/03-playbooks/hackathon-trip.md) | create with `scripts/new-event.sh 2026-fall YYYY-MM-DD cal-hacks-13` once the date is public |
| ICPC Southern California Regional, RCC site | [TBD] (November 15 in 2025) | [icpc-regional-site.md](../../../docs/03-playbooks/icpc-regional-site.md) | create once the 2026-27 date is announced |
| ACM AI Hackathon | [TBD] | [acm-ai-hackathon.md](../../../docs/03-playbooks/acm-ai-hackathon.md) | create once a date is picked |
| Club Rush | [TBD] | [club-rush.md](../../../docs/03-playbooks/club-rush.md) | create once Student Activities publishes the date |

The last trip's numbers are in [2025-fall/events/2025-10-24-cal-hacks-12/](../../2025-fall/events/2025-10-24-cal-hacks-12/plan.md).
