# Playbook: Microcontroller lab day

## Purpose

A lab day turns the regular Thursday meeting into four parallel hands-on stations, one per competency tier, each running a 30-minute microcontroller challenge. Students pick a difficulty, not a topic, and leave with something that blinks, beeps, or moves and code they wrote themselves. It is the Build and Learn pillars on the club's own hardware, and it is cheaper to repeat than a workshop because the same kit comes back every time.

Use this playbook instead of the [workshop](workshop.md) one when the session fits the normal meeting hour, uses the club's own kit, and runs several difficulty levels at once. Use the [workshop](workshop.md) playbook when the session needs a longer block, a different room, food, or outside attendees.

The challenge library, the kit list, the setup steps, and the facilitator guide live in a separate repo so this one stays free of code: <https://github.com/Sam-T-G/rcc-acm-microcontroller-lab>.

| What you need | Where it is |
|---|---|
| Station cards (one per challenge: card, starter code, solution, wiring) | [challenges/](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges) |
| Program shape, tiers, and design rules | [docs/program.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/program.md) |
| Kit parts list and what it costs | [docs/kit.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/kit.md) |
| One-time installs and the per-station routine | [docs/setup.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/setup.md) |
| Running the hour, unsticking students, troubleshooting | [docs/facilitator-guide.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/facilitator-guide.md) |
| Fixed pin map every card assumes | [docs/wiring-conventions.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/wiring-conventions.md) |
| End-of-semester showcase format | [docs/showcase.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/showcase.md) |

## When

| | |
|---|---|
| Day and time | The regular meeting slot: Thursdays, 12:50 to 1:50 PM |
| Room | BLCIS A-210 |
| Cadence | Roughly every other week, so officers have a full week to build and test the next four stations |
| Skips | Campus holidays, finals week, and the weeks the semester calendar marks as off |
| Lead time | Start the checklist 2 weeks before the first lab day of a run; a single repeat lab day needs 1 week |

Parts ordering is the long pole and it sits outside this checklist. Vendors that ship from overseas have run 7 to 14 working days, so the kit order goes in at least three weeks before the first lab day of the semester. That date belongs in the semester `calendar.md`, not here.

A lab day sits inside the regular meeting, is not open to non-members, and serves no food, so it does not meet the campus-event condition the [workshop](workshop.md) playbook lists and no Student Activities Event Form is started. Confirm that reading with the advisor once, at the start of the program: [TBD]. If a lab day is ever opened up as a campus event, work [event-checklist.md](../02-operations/event-checklist.md) instead.

## Owner

Lab lead: an officer the Chair assigns for the semester. The lab lead picks the four challenges for each day, assigns station officers, and owns the kit inventory.

Per lab day you need one officer per station plus one floater, so five officers for four stations at about 22 members. That is the ratio the challenge library is written for: one facilitator per 4 to 6 people. If only three officers are free, run three stations and drop the tier nobody signed up for.

The Treasurer owns the kit purchase and the restock reserve. The Chair signs off on the semester budget line. The advisor is only involved for room booking and campus storage.

## Design rules

- One board, one pin map. Every station uses the same board and the same base wiring, so any card runs at any table and a dead station is a swap, not a rebuild.
- Wiring is officer work. Boards are wired, flashed, and smoke-tested the day before. A student's 30 minutes are for code. Students touch 3 to 6 wires at most, and only when the card says so.
- The starter always compiles and always does something on power-up. A starter that fails to build is a dead station and the student blames themselves.
- Steps 1 and 2 on a card are reachable in the first 10 minutes. If the first visible result is at minute 20, the card is wrong.
- Faded scaffolding by tier. The lowest tier gets a complete working program and changes constants and one conditional; the highest gets function signatures and a pass/fail harness and writes the algorithm.
- Pair work at every station. Two students per board, one driver and one reviewer, and the facilitator calls the swap at the 10-minute mark. Buying one board per person is how pair work disappears.
- Self-select the tier. Name the four stations out loud with one sentence each and let people walk to the table they want. No quiz, no prerequisite check. A facilitator nudge is a question asked once, and either answer is fine.
- Every card names the skill it builds and carries one 60-second check the facilitator asks the non-driver. "It works" is not the check.
- Power rule: one servo with its capacitor, or one small LED ring at capped brightness, never both on the same board. USB current is the limit and brownouts read as mystery bugs.
- Safety: no mains voltage, no soldering during the session, no lithium cells outside a protected board.
- Anything a facilitator learns goes back into the challenge repo the same day, so the cards carry the knowledge after the officer who ran that station graduates.

## T-minus checklist

### T-2 weeks

- [ ] Lab lead assigned by the Chair and named in the semester `projects/` folder
- [ ] Lab days on the semester `calendar.md` with the kit order-by date ahead of the first one
- [ ] Kit funded: budget line in the semester `budget.md`, and a [decision log](../01-governance/decision-log.md) entry for the spending cap and the board choice
- [ ] Kit ordered against [docs/kit.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/kit.md), with spares, and a restock reserve held back
- [ ] Storage for the boxes between meetings confirmed with the advisor
- [ ] The four challenges for the first lab day picked from the library and read end to end by the lab lead

### T-1 week

- [ ] One officer assigned per station, plus a floater
- [ ] Each station officer builds their own station's challenge from the starter, on the real hardware, start to finish. Over 20 minutes for an officer means the card needs a fix before Thursday
- [ ] Libraries and drivers installed at the versions the cards name; every starter and every solution compiles or parses
- [ ] Parts counted against the four cards; anything short is ordered with lead time or the card is swapped
- [ ] Station names, tiers, and one-line prereqs posted in Discord so members can pick before they walk in
- [ ] Station laptops confirmed. Chromebooks do not drive the boards; they go to the simulator table

### T-1 day

- [ ] Every station wired per its `wiring.md` by an officer, and photographed from directly above
- [ ] Smoke test at every station: each LED, each sensor, the servo, the ring
- [ ] Both language tracks pre-flashed, and each board runs its starter with no laptop attached
- [ ] Boards and cables labeled by station; parts bagged by type with a printed count
- [ ] Cards printed, one per station, with the pin table on the back
- [ ] Tested-cable bag packed; any cable that failed once is retired, not repacked

### Day of, T-20 minutes

- [ ] Tables out, one station per table, boxes open
- [ ] Every board powered and running its starter before any laptop is opened
- [ ] Laptops on, editor open, correct file loaded, serial monitor or shell open at the right baud rate
- [ ] Capacitor check at every station that moves a servo or lights a ring
- [ ] Whiteboard: four station names, tier, one-line prereq each
- [ ] Simulator table set up for anyone without a station board
- [ ] Headcount sheet or form at the door

## Day-of run sheet (60-minute meeting)

| Time | Who | Action |
|---|---|---|
| 12:30 | Lab lead | In the room, tables and boxes out, power up, smoke check |
| 12:50 | Note taker | Doors and sign in; new faces get pointed at a station and at Discord |
| 12:53 | Chair | Announcements, 3 minutes, hard stop |
| 12:56 | Lab lead | Name the four stations: what you build, what you should already be able to do. People walk to a table |
| 13:00 | Station officers | Intro at the table, 3 minutes: run the starter, narrate one change, no lecture |
| 13:03 | Pairs | Build block. Officers walk the table, mark completions, never type for a student |
| 13:13 | Station officers | Call the driver swap out loud |
| 13:25 | Station officers | Stop new work. Demos at the table, then the 60-second check asked of the non-driver |
| 13:33 | Lab lead | Two or three demos to the whole room, one per tier if the timing allows |
| 13:40 | Lab lead | Wrap: next lab day, which tiers run, the repo link, one ask |
| 13:43 | Everyone | Tear down: boards back in the labeled box, cables coiled, dead parts into the hospital bag |
| 13:50 | Lab lead | Room clear, boxes to storage |

Notes on the shape:

- The build block is 22 minutes of real work. Anything that eats into it (a long announcement, a laptop that will not see its port) comes out of the demo, so protect it.
- A pair that finishes in 12 minutes goes to the stretch goals first, then gets pointed at the tier above for next time.
- A pair stuck on step 1 at the 12-minute mark gets one question: the tier below runs the same idea with more of the code written. Either answer is fine.
- If ASRCC money paid for the kit, say so out loud at the announcements and put it on the slide or the whiteboard. Acknowledgment is a condition of the funding (see [asrcc-funding.md](../02-operations/asrcc-funding.md)).

## After

- [ ] Headcount to the semester attendance record, split by station if the sheet allows (see [attendance-tracking.md](../02-operations/attendance-tracking.md))
- [ ] Officer retro at the table, 10 minutes, same day: which cards ran long, which step lost people, what broke
- [ ] Card fixes opened as pull requests against the challenge repo the same week, while the detail is still fresh
- [ ] Inventory reconciled against the packing list; losses and dead parts written down
- [ ] Restock ordered from the reserve if any station cannot run next time
- [ ] Photos and student write-ups collected for the showcase and for the semester retrospective
- [ ] Kit spend and restock spend added to the semester `budget.md`; receipts to the Treasurer per [reimbursements.md](../02-operations/reimbursements.md)
- [ ] Next lab day's four challenges picked before the officers leave the room
