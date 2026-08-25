# Semester lifecycle

Every semester runs the same three phases: open, run, close. The folder for the semester (`semesters/<YYYY-term>/`) is the working record for all three. This page is the evergreen shape; the actual dates for a given term live in that term's `calendar.md`.

RCC terms and folder names: Fall (late August to mid December, `YYYY-fall`), Spring (mid February to early June, `YYYY-spring`), Summer (`YYYY-summer`). RCC also runs a short Winter session in January; the club has not used a `YYYY-winter` folder yet, and whether to is a decision for [decision-log.md](decision-log.md) when it comes up.

## The three phases

| Phase | Starts | Ends | Output |
| --- | --- | --- | --- |
| Open | Before the first class day | End of week 2 | Semester folder exists; `goals.md`, `calendar.md`, `budget.md` filled; first meeting held |
| Run | Week 3 | Two weeks before finals | Meetings and events logged as they happen; budget kept current |
| Close | Two weeks before finals | Handoff PR merged | `retrospective.md` and `handoff.md` filled; next semester folder created; accounts transferred |

## Week by week

Weeks are counted from the first day of classes. Fall and Spring are about 17 weeks including finals. Items marked "Spring only" follow the ASRCC funding cycle, which runs on the fiscal year (July 1 to June 30) and lands in spring.

| Week | Phase | What happens | Who |
| --- | --- | --- | --- |
| Before week 1 | Open | Run `scripts/new-semester.sh`. Copy open items from the previous `handoff.md` into `goals.md`. Fill `calendar.md` from the RCC academic calendar (holidays, breaks, finals). Confirm the meeting room and time still hold (Thursdays, 12:50 to 1:50 PM, BLCIS A-210). Confirm the advisor is still the advisor. Confirm [MAINTAINERS.md](../../MAINTAINERS.md) has two admins. | President, repo admin |
| 1 | Open | First weekly meeting. Announce the semester on Discord and Instagram. Start the club recharter packet (RCC requires it every semester; see [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md)). | President, secretary, outreach |
| 2 to 3 | Open | Club Rush (date set by Student Activities each term; record it in `calendar.md`). Update the member count in `roster.md`. Book rooms for the semester's events through the advisor (see [room-booking.md](../02-operations/room-booking.md)). | Outreach, advisor |
| 4 to 6 | Run | Recharter packet submitted before the RCC deadline (published as the first six weeks of the semester; confirm each term). ICC representative attending ICC meetings. First workshop or event. | ICC rep, president, event lead |
| 7 to 9 | Run | Mid-semester check against `goals.md`: what is on track, what is dropped. Budget check: spent vs granted. Spring only: ASRCC funding packets come out early February; start drafting next year's request in `budget.md`. | Officers, treasurer |
| 10 to 13 | Run | Main event of the semester. Spring only: ASRCC funding request due late April to `studentactivities@rcc.edu`; hearings are 15-minute Q&A sessions in mid May. Elections for next year's officers per [elections.md](../00-charter/elections.md) (date `[TBD]` until the constitution sets it). | Event lead, treasurer, president |
| 14 to 15 | Close | Retrospective meeting. Fill `retrospective.md` and start `handoff.md`. Reconcile `budget.md` with actual receipts and reimbursements. | All officers |
| Finals week | Close | Outgoing officers open the handoff PR. Incoming officers review it against the acceptance checklist in [handoff-procedure.md](handoff-procedure.md) and merge. Next semester folder created. | Outgoing and incoming officers |
| After finals | Close | Account and contact transfers per the handoff procedure. Spring only: ASRCC allocation notice arrives by July 1; record the granted amount in the next semester's `budget.md`. | Incoming president, treasurer |

## During the run phase, every week

- Meeting note created with `scripts/new-meeting.sh` and filled the same day.
- Any event that happened gets its `retro.md` filled within a week (the `scripts/new-event.sh` folder already has the file).
- Anything decided that is binding (money, policy, go/no-go) gets a row in [decision-log.md](decision-log.md).
- `budget.md` updated when money is requested, granted, spent, or reimbursed.

## Definition of done for a semester

A semester is closed when all of these are true. This is rule 6 in [maintenance-rules.md](maintenance-rules.md); the incoming team checks it before merging the handoff PR.

- [ ] `semesters/<YYYY-term>/retrospective.md` is filled in: goals vs results, event list with attendance counts, what to keep, what to drop.
- [ ] `semesters/<YYYY-term>/handoff.md` is filled in: open items, account status, contacts, and anything the next team must do in week one.
- [ ] `semesters/<YYYY-term>/budget.md` reconciles: every line has a requested, granted, and spent value, or `[TBD]` with a reason.
- [ ] Every event folder under `semesters/<YYYY-term>/events/` has its `retro.md` filled or marked cancelled.
- [ ] `scripts/check.sh --strict` passes: no template fill markers (the HTML comments the templates carry) are left anywhere in this semester's folder.
- [ ] Every meeting under `semesters/<YYYY-term>/meetings/` has a note (a short one is fine; a missing one is not).
- [ ] Every binding decision from the term appears in [decision-log.md](decision-log.md).
- [ ] The next semester's folder exists and its `goals.md` carries forward the open items from `handoff.md`.
- [ ] [MAINTAINERS.md](../../MAINTAINERS.md) names the incoming admins and still satisfies the two-admin rule.
- [ ] The handoff PR was opened by the outgoing team and merged by the incoming team.
- [ ] Account transfers in [handoff-procedure.md](handoff-procedure.md) are complete, or listed in `handoff.md` with a named owner and date.
