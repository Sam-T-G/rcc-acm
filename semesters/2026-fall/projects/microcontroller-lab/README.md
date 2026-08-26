# Microcontroller lab

## Goal

Run six microcontroller lab days at the weekly meeting this semester, four parallel 30-minute stations each (one per competency tier), so members build fundamental programming skills on hardware they can see respond. Done means: six lab days held, all 24 scheduled station challenges run at least once, attendance counted for each one, and a showcase on the last meeting where pairs demo what they built.

## Owner

Lab lead (an officer the Chair assigns). Treasurer owns the kit purchase and the restock reserve. Chair signs off on the budget line. Advisor is involved only for room booking and on-campus storage.

Proposed by Sam Gerungan on 2026-08-25. Officer names appear here only with consent on file; the roles above are the record.

## Status

`proposed`. Nothing is bought and no date is confirmed until the officer meeting approves the program, the $1,000 cap, and the kit order. See the [decision log](../../../../docs/01-governance/decision-log.md) entry dated 2026-08-25.

## Links

| What | Where |
|---|---|
| Challenge library, kit, setup, facilitator guide (code lives there, not here) | <https://github.com/Sam-T-G/rcc-acm-microcontroller-lab> |
| Evergreen playbook for running a lab day | [docs/03-playbooks/microcontroller-lab-day.md](../../../../docs/03-playbooks/microcontroller-lab-day.md) |
| Kit parts list and pricing | [docs/kit.md in the lab repo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/kit.md) |
| Program shape and tier definitions | [docs/program.md in the lab repo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/program.md) |
| Showcase format | [docs/showcase.md in the lab repo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/showcase.md) |
| Semester budget row | [budget.md](../../budget.md) |
| Dates | [calendar.md](../../calendar.md) |
| Semester goal | [goals.md](../../goals.md) |

## Proposed lab days

All six are Thursdays in the regular meeting slot, 12:50 to 1:50 PM, BLCIS A-210, roughly every other week. Each row is one station; the four stations run in parallel. Every station links to its folder in the lab repo, which holds the card, the starter, the solution, and the wiring table.

Tiers: T0 brand new, T1 intro programming (CIS-5), T2 programming II (CIS-17A), T3 data structures and algorithms (CIS-17B/C). T0 runs MicroPython; T1 through T3 run Arduino C++ on the arduino-pico core. Same board and same pin map at every station.

### Lab day 1: 2026-09-24 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Play Your Riff](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-02-play-your-riff) | MicroPython | sequencing, and calling a function with arguments |
| T1 | [Chiptune Jukebox: melody from parallel arrays](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-01-chiptune-jukebox) | Arduino C++ | parallel arrays walked by one for loop |
| T2 | [Ringtone That Never Blocks](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-01-ringtone-never-blocks) | Arduino C++ | refactoring blocking delay() into a millis() state machine |
| T3 | [Sort race on the LED ring](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-01-sort-race) | Arduino C++ | reading an algorithm's cost from measured compare and swap counts |

### Lab day 2: 2026-10-08 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Cyclone: Stop the Light](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-03-cyclone-stop-the-light) | MicroPython | per-round state variables and one conditional |
| T1 | [Simon Says: Memory Sequence](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-06-simon-says) | Arduino C++ | early return from a function on the first failed comparison |
| T2 | [Bit-Packed Drum Machine](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-03-bit-packed-drum-machine) | Arduino C++ | bit manipulation with shifts and masks |
| T3 | [Snake, but the body is a queue](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-02-snake-queue) | Arduino C++ | ring-buffer queue with O(1) enqueue and dequeue |

### Lab day 3: 2026-10-22 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Parking Sensor](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-05-parking-sensor) | MicroPython | calling a function that returns a value |
| T1 | [Cyclone: loops and modulo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-02-cyclone-loops-and-modulo) | Arduino C++ | modulo arithmetic for wraparound |
| T2 | [OLED Screensaver Sprites](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-04-oled-sprites) | Arduino C++ | a class with update, bounce, and draw methods, then an array of objects |
| T3 | [Unbeatable tic-tac-toe: minimax on the OLED](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-03-minimax-tic-tac-toe) | Arduino C++ | recursion as game-tree search (negamax) |

### Lab day 4: 2026-11-05 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Reaction Duel](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-01-reaction-duel) | MicroPython | if / else if on two button inputs |
| T1 | [Dino Runner on the OLED](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-04-dino-runner) | Arduino C++ | variables as physics state, updated every frame |
| T2 | [Cyclone: state machine](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-02-cyclone-state-machine) | Arduino C++ | splitting updateGame() from drawFrame() so the state decides the frame |
| T3 | [Rhythm game on a ring with a min-heap scheduler](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-04-heap-rhythm-game) | Arduino C++ | binary min-heap priority queue keyed on due time |

### Lab day 5: 2026-11-19 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Bouncing Face](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-04-bouncing-face) | MicroPython | variables that change every pass through the loop |
| T1 | [Air Theremin that snaps to a scale](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-05-theremin-snap-to-scale) | Arduino C++ | writing a function that returns a value |
| T2 | [Steady Tray: IMU-leveled servo with integer smoothing](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-06-steady-tray) | Arduino C++ | reading a sensor struct over I2C and converting units |
| T3 | [Maze race: you versus breadth-first search](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-05-bfs-maze-race) | Arduino C++ | BFS with a queue and a parent array on a grid graph |

### Lab day 6: 2026-12-03 (proposed)

| Tier | Station | Language | Skill it builds |
|---|---|---|---|
| T0 | [Sunflower: a servo that turns toward the light](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t0-06-sunflower-servo) | MicroPython | comparing two sensor readings in one conditional |
| T1 | [Reaction Duel: First Press Wins](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t1-03-reaction-timer) | Arduino C++ | millis() as a stopwatch, unsigned long subtraction |
| T2 | [Interrupt Theremin](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t2-05-interrupt-theremin) | Arduino C++ | external interrupts, a CHANGE-mode ISR that stamps micros() |
| T3 | [Elevator scheduler: one car, eight floors](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-07-elevator-scheduler) | Arduino C++ | scheduling policy as code, chosen from a measured benchmark under a fairness bound |

The T3 station on this day has a second, longer form. [The two-car elevator dispatch workshop](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/challenges/t3-07-elevator-scheduler/workshop.md) takes a whole 60-minute meeting instead of a 30-minute station: a second car goes into the same simulation, teams write the policy that decides which car answers each call, and every team runs the same benchmark so the scores compare. It uses the same board, the same wiring, and no new parts. It is proposed, it is not on the six days above, and running it would mean using a meeting that is not a lab day, or a block at the showcase. Officer meeting decides.

[G-code Lite: a serial command parser drives the rig](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/tree/main/challenges/t3-06-gcode-lite-parser) was the original day 6 T3 station and is written, compiled, and ready. The elevator card took the slot, so G-code Lite is now the T3 spare: it needs no new parts either, and it is the card to swap in if the elevator station has to come out.

### Showcase: 2026-12-10

The last Thursday before finals, in the same slot and room. It runs as an expo: pairs set their board up in a tier lane and judges walk the lanes, four minutes per project, rather than everyone presenting from the front. Then a ladder relay where a team runs one challenge family up the tiers. Awards and a group photo in the last five minutes. Format and rubric: [docs/showcase.md in the lab repo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/showcase.md).

## Purchase plan

Full parts list, vendors, and per-line prices: [docs/kit.md in the lab repo](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/kit.md). Prices there were checked on 2026-08-24 and 2026-08-25. Hard cap for the program is $1,000 including tax and shipping.

Six identical station kits plus a shared pool box, built around the Raspberry Pi Pico 2 W with pre-soldered headers. Spares are built into the base order: 8 boards for 6 stations, 7 breadboards, 7 organizer boxes (the seventh is the pool box).

| Order | Pre-tax | Tax (8.75%, City of Riverside) | Shipping | Reserve | Total |
|---|---|---|---|---|---|
| Base: everything the 24 scheduled challenges need | $533.01 | $46.64 | $45.00 [TBD, estimate] | none | **$624.65** |
| Max: base plus backlog parts and a restock reserve | $661.74 | $57.90 | $60.00 [TBD, estimate] | $150.00 | **$929.64** |

Headroom under the $1,000 cap: $375.35 on the base order, $70.36 on the max order. The backlog parts in the max order (temperature and humidity sensor, RFID reader, 4-digit display, continuous servo, DC motors and driver, battery holders) serve challenges that are written but not scheduled this semester; nothing on the six lab days above needs them.

Shipping on both lines is an estimate. Adafruit and pishop.us compute it at checkout, SparkFun ships free above $100, SunFounder ships free from China, and the Harbor Freight boxes are bought in store.

### Reserve rule

$150 of the max order is held back, not spent at order time. It is released after lab day 2 (2026-10-08) to restock whatever the first two sessions actually killed: servos strip gears, USB cables go bad, and boards get bricked. If the base order is approved instead of the max order, hold $150 of the $375 headroom under the same rule rather than spending it up front.

### Order by 2026-09-03

Three weeks before lab day 1. The long pole is SunFounder, which ships from China in 7 to 14 working days, and that line carries the OLEDs, servos, joysticks, IMUs, and the LED matrix. Ordering on 2026-09-03 leaves about a week of slack for a late or wrong shipment before officers have to wire and test stations on 2026-09-23.

Everything else (Adafruit, pishop.us, SparkFun) ships domestically and can go in the same day. If approval slips past 2026-09-03, either move lab day 1 back two weeks or re-source the SunFounder lines domestically, which [docs/kit.md](https://github.com/Sam-T-G/rcc-acm-microcontroller-lab/blob/main/docs/kit.md) estimates adds roughly $130 to $200 and leaves two parts with no priced US source.

## Risks

| Risk | Why it bites | What we do about it |
|---|---|---|
| Part losses in the first two weeks | Small parts walk off tables and polarity mistakes kill capacitors and LEDs before anyone has a routine. Historically the first two sessions are where a kit gets thinned out | Count every box against a printed packing list at teardown on lab days 1 and 2. Hold the $150 restock reserve until after 2026-10-08. Buy spares up front (8 boards, 10 capacitors, extra buzzers and buttons) rather than reordering one part at a time |
| Room power in A-210 | Four stations plus laptops need outlets, and a servo or an LED ring browning out reads as a mystery software bug | Boards run from laptop USB, not wall bricks. Enforce the power rule: one servo with its capacitor, or one small ring at capped brightness, never both on a board. Count working outlets in A-210 before lab day 1: [TBD] |
| Officer time | A lab day costs five officers on the day plus each station officer building their own challenge beforehand. Every-other-week cadence exists for this reason | Confirm five officers per lab day at T-1 week. Three officers means three stations, not four rushed ones. The cards are written so a new officer can run a station without having designed it |
| Storage between meetings | Seven boxes, seven breadboards, and a hub have to live somewhere on campus or in an officer's car | Ask the advisor for a locked space before the order goes in. Location: [TBD] |
| Attendance dropping mid-semester | Six sessions across a semester is a long run, and a thin room makes stations look empty | Announce the four station names and tiers in Discord a week ahead so people pick before they walk in. Pairs, not solos, so 12 attendees still fills four tables |
| Cap overrun | Tax and shipping are the part nobody remembers | The cap is $1,000 including tax and shipping. Both quoted totals include both. Any add-on after the first order comes out of the reserve, not a new request |

Not a risk: campus WiFi. Every station runs over USB from a laptop, the boards are flashed locally, and no challenge on the six lab days uses WiFi or BLE even though the Pico 2 W has both. A dead network does not stop a lab day.

## Open questions for the officer meeting

1. Approve the program and the $1,000 cap? Approve the base order at $624.65 or the max order at $929.64?
2. Which funding line pays for it: an ASRCC line from the FY 2026-27 allocation, or the old ACM trust account? The allocation amount is still [TBD] and the trust account still has signer problems, so this may decide itself.
3. Who is the lab lead, and which four other officers commit to a lab day rotation?
4. Do the six proposed Thursdays clear the rest of the calendar? Lab day 3 (2026-10-22) and lab day 5 (2026-11-19) sit near the ICPC rehearsal and contest dates, both still [TBD].
5. Where do the seven boxes live between meetings, and who asks the advisor?
6. Shipping is a $45 to $60 estimate. Do we move the seven breadboards to SparkFun (+$12.60 in parts) to clear its $100 free-shipping line?
7. Does anyone apply for the Adafruit educator discount (up to 10%), and under whose name?
8. Do the boards go home with members between lab days, or stay in the boxes? Take-home loaners would need two more boards, about $16.
9. Who owns the showcase on 2026-12-10, and does it need prizes? Prize budget: [TBD].

## Log

- 2026-08-25: Program proposed. Board chosen (Raspberry Pi Pico 2 W), 25 station challenges written and compiled in the lab repo (24 scheduled plus one spare), kit priced at $624.65 base and $929.64 max. The elevator scheduler card holds the lab day 6 T3 slot and adds no parts. Logged in the [decision log](../../../../docs/01-governance/decision-log.md). Pending officer meeting approval.
