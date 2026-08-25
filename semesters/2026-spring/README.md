# Spring 2026

Working checklist for the Spring 2026 officer team of ACM @ RCC. Folder: `semesters/2026-spring/`. The rules behind this checklist are in [semester-lifecycle.md](../../docs/01-governance/semester-lifecycle.md).

Tick boxes in this file as you go and commit it as-is. A half-finished checklist in the repo beats a finished one in someone's head.

## Backfilled folder

This folder was created in August 2026, after the semester ended. It was built from the FY 2026-27 ASRCC funding request, which the club wrote and submitted this semester. Nobody ran the checklist below at the time, so the boxes stay unticked unless a record shows the step happened. Every `[TBD]` is a real gap: fill it from the advisor's files, the treasurer's records, or Discord history, and say where the number came from.

What is known for sure: the club requested $12,000 from ASRCC for FY 2026-27 (due April 29, 2026; hearing preferences May 11 to 13, 2026) and reported 22 active members in that request. Details: [budget.md](budget.md).

## Files in this folder

| File | What it holds | Fill in by |
|---|---|---|
| [goals.md](goals.md) | 3 to 5 goals with a number attached to each | week 2 |
| [calendar.md](calendar.md) | every dated thing this semester, deadlines first | week 2, then kept current |
| [budget.md](budget.md) | ASRCC allocation, trust balance, spending, reimbursements | week 2, then after every spend |
| [roster.md](roster.md) | counts and which roles are filled (never names without consent) | week 2 and last week |
| [meetings/](meetings/README.md) | one file per meeting | within 48 hours of each meeting |
| [events/](events/README.md) | one folder per event: plan, run sheet, retro | when an event gets a yes |
| [projects/](projects/README.md) | member projects running this semester | as they start |
| [retrospective.md](retrospective.md) | what happened, what to change | last 2 weeks |
| [handoff.md](handoff.md) | access transfers and open threads for the next team | last 2 weeks |

## Open (weeks 0 to 2)

- [ ] Read last semester's `retrospective.md` and `handoff.md`. Copy open threads into `goals.md` or `calendar.md`.
- [ ] Renew the club with Student Activities for this semester. Record the due date and the submitted date in `calendar.md`. See [club-recognition-and-icc.md](../../docs/02-operations/club-recognition-and-icc.md).
- [ ] Confirm the weekly slot (Thursdays, 12:50 to 1:50 PM, BLCIS A-210) and ask the advisor to book the room. See [room-booking.md](../../docs/02-operations/room-booking.md).
- [ ] Confirm who holds each role in `roster.md`. Every role listed there has a person, or the row says `open`.
- [ ] Check [MAINTAINERS.md](../../MAINTAINERS.md) lists two repo admins plus the advisor. Fix it in this PR if not.
- [ ] Write `goals.md`.
- [ ] Fill `calendar.md`: replace every `[TBD]` date you know, mark rows that do not apply this term as `n/a`, add Club Rush, elections, and finals.
- [ ] Fill `budget.md`: allocation status, trust balance, planned line items. See [asrcc-funding.md](../../docs/02-operations/asrcc-funding.md).
- [ ] Post the first announcement on Discord and Instagram. Start from [announcement.md](../../templates/announcement.md). Links live in [links.md](../../docs/04-brand/links.md).
- [ ] Hold the first meeting and commit the notes.
- [ ] Set this semester to `active` in [semesters/README.md](../README.md).

## Run (every week)

- [ ] After the meeting: `scripts/new-meeting.sh 2026-spring YYYY-MM-DD`, fill in attendance count, decisions, action items, commit within 48 hours.
- [ ] Any binding decision (money, policy, event go/no-go, template change) gets an entry in the [decision log](../../docs/01-governance/decision-log.md) the same week.
- [ ] Event gets a yes: `scripts/new-event.sh 2026-spring YYYY-MM-DD slug`, fill `plan.md`, confirm the calendar row the script added. Walk through [event-checklist.md](../../docs/02-operations/event-checklist.md).
- [ ] Event done: fill `retro.md` within a week, update `budget.md` with what was actually spent.
- [ ] Money moved: add a row to `budget.md`, hand the receipt to the treasurer, follow [reimbursements.md](../../docs/02-operations/reimbursements.md).
- [ ] Look at `calendar.md` for anything due in the next 4 weeks.
- [ ] Run `scripts/check.sh` before opening a PR.

## Close (last 2 weeks)

- [ ] Update the end-of-semester column in `roster.md`.
- [ ] Reconcile `budget.md`: every planned row has a spent amount or `0`, every reimbursement has a status.
- [ ] Write `retrospective.md`. Numbers first, then what to change.
- [ ] Hold elections if they are due. Log the result in the decision log. Update `MAINTAINERS.md` and `roster.md`. See [elections.md](../../docs/00-charter/elections.md).
- [ ] Write `handoff.md`. Transfer every account listed there and tick the row when the new holder has logged in.
- [ ] Run `scripts/check.sh --strict`. Every template fill marker (the HTML comments the templates carry) left in this folder is either filled in or replaced with `[TBD]`.
- [ ] Create next semester's folder: `scripts/new-semester.sh YYYY-term`.
- [ ] Set this semester to `closed` and the next one to `planning` in [semesters/README.md](../README.md).
- [ ] Open one PR titled `close 2026-spring`. Outgoing team opens it, incoming team reviews and merges. See [handoff-procedure.md](../../docs/01-governance/handoff-procedure.md).

A semester is not done until `retrospective.md` and `handoff.md` are filled in and the next folder exists.
