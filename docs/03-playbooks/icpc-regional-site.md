# Playbook: ICPC Southern California Regional site

Runbook for the one weekend a year when RCC hosts a site for the ICPC Southern California Regional Contest and fields its own teams. Evergreen rules live here. Each season's dates, headcounts, and spend live under `semesters/<YYYY-term>/events/`.

## Purpose

RCC plays two separate roles on contest day, and they need two separate owners:

1. **Host site.** RCC provides the building, the lab machines, the network, volunteers, and food for every team assigned to the Riverside site. The regional contest directors run the contest itself (problems, judging, clock, scoreboard).
2. **Competing institution.** RCC registers its own teams of three, with a faculty or staff coach, and those students compete like everyone else.

Keeping the two roles apart matters: ICPC rules say the coach cannot be a contestant, the club keeps host volunteers and contestants separate so nobody is torn between the two jobs, and the host budget is separate from the team budget.

## History, for context

- RCC teams first competed in the SoCal regional in 1998. RCC students helped judges with Linux installs in 1999. RCC became a host site in 2000.
- November 2024: RCC hosted 400+ participants from 10+ institutions (Caltech, Harvey Mudd, UCLA, USC, UCSD, UCR, UCI, CSUs). The ACM chapter organized it with support from Dean Shari Yates through the Strong Workforce Grant. Source: <https://www.rcc.edu/about/news/2024-icpc-competition-rcc.html>.
- November 15, 2025: RCC was again a site. Venue: Martin Luther King Jr. Teaching and Learning Center.

## Season facts

Numbers below are from the 2025-26 season page at <https://scl.na.icpc.global/2025-26/>. The 2026-27 date, sites, fees, and registration window were all "to be announced" as of August 24, 2026. Check <https://scl.na.icpc.global/> in early September and copy the confirmed values into the semester folder.

| Item | 2025-26 value | 2026-27 |
| --- | --- | --- |
| Contest date | November 15, 2025 | [TBD] |
| Registration window | September 1 to November 1, 2025 | [TBD] |
| Team fee | $175 per team, invoiced through ICPC QuickBooks | [TBD] |
| Team slots | up to 3 per institution guaranteed; extra slots round-robin after registration closes | [TBD] |
| Online rehearsal | around October 25, 2025 | [TBD] |
| Contest length | 5 hours | same unless announced |
| Contest environment | Intel Core i7, Fedora 42, XFCE; C/C++ 14.2, Java OpenJDK 21, Kotlin 2.0, Python 3.12; DOMjudge | [TBD] |
| Contest directors | Jaime Cabrera and Ed Skochinski, <director@socalcontest.org> | confirm |
| Region | California south of and including San Luis Obispo, Kern, and San Bernardino counties, plus Clark County, Nevada | same |

Use `scl.na.icpc.global`, not `socalcontest.org`. The legacy domain served an expired TLS certificate on 2026-08-24.

## Owner roles

| Role | Who | Does |
| --- | --- | --- |
| Site lead | An officer (not competing) | Single point of contact with the contest directors; owns the host checklist |
| Faculty or staff site contact | Advisor or CIS faculty ([TBD]) | 25Live booking, building access, keys, custodial, Campus Safety, Strong Workforce or dean-level funding |
| Lab lead | A member with Linux experience (not competing) | Machine imaging to the contest spec, network, printer, DOMjudge client checks |
| Volunteer lead | Any officer or member (not competing) | Recruits and schedules volunteers; check-in table, runners, food |
| Food lead | Any officer or member | Food Authorization form, vendor order, delivery timing, dietary needs |
| Coach | Faculty or staff member ([TBD]) | Registers RCC teams, confirms eligibility, is present on contest day |
| Team captains | One per RCC team | Practice schedule, rehearsal login, contest-day materials |

## Host site: T-minus checklist

### T-12 weeks (early September)

- [ ] Confirm with the contest directors that RCC is a site this season, and get the date. Email <director@socalcontest.org>.
- [ ] Ask the advisor to submit the 25Live request for the venue (Martin Luther King Jr. Teaching and Learning Center in 2025; confirm) for the full contest day plus a setup day. Students cannot submit 25Live requests. See [room booking](../02-operations/room-booking.md).
- [ ] Confirm the funding source for hosting. In 2024 it was the Strong Workforce Grant through the dean. Current source: [TBD]. Hosting costs are not a good fit for ASRCC's on-campus-engagement priority, but food for RCC students may be; ask.
- [ ] Create the event folder: `scripts/new-event.sh <semester> <YYYY-MM-DD> icpc-regional`. Fill in the [event plan](../../templates/event-plan.md).
- [ ] Log the go/no-go in the [decision log](../01-governance/decision-log.md).

### T-8 weeks

- [ ] Get the contest environment spec and machine count from the directors. Number of lab machines RCC can provide: [TBD].
- [ ] Lab lead confirms with campus IT who images the machines, when, and whether the lab can boot the contest OS. Owner on the IT side: [TBD].
- [ ] Volunteer lead opens a sign-up in Discord. Target: [TBD] volunteers (the RCC-hosted 2024 event had 400+ participants per the RCC news article; how many were at the Riverside site versus other sites is [TBD]).
- [ ] Draft the site budget (shape below).

### T-4 weeks

- [ ] Registration closes November 1 (2025 pattern). Ask the directors for the team count assigned to the Riverside site.
- [ ] Food lead files the Food Authorization form and prices an order for teams, coaches, and volunteers.
- [ ] Advisor files the Student Activities Event Form and contacts College Safety and Police about the event, parking, and building hours.
- [ ] Print plan: problem sets are usually printed on site. Confirm who prints, how many copies, and where the printer is. [TBD]
- [ ] Signage: room numbers, check-in, restrooms, food, "quiet" signs. Reuse last year's files from the shared drive.

### T-2 weeks

- [ ] Lab lead runs the online rehearsal setup on real lab machines, not a laptop. Every machine: contest OS boots, compilers match the spec, DOMjudge client reaches the judge server, printing works.
- [ ] Volunteer schedule published: setup shift, check-in, runners during the contest, teardown.
- [ ] Send the directors: venue map, parking instructions, site lead phone (privately, not in this repo), Wi-Fi plan for coaches.
- [ ] Confirm the food delivery time and headcount.

### T-1 day (setup)

- [ ] Room laid out: one machine per team, team number on each station, no adjacent teams sharing a monitor line of sight if the directors ask for it.
- [ ] All machines re-imaged or verified; USB ports and network per the directors' instructions.
- [ ] Coach and volunteer room set up; check-in table stocked (team list, name tags, maps).
- [ ] Walk the route from parking to the room with fresh eyes.

## Competing institution: T-minus checklist

### Eligibility self-check (do this before anyone practices seriously)

From the ICPC regional rules at <https://icpc.global/regionals/rules>. The year numbers move every season; store the rule shape here and confirm the current numbers on that page.

- [ ] Enrolled at RCC in a degree program with at least a half-time load.
- [ ] Willing and able to compete in the World Finals if the team advances.
- [ ] Period of eligibility (2025-26 numbers): first began post-secondary studies in 2022 or later, **or** born in 2003 or later. Confirm the current year's cutoffs.
- [ ] Has not competed in five different regional contest years and has not competed in two World Finals. Transfer students count regional years at previous schools.
- [ ] Fifth-year exception for 2025-26 and 2026-27: allowed as long as the student has not completed more than the equivalent of eight semesters of full-time STEM study.
- [ ] Coach is a faculty or staff member and is not a contestant.

### Registration

- [ ] September 1 (2025 pattern): registration opens. Coach registers teams through the ICPC registration system: <https://icpc.global/regionals/finder/Southern-California>.
- [ ] Teams are exactly three contestants. Up to three RCC team slots are guaranteed; ask for more and take what round-robin gives.
- [ ] Fee: $175 per team (2025), invoiced through ICPC QuickBooks. Who pays (club, department, ASRCC): [TBD]. Log it.
- [ ] Practice: weekly problem sessions in the regular meeting slot (Thursdays 12:50 to 1:50 PM, BLCIS A-210) from September until contest week. Use the contest languages only: C, C++, Java, Python 3, Kotlin.
- [ ] Online rehearsal (around October 25 in 2025): every RCC team logs in from a lab machine and submits at least one problem.

### Contest rules to drill

- Five hours. Most problems solved wins; ties broken by cumulative time. 20-minute penalty per rejected submission on a problem that is eventually solved.
- Source files no larger than 300,000 bytes.
- Contestants may bring non-electronic resources (textbooks, paper notes). Phones, laptops, and any machine-readable software or data are banned at the station.
- One machine per team. Practice with one keyboard.

## Day-of run sheet

Times are relative until the directors publish the schedule. Fill in the real clock times in the semester event folder.

| Time | Item | Owner |
| --- | --- | --- |
| Contest start minus 3 h | Volunteers arrive. Lab lead boots every machine and checks judge connectivity. | Lab lead, volunteer lead |
| Minus 2 h | Check-in opens. Teams sign in, get name tags and station numbers. Coaches to the coach room. | Volunteer lead |
| Minus 1 h | Food for breakfast or coffee out (if ordered). Directors' briefing for volunteers: what runners may and may not say to teams. | Food lead, site lead |
| Minus 30 min | Teams seated. Devices collected or bagged per the directors' rule. Problem sets distributed sealed. | Site lead |
| 0:00 | Contest starts. Runners deliver printouts and balloons if the directors use them. | Volunteers |
| About 2:30 | Lunch delivered to the coach and volunteer room; teams get food at their stations only if the directors allow it. | Food lead |
| 5:00 | Contest ends. Nobody touches a machine until the directors say so. | Site lead |
| Plus 30 min | Results and awards, run by the directors. | Directors |
| Plus 1 h | Teardown: machines to their normal image or shut down per IT, furniture back, trash out, keys returned. | Lab lead, volunteers |

Incidents on contest day: site lead first, then the directors. Conduct issues follow the [code of conduct](../../CODE_OF_CONDUCT.md); ICPC's own rules govern contest disputes.

## After

- [ ] Within 3 days: Treasurer or site lead collects receipts and files reimbursements. See [reimbursements](../02-operations/reimbursements.md).
- [ ] Within 1 week: fill in the [retro](../../templates/event-retro.md) in the event folder. Record team count at the Riverside site, RCC team results, volunteer count, machine failures, food headcount versus order, and spend versus budget.
- [ ] Thank-you notes to the dean, IT, custodial, and Campus Safety contacts. Post results to Discord and Instagram (photos of people only with consent).
- [ ] If the club's ACM annual report is due, the contest counts as a meeting or activity; note it for the Treasurer.
- [ ] Update this playbook only for rule or process changes. Dated facts go in the semester folder.

## Budget shape

No verified dollar figures for hosting exist in this repo yet. The 2024 site was funded through the Strong Workforce Grant, not the club. Fill in real numbers from the first season that runs on this playbook.

| Line item | Host or team | How to estimate | Figure |
| --- | --- | --- | --- |
| Team registration | Team | $175 per team (2025) times RCC teams | 3 teams = $525 at the 2025 rate |
| Food (teams, coaches, volunteers) | Host | Headcount times per-head cost, two meals plus snacks | [TBD] |
| Printing | Host | Problem set pages times team count, plus signage | [TBD] |
| Balloons, name tags, supplies | Host | Per team plus check-in table | [TBD] |
| Volunteer shirts (optional) | Host | Per volunteer | [TBD] |
| Custodial or building overtime | Host | Ask the advisor whether the college charges the club | [TBD] |
| Machine imaging or spare hardware | Host | Usually IT time, not money | [TBD] |
| Contingency | Both | 5 to 10 percent | [TBD] |

## Links

- SoCal regional (current season): <https://scl.na.icpc.global/>
- SoCal regional 2025-26 page: <https://scl.na.icpc.global/2025-26/>
- Contest rules (regional): <https://scl.na.icpc.global/contest-rules/>
- General contest information: <https://scl.na.icpc.global/general-contest-information/>
- ICPC regional rules and eligibility: <https://icpc.global/regionals/rules>
- ICPC North America regions: <https://na.icpc.global/regionals/>
- RCC news, 2024 regional at RCC: <https://www.rcc.edu/about/news/2024-icpc-competition-rcc.html>
- Room booking: [room-booking](../02-operations/room-booking.md); event checklist: [event-checklist](../02-operations/event-checklist.md)
- Templates: [event-plan](../../templates/event-plan.md), [event-run-sheet](../../templates/event-run-sheet.md), [event-retro](../../templates/event-retro.md)
- Playbook index: [README](README.md)
