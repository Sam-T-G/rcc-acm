# Playbook: Workshop

## Purpose

A workshop is a hands-on session where everyone leaves having built or run something. It is the Build and Learn pillars in one block. Use this playbook instead of the [weekly meeting](weekly-meeting.md) one when the session needs setup ahead of time, runs longer than an hour, is open to non-members, needs food, or needs a room other than A-210.

## When

Any week classes are in session. Start planning 4 weeks out. A workshop can take the Thursday 12:50 slot in BLCIS A-210 or run at a separate time; a separate time means the advisor has to book a room (students cannot submit 25Live requests, see [room-booking.md](../02-operations/room-booking.md)).

Length: 60 to 120 minutes. Past 2 hours attendance drops and so does the quality of what people build.

## Owner

The workshop lead is whoever proposed it (officer or member). The Chair signs off on the date and budget. The Treasurer is involved only if money is spent.

## Proposing one

1. Open a workshop proposal issue using [.github/ISSUE_TEMPLATE/workshop-proposal.yml](../../.github/ISSUE_TEMPLATE/workshop-proposal.yml).
2. Write the outline in [templates/workshop-outline.md](../../templates/workshop-outline.md).
3. If it needs money, add a line in the semester `budget.md` and a [decision log](../01-governance/decision-log.md) entry.

## Design rules

- One outcome. Finish the sentence "By the end, every person will have ___" before you write a slide.
- Prerequisites are posted a week ahead: accounts to create, software to install, hardware to bring. Assume the campus wifi is slow and plan for it.
- Test the setup steps on a laptop that is not yours, on at least one Windows and one macOS machine.
- Nothing requires a paid account or a credit card.
- Hands-on time is at least half the session. Talking for 40 minutes then "now try it" in the last 10 is a lecture.
- Have a fallback: a repo with the finished state at each checkpoint so someone who gets stuck can jump ahead.

## T-minus checklist

### T-4 weeks

- [ ] Proposal issue opened; topic, lead, date, room, and budget agreed
- [ ] If not in A-210 at the usual time: advisor asked to book the room in 25Live (at least 2 weeks before the event per the Club Advisor Guide; ask earlier)
- [ ] If it is a campus event (open to non-members, food, or outside the regular meeting): Student Activities Event Form started; see [event-checklist.md](../02-operations/event-checklist.md)
- [ ] Event folder created with `scripts/new-event.sh`

### T-3 weeks

- [ ] Outline drafted from the template: outcome, checkpoints, timing
- [ ] Prerequisites list written
- [ ] Setup tested on a second machine

### T-2 weeks

- [ ] Event Form submitted if required; Food Authorization form if food is served
- [ ] Supplies list (if any) to the Treasurer with prices; keep receipts for [reimbursements.md](../02-operations/reimbursements.md)
- [ ] Draft announcement using [templates/announcement.md](../../templates/announcement.md)

### T-1 week

- [ ] Announce in Discord and Instagram with prerequisites and a sign-up form if you need a headcount
- [ ] Sign-up form lives outside the repo (names and emails never get committed)
- [ ] Starter repo or files public and linked

### T-2 days

- [ ] Full dry run with a timer
- [ ] Reminder post with the prerequisites again
- [ ] Print anything that needs printing (QR code to the repo, a one-page cheat sheet)

### Day of, T-20 minutes

- [ ] Room open, projector tested, links pinned in Discord
- [ ] Sign-in sheet or form ready
- [ ] Checkpoint repo open on the presenter laptop

## Day-of run sheet (90-minute version)

| Time | Who | Action |
|---|---|---|
| -0:20 | Lead | Tech check; pin links in Discord |
| 0:00 | Helper | Sign in, seat people near a helper if they are new |
| 0:05 | Lead | Why this topic, what everyone will have at the end, where the links are |
| 0:10 | Lead | Setup check: hands up if step 0 works; helpers fix stragglers |
| 0:15 | Lead | Checkpoint 1: demo 5 minutes, build 15 |
| 0:35 | Lead | Checkpoint 2: demo 5, build 15 |
| 0:55 | Lead | Checkpoint 3 or stretch task |
| 1:15 | Lead | Show and tell: 3 or 4 people show what they made |
| 1:25 | Lead | Wrap: where to go next, next meeting, feedback form |
| 1:30 | Everyone | Room cleared |

Helpers: one per 6 to 8 attendees. Helpers walk the room during build blocks; they do not sit at the front.

If ASRCC money paid for anything, say so out loud and on the slides. Acknowledging ASRCC at funded events is a condition of the funding (see [asrcc-funding.md](../02-operations/asrcc-funding.md)).

## After

- [ ] Headcount to the semester attendance record (see [attendance-tracking.md](../02-operations/attendance-tracking.md))
- [ ] Materials committed to the event folder or linked from it (slides as PDF under 1 MB, otherwise link the shared drive)
- [ ] `retro.md` filled in within a week: what worked, what broke, what to change in this playbook
- [ ] Receipts to the Treasurer
- [ ] Thank the helpers in Discord
- [ ] If the workshop is worth repeating, note that in the retro so next semester's team sees it
