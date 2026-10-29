# Deck copy

ACM @ RCC, first meeting of Fall 2026. Thursday 2026-09-03, 12:50 to 1:50 PM, BLCIS A-210. Single HTML file, 1920 x 1080, light theme, Inter and JetBrains Mono from fonts.googleapis.com only.

Slide type floor from the design system (assets.md §10.5, `design-system` branch): title 72 px, body 40 px, ledger line 32 px, margins 96 px, one idea per slide, at most one callout per slide. Working body area is 1728 x 888 px; after a title and eyebrow, roughly 700 px of body, which is about 11 rows of 40 px table text. Every slide split below is sized to fit in that 700 px.

## 1. Source table

Every number, date, and fact used on screen or in notes. "prep" is `semesters/2026-fall/meetings/2026-09-03-prep.md`. "plan" is `semesters/2026-fall/meeting-plan.md` on the `meeting-structure` branch. "lab README" is `semesters/2026-fall/projects/microcontroller-lab/README.md` on the `microcontroller-lab-program` branch. "kit" and "program" are `docs/kit.md` and `docs/program.md` in `rcc-acm-microcontroller-lab`. Design-system files are on the `design-system` branch under `docs/04-brand/design-system/`.

| Fact | Value | Source | Discrepancy or note |
|---|---|---|---|
| Meeting day, time | Thursday 2026-09-03, 12:50 to 1:50 PM | prep header; `docs/03-playbooks/weekly-meeting.md`; `docs/00-charter/mission.md` | none |
| Room | BLCIS A-210 | same three files | none |
| Room handoff | GDG takes A-210 at 2:30 | prep header | none |
| Run sheet blocks | 12:50 doors 5; 12:55 club 8; 13:03 semester 8; 13:11 lab and money 12; 13:23 seats 12; 13:35 questions 10; 13:45 close 5; 13:50 out | prep run sheet | The Board has no line of its own in the prep run sheet. plan standing rules and design-system components.md line 83 say the Board runs every week (five minutes on a regular meeting). This deck takes one minute for it at the top of Block 1. Flagged, not solved. |
| Club name on slides | ACM @ RCC | `docs/04-brand/brand.md` Names table | none |
| One sentence | "where students who want to get good at computing practice together, chartered under ACM" | prep Block 1; mission.md | none |
| Four pillars, one line each | Build, Compete, Learn, Connect | prep Block 1 table; mission.md | mission.md names Google and Amazon in Connect; prep says "large tech companies". Screen uses the shorter form. |
| ICPC host site since | 2000 | mission.md (cites RCC news 2024); prep | none |
| RCC teams competing since | 1998 | mission.md; prep | none |
| Cal Hacks 12.0 | 11 members accepted, Fall 2025 | mission.md; prep | none |
| Active members | 22, as of the Spring 2026 ASRCC funding request | mission.md; prep; program.md ("about 22") | none |
| "Most community colleges do not host anything" | claim in prep Block 1 | prep only | Not in mission.md and unsourced. Kept off screen and out of the notes. |
| Discord | discord.gg/fM2HbsJyBG | mission.md; prep; weekly-meeting.md | none |
| Instagram | instagram.com/rcc.acm, handle rcc.acm | prep Block 1; weekly-meeting.md | none |
| QR placement | Discord QR and Instagram QR on one slide, up during doors and again at close | prep day-of checklist | The repo file `assets/rcc-acm-qr-code.png` encodes a target that brand.md marks `[TBD]`. Do not reuse it. Embed a freshly generated QR for the Discord invite as inline SVG or a data URI (no external resources allowed). |
| Fifteen Thursdays | Sep 3 through Dec 10 | plan table; prep Block 2 table | plan has Aug 27 kickoff with the lab vote and Sep 3 as career internships, Oct 1 as the first full drill. prep reshuffle supersedes: Sep 3 is the kickoff, Oct 1 becomes career internships, the Oct 1 drill merges into the Oct 29 mock contest. Deck follows prep. |
| Semester shape | 6 lab days, 2 career, 2 ICPC, 1 hackathon, 1 showcase | prep Block 2 | plus today, Sep 17 dev environment, Nov 26 no class = 15. Checks out. |
| Nov 26 | no class, Thanksgiving week, classes not in session Nov 23 to 29 | plan | none |
| Warm-up track | every regular meeting opens with a 15-minute contest problem; lead rotates; lowest-stakes way to run part of a meeting | prep Block 2; plan | none |
| The Board rule | every dated thing in the next four weeks, one line each | plan standing rules; components.md line 83; assets.md §10.5 | none |
| Sep 10 | ICPC: format, teams, registration | prep; plan | none |
| Sep 17 | Dev environment and git, the week before lab day 1 | prep; plan | none |
| Sep 24 | Lab day 1, proposed, depends on the order going out today | prep; plan; lab README; kit | none |
| Club Rush | Student Activities sets it; historically three days in mid September on Terracina Drive; `[TBD]`; confirm with studentactivities@rcc.edu | prep Block 2 | The task brief says "week of Sep 8". No file read supports that week. The Board line says "mid September, dates [TBD]" and nothing more specific. If Sam has a source for the week of Sep 8, add it; otherwise do not say it. |
| Dec 10 | showcase: expo, ladder relay, awards; last instruction Thursday | prep; lab README; plan | none |
| Board | Raspberry Pi Pico 2 W, pre-soldered headers | lab README; program; kit | none |
| Lab format | six lab days, four parallel 30-minute stations, one per tier | lab README; program; prep | none |
| Tiers | T0 brand new, MicroPython; T1 CIS-5; T2 CIS-17A; T3 CIS-17B/C; T1 to T3 Arduino C++ | lab README; program; prep | none |
| Same board, same pin map at every station | yes | lab README; program | none |
| Challenge count | 24 scheduled, 25 written (one spare, G-code Lite) | lab README log; program scale line | none |
| Station names | per lab day, see lab README "Proposed lab days" and program "Lab days at a glance" | both agree | none |
| Elevator station | Dec 3 T3 is "Elevator scheduler: one car, eight floors". The two-car dispatch is a proposed 60-minute workshop, not scheduled | lab README; program | prep says "a two-car elevator scheduler". Screen and notes use the scheduled one-car name. |
| The ladder | same hardware at rising tiers; Cyclone T0 day 2, T1 day 3, T2 day 4 | program "The ladder"; prep | none |
| Cap | $1,000 including tax and shipping | kit; lab README; prep | none |
| Base order | $624.65 (pre-tax $533.01, tax $46.64, shipping $45.00 estimate) | kit §8; lab README; prep | none. kit also says "ask the treasurer for $675" to absorb shipping; notes only. |
| Max order | $929.64 (pre-tax $661.74, tax $57.90, shipping $60.00 estimate, reserve $150.00) | kit §9; lab README; prep | none |
| Tax | 8.75%, City of Riverside | kit; prep | none |
| Headroom under cap | $375.35 base, $70.36 max | kit §8, §9; lab README | kit §11 also says "$346 of headroom" for the base variant. Internal inconsistency in kit.md; neither figure is on screen. |
| Restock reserve | $150, held until after lab day 2 (Oct 8); at the base order, hold $150 of the headroom under the same rule | kit §9; lab README | prep says "roughly $114 to $375 depending on which order goes out". $114 appears in no lab-repo file read. Screen uses $150 from kit.md. |
| Spares | 8 boards for 6 stations, 7 breadboards, 7 boxes (seventh is the pool box) | kit §4; lab README | none |
| Vendor lead time | SunFounder from China, 7 to 14 working days | kit §7, §11; lab README; prep | none |
| Order-by date | 2026-09-03, today | kit; lab README; plan; prep | none |
| If the order slips | lab day 1 moves back about two weeks (prep names Oct 8), or re-source domestically at about $130 to $200 more | lab README; kit §11; prep | kit adds that two parts have no priced US source. Notes only. |
| Code repo | github.com/Sam-T-G/rcc-acm-microcontroller-lab, public | lab README; prep | none |
| "CI compiles all 52 sketches" | prep Block 3 | prep only | 52 appears in no lab-repo doc. The repo holds 42 `.ino` and 14 `.py` files; `scripts/compile-all.sh` prints its count only at run time. Kept off screen. Notes say "CI compiles every sketch" with no number. |
| Governance | quorum `[TBD]` in constitution.md; Chair, Vice Chair, Treasurer, Faculty Advisor `[TBD]` in roster.md; no body can bind a purchase today | prep "Read this first" | prep cites those files; I did not read them. Taken as prep states it. |
| What today can do | straw poll recorded as a count; advisor sign-off outside the meeting; decision-log entry worded honestly | prep | none |
| RCC recognition | at least 7 fee-paid students incl. President, Treasurer, ICC Rep, plus a full-time faculty advisor | prep Block 4; confirmed by grep in `docs/02-operations/club-recognition-and-icc.md` lines 11 to 13 | none |
| Officer seats and weekly cost | six seats, RCC and ACM titles, all open | prep Block 4 table; `docs/00-charter/officer-roles.md` | none |
| ACM Student Membership | $19 per year as of 2026-08-24; required for Chair, Vice Chair, Treasurer | officer-roles.md; prep | none |
| ICC meeting | Mondays 9:30 AM, Bradshaw Center Hall of Fame; three absences in a semester costs good standing | officer-roles.md; prep ("Bradshaw Center") | Screen uses the shorter "Bradshaw Center". |
| Secretary | optional under ACM; notes within 48 hours | officer-roles.md; prep | none |
| Non-officer jobs | ICPC coach (faculty or staff, cannot be a contestant); lab lead; warm-up lead; repo admin 2 | prep Block 4 table | none |
| On-ramp | warm-up, back up a lab day, take notes, then a seat | prep Block 4 | none |
| Elections | month `[TBD]` in elections.md; whether a fall election is required is unresolved | prep; plan | none |
| Privacy | names on the interest sheet only; names in roster.md only with written consent; the sheet does not go in the repo | prep Blocks 4 and 5; weekly-meeting.md | none |
| Expected questions | five, with answers | prep Block 5 | none |
| ICPC in one line | three people, one computer, five hours, a set of problems; RCC hosts a site | prep Block 5 | none |
| Close | one ask, Discord; next Thursday is ICPC; lab decision in one sentence with a name; out by 1:50 | prep Block 6 | none |
| Slide spec | 1920 x 1080, 96 px margins, light theme, title 72, body 40, ledger 32, the Board is one slide, at most one callout per slide | assets.md §10.5 | assets.md also says "The Rail once, on the title slide." The prep scaffold wants the Rail's Break to move per slide by pillar. That gets decided when the deck is built. Pillar tags are given per slide below so either reading can be built. |
| Callout types | Note (useful, not critical), Warning (money, safety, privacy, room booking), Check (the one ask a meeting ends with) | components.md §7.7 | none |
| Eyebrow | pillar name, date, or "Fall 2026" | components.md hero anatomy; assets.md ledger line | none |
| Placeholders not to announce | Club Rush dates; ICPC registration ~Sep 1, rehearsal ~Oct 25, regional ~Nov 15 are 2025 figures; Cal Hacks 13.0 dates; FY 2026-27 ASRCC allocation ($12,000 requested, outcome unrecorded); UC transfer window Oct 1 to Nov 30 `[confirm 2027 dates]` | prep Block 2; plan | none |

## 2. Slide list

Sixteen slides. The ten-slide scaffold is kept in order. Changes and why:

- Added slide 2, the Board, as the design system requires.
- Added slide 6, "What you get". The prep doc's Block 1 has this beat and "any major, any level" after the proof, and the scaffold had no slide for it. Cut it first if Block 1 runs long.
- Split the semester (scaffold 5) into 7 and 8. A 15-row table is 16 rows with the header, about 900 px at 40 px body, and the body area is about 700 px. Slide 7 is the shape (five lines). Slide 8 is a three-column, five-row date grid, one line per cell, 280 px tall, lab days marked. The Board (slide 2) already lists the next four weeks in detail, so slide 8 only has to be readable; the presenter doesn't read it aloud.
- Split the lab block (scaffold 6 and 7) into 9, 10, and 11. The order-by dependency and the show of hands are one idea and get their own slide, so the money slide stays at four numbers.
- Split the seats (scaffold 8) into 12 (the six officer seats, the photographed slide) and 13 (the four non-officer jobs). Ten rows with a callout does not fit at 40 px.
- Added slide 15 for the ten-minute questions block, which otherwise has nothing on screen.

Station names and event names keep the capitalization they have in the repo (Play Your Riff, Cal Hacks 12.0, Club Rush). Everything else is sentence case.

| # | id | Title | Pillar | Block |
|---|---|---|---|---|
| 1 | s01-title | ACM @ RCC | none | 12:50 doors |
| 2 | s02-board | The next four weeks | none | 12:55 |
| 3 | s03-sentence | One sentence | none | 12:55 |
| 4 | s04-pillars | Four pillars | all | 12:55 |
| 5 | s05-proof | Proof | Compete | 12:55 |
| 6 | s06-what-you-get | What you get | none | 12:55 |
| 7 | s07-shape | Fifteen Thursdays | none | 13:03 |
| 8 | s08-dates | The dates | none | 13:03 |
| 9 | s09-lab | Six lab days on a Pico 2 W | Build | 13:11 |
| 10 | s10-money | The money | Build | 13:11 |
| 11 | s11-decision | Order today, or lab day 1 moves | Build | 13:11 |
| 12 | s12-seats | Six seats, all open | Connect | 13:23 |
| 13 | s13-jobs | Four more jobs | Connect | 13:23 |
| 14 | s14-on-ramp | The on-ramp | Connect | 13:23 |
| 15 | s15-questions | Questions | none | 13:35 |
| 16 | s16-ask | Join the Discord | none | 13:45 |

---

### Slide 1: s01-title

**Title:** ACM @ RCC
**Eyebrow:** Fall 2026
**Pillar:** none. The Rail sits on this slide.

**Screen copy:**

> ACM @ RCC
>
> Thursdays, 12:50 to 1:50 PM
> BLCIS A-210

QR (Discord invite, generated inline), captioned:

> discord.gg/fM2HbsJyBG

Ledger line, 32 px, bottom:

> instagram.com/rcc.acm

**Callout:** none.

**Speaker notes:**

- This slide holds for the whole doors block. Do not talk over it.
- Sign-in sheet at the door. The person taking the headcount is [TBD]. Grab someone before 12:50, not after.
- Point every new face at the QR. That is the only job of these five minutes.
- Start at 12:55 on the clock, whatever the room looks like.

**Timing:** 12:50, doors, sign-in, Discord QR up, 5 min.

---

### Slide 2: s02-board

**Title:** The next four weeks
**Eyebrow:** Thursday, Sep 3
**Pillar:** none

**Screen copy, one line per dated thing:**

> Today: kit order-by date for the lab
> Sep 10: ICPC. Format, teams, registration
> Sep 17: Dev environment and git
> Sep 24: Lab day 1, if the order goes out today
> Club Rush: mid September, dates [TBD]

**Callout:** none.

**Speaker notes:**

- Read the five lines. Sixty seconds, then move on. This is the Board; it runs every week.
- Today is the order-by date for the lab kit. We come back to that at 1:11.
- Club Rush is set by Student Activities. It is not confirmed. It goes in Discord the day it is.
- Two clubs share this room: GDG on Campus meets here at 2:30. Different club. Plenty of people do both.

**Timing:** 12:55, first minute of Block 1 (the prep run sheet has no separate Board line; take it out of the 8 minutes).

---

### Slide 3: s03-sentence

**Title:** none on screen (type only, no chrome)
**Eyebrow:** none
**Pillar:** none

**Screen copy, at title size:**

> Where RCC students who want to get good at computing practice together.

Ledger line under it:

> Chartered under ACM, the professional association for computing.

**Callout:** none.

**Speaker notes:**

- Say the full sentence: the ACM Student Chapter at RCC is where students who want to get good at computing practice together, and it is chartered under ACM, the professional association for computing.
- Do not open with the constitution. Do not open with the officer list.
- One sentence, then the four words.

**Timing:** 12:55, Block 1, what this club is, 8 min.

---

### Slide 4: s04-pillars

**Title:** Four pillars
**Eyebrow:** Fall 2026
**Pillar:** all (the sweep, if the Rail moves)

**Screen copy, four cells, pillar name as the cell heading:**

| Pillar | Line |
|---|---|
| Build | Projects, hackathons, the website, the AI Hackathon we run |
| Compete | Weekly problems, the ICPC regional, collegiate hackathons |
| Learn | Workshops, study sessions, speakers, help with CS courses |
| Connect | Discord, meetings, trips, alumni in tech |

**Callout:** none.

**Speaker notes:**

- These are the four words on the website. Every event we run fits at least one.
- Build: projects, hackathons, the chapter website, and the AI Hackathon we run ourselves.
- Compete: a problem every week, the Southern California ICPC Regional, collegiate hackathons.
- Learn: workshops, study sessions, guest speakers, help with the transfer-level CS courses.
- Connect: Discord, these meetings, trips, and an alumni network that reaches large tech companies.

**Timing:** 12:55, Block 1, 8 min.

---

### Slide 5: s05-proof

**Title:** Proof
**Eyebrow:** Compete
**Pillar:** Compete

**Screen copy, three numbers, large, one label each:**

> 2000
> ICPC regional host site since
>
> 1998
> RCC teams competing since
>
> 11
> members accepted to Cal Hacks 12.0, fall 2025

**Callout:** none.

**Speaker notes:**

- Three facts so this does not sound like a poster.
- RCC has hosted a Southern California ICPC Regional site since 2000. RCC teams have competed since 1998.
- Last fall, 11 of our members were accepted to Cal Hacks 12.0.
- As of the spring funding request, 22 active members. That is the room you are joining.

**Timing:** 12:55, Block 1, 8 min.

---

### Slide 6: s06-what-you-get

**Title:** What you get
**Eyebrow:** Fall 2026
**Pillar:** none

**Screen copy, four lines:**

> A team for the contest
> People to build with
> A resume line you made
> Transfer evidence

**Callout (Note):** Any major, any level. Nobody gets screened at the door.

**Speaker notes:**

- Say this to the room and mean it. A team for the contest. People to build with when a class project is bigger than one person. A resume line that is a thing you made rather than a club you joined. A transfer application with evidence in it.
- Any major, any level. The lab program is tiered from "never written code" upward on purpose.
- Housekeeping, thirty seconds: every Thursday, 12:50 to 1:50, this room. Discord is where everything actually happens. Instagram is rcc.acm.
- Cut this slide first if the block is running past 1:03.

**Timing:** 12:55, Block 1, 8 min (ends 13:03).

---

### Slide 7: s07-shape

**Title:** Fifteen Thursdays
**Eyebrow:** Fall 2026
**Pillar:** none

**Screen copy, five lines:**

> 6 lab days
> 2 career meetings, set against deadlines that do not move
> 2 ICPC meetings, set against the season
> 1 hackathon meeting
> 1 showcase, Dec 10

**Callout (Note):** Every regular meeting opens with a 15-minute contest problem. The warm-up lead rotates.

**Speaker notes:**

- Say the shape, not the table. Six lab days. Two career meetings placed against deadlines that do not move. Two ICPC meetings placed against the season. One hackathon meeting. One showcase on Dec 10.
- The other three Thursdays: today, the dev environment session on Sep 17, and Thanksgiving week off.
- Every regular meeting opens with a 15-minute contest problem. That is the ICPC preparation, spread out instead of crammed.
- Running one warm-up is the lowest-stakes way to run part of a meeting. Say that line; it recruits.

**Timing:** 13:03, Block 2, the semester on one page, 8 min.

---

### Slide 8: s08-dates

**Title:** The dates
**Eyebrow:** Fall 2026
**Pillar:** none

**Screen copy, three columns of five, one line per cell, lab days and the showcase marked (orange tag or weight, builder's call):**

| Column 1 | Column 2 | Column 3 |
|---|---|---|
| Sep 3 · Today: kickoff | Oct 8 · Lab day 2 | Nov 12 · Hackathon planning |
| Sep 10 · ICPC: teams | Oct 15 · Career: resume, transfer | Nov 19 · Lab day 5 |
| Sep 17 · Dev environment, git | Oct 22 · Lab day 3 | Nov 26 · No class |
| Sep 24 · Lab day 1 | Oct 29 · ICPC mock contest | Dec 3 · Lab day 6 |
| Oct 1 · Career: internships | Nov 5 · Lab day 4 | Dec 10 · Showcase |

Ledger line, 32 px:

> Lab days depend on today's order. ICPC dates follow the season calendar once it is published.

**Callout:** none.

**Speaker notes:**

- Do not read the grid. Point at two things: lab days are every other week from Sep 24, and Dec 10 is the showcase.
- Oct 1 is the internship timeline, because fall is when summer applications open. Oct 15 is resume and transfer, inside the UC window.
- Sep 10 and Oct 29 are placed against last season's ICPC dates. They move once the real calendar is out.
- Anything not on this grid is not confirmed. Club Rush, Cal Hacks 13.0, the ICPC calendar: "not confirmed yet, it goes in Discord the day it is."

**Timing:** 13:03, Block 2, 8 min (ends 13:11).

---

### Slide 9: s09-lab

**Title:** Six lab days on a Pico 2 W
**Eyebrow:** Build
**Pillar:** Build

**Screen copy:**

> Four stations, one per tier, 30 minutes each.

Tier strip, four cells:

| T0 | T1 | T2 | T3 |
|---|---|---|---|
| Never written code. MicroPython | CIS-5. Arduino C++ | CIS-17A. Arduino C++ | CIS-17B/C. Arduino C++ |

Three station names:

> Play Your Riff (T0)
> Bit-Packed Drum Machine (T2)
> Snake, but the body is a queue (T3)

Ledger line, 32 px:

> Same board and same pin map at every station. The same build comes back at a higher tier.

Build note: the scaffold wants one photo of a wired board here instead of a diagram. No photo exists in the files read. [TBD: photo]. Ship the slide without one rather than with a stock image.

**Callout:** none.

**Speaker notes:**

- Six lab days this semester. Four stations run at once, one per skill tier, 30 minutes each, on a Raspberry Pi Pico 2 W. Everyone builds something that physically responds in the room.
- T0 has never written code and runs MicroPython. T1 through T3 run Arduino C++ and line up with CIS-5, CIS-17A, and CIS-17B/C.
- Name the stations, they sell it better than the structure: Play Your Riff. Cyclone: Stop the Light. A drum machine where the beat is packed into bits. Snake where the body is a queue. Tic-tac-toe you cannot beat. An elevator scheduler, one car, eight floors.
- The ladder is the feature. Same board every time, so a T0 member can see exactly what the T2 version of their own project looks like.
- Three minutes here. The money is next.

**Timing:** 13:11, Block 3, the lab program and the money, 12 min (pitch, 3 min).

---

### Slide 10: s10-money

**Title:** The money
**Eyebrow:** Build
**Pillar:** Build

**Screen copy, four numbers, one label each:**

> $1,000
> cap
>
> $624.65
> base order
>
> $929.64
> max order
>
> $150
> restock reserve, held until after lab day 2

Ledger line, 32 px:

> Both totals include 8.75% tax and a shipping estimate. Six station kits plus spares. Code and wiring: github.com/Sam-T-G/rcc-acm-microcontroller-lab

**Callout:** none.

**Speaker notes:**

- No hedging. The cap is $1,000. The base order is $624.65. The max order, which adds backlog parts and a reserve, is $929.64. Both include tax and a shipping estimate.
- $150 is held back as a restock reserve until after lab day 2, to replace whatever the first two sessions actually break.
- Six station kits plus spares: eight boards for six tables.
- The code and wiring are public. CI compiles every sketch, so the starters and solutions are known to build. Do not quote a sketch count.

**Timing:** 13:11, Block 3, 12 min (money, 3 min).

---

### Slide 11: s11-decision

**Title:** Order today, or lab day 1 moves
**Eyebrow:** Build
**Pillar:** Build

**Screen copy, three lines:**

> Overseas vendor line: 7 to 14 working days
> Lab day 1: Sep 24
> After today: lab day 1 moves about two weeks, or the kit costs about $130 to $200 more from US vendors

**Callout (Warning):** Hands today are a count, not a binding vote. The spend needs advisor sign-off before anyone orders.

**Speaker notes:**

- State it as a fact. The vendor line is 7 to 14 working days. Lab day 1 is Sep 24. An order that does not go out today either moves lab day 1 or costs $130 to $200 more domestically.
- Ask for a show of hands. Record it as a count. It is a straw poll, and say so.
- Then say what actually happens next: advisor sign-off, a decision-log entry, and the order placed by [TBD: name the person with the card]. Say the name out loud or the decision evaporates on the way out.
- If the room is thin or the advisor is unreachable today, take the schedule hit on purpose: lab day 1 moves to Oct 8, the rest slides, and say when the decision gets made instead.
- Six minutes. Close it with one of the two lines above, not a maybe.

**Timing:** 13:11, Block 3, 12 min (decision, 6 min; ends 13:23).

---

### Slide 12: s12-seats

**Title:** Six seats, all open
**Eyebrow:** Connect
**Pillar:** Connect

**Screen copy, table:**

| RCC title | ACM title | What it costs per week |
|---|---|---|
| President | Chair | Runs the meeting, owns the semester plan |
| Vice President | Vice Chair | Events, Club Rush, backs up the Chair |
| Treasurer | Treasurer | The money, the ledger, the ACM annual report |
| Secretary | Secretary | Notes within 48 hours. Optional under ACM |
| ICC Representative | none | Mondays 9:30 AM, Bradshaw Center |
| Faculty Advisor | Faculty Sponsor | Room booking, spend supervision |

Ledger line, 32 px:

> Chair, Vice Chair, and Treasurer hold ACM Student Membership: $19 a year.

**Callout (Warning):** ICC Representative is every Monday at 9:30 AM. Three absences and the club loses its standing.

**Speaker notes:**

- Sixty seconds on why this matters: RCC requires at least seven fee-paid students including a President, a Treasurer, and an ICC Representative, plus a full-time faculty advisor. Below that the club is not recognized, and an unrecognized club cannot book this room or request funding.
- Two names for each job, one person holds both. Lead with the cost per week, not the title.
- Chair, Vice Chair, and Treasurer need ACM Student Membership. It is $19 a year. Say the number now; finding out later feels like a bait and switch.
- The ICC seat is a real Monday morning commitment and it is the one that quietly kills clubs. Someone whose Monday is already free is worth more than someone enthusiastic with a 9:35 class.
- Nobody has to run for anything today.

**Timing:** 13:23, Block 4, seats that are open, 12 min.

---

### Slide 13: s13-jobs

**Title:** Four more jobs
**Eyebrow:** Connect
**Pillar:** Connect

**Screen copy, table:**

| Job | What it costs |
|---|---|
| ICPC coach | Faculty or staff. Cannot be a contestant |
| Lab lead | Owns a lab day: setup, four stations, teardown |
| Warm-up lead | One 15-minute problem. Rotates |
| Repo admin 2 | Reviews pull requests on the docs repo |

**Callout (Note):** Warm-up lead is the best first task.

**Speaker notes:**

- These are not officer seats. They are the jobs that make the semester run.
- The ICPC coach has to be faculty or staff and cannot compete. If you know a professor who would, tell me.
- A lab lead owns one lab day end to end. A warm-up lead owns fifteen minutes, once.
- The docs repo needs a second admin who will review pull requests.

**Timing:** 13:23, Block 4, 12 min.

---

### Slide 14: s14-on-ramp

**Title:** The on-ramp
**Eyebrow:** Connect
**Pillar:** Connect

**Screen copy, numbered rungs:**

> 1. Run one 15-minute warm-up problem
> 2. Back up a lab day. Hand out kits
> 3. Take notes at one meeting
> 4. Then an officer seat

**Callout:** none.

**Speaker notes:**

- Nobody runs for office today. Each of these is a rung, in this order.
- One problem, one board, fifteen minutes. Then stand next to the person running a lab day and do nothing but hand out kits. Then take notes once. Then, and only then, a seat.
- The elections question, do not improvise it: "Seats are open. How they get filled, appointment now or an election in a few weeks, is a question for the advisor and I will have the answer in Discord by [TBD: date]." Then have it.
- If you get names today, they go on the interest sheet with a role, and nowhere else.

**Timing:** 13:23, Block 4, 12 min (ends 13:35).

---

### Slide 15: s15-questions

**Title:** Questions
**Eyebrow:** Fall 2026
**Pillar:** none

**Screen copy:**

> The sheet going around: name, email, what you are interested in.
> Officer seat, lab, ICPC, hackathon, just meetings.

**Callout (Note):** The sheet does not go online. Names are published only with written consent.

**Speaker notes:**

- Start the interest sheet at the top of this block, not the end. Half the room leaves at 1:48.
- Do I need to know how to code? No. T0 stations assume you have never written a line.
- How much time is this? One hour a week. Everything else is optional.
- Is there money for the hackathon trip? Not recorded yet. Say that rather than guessing.
- Is this the same as the GDG club? Different clubs, same room, GDG meets at 2:30 right after us. Plenty of people do both. Do not sell against it.
- What is ICPC? Three people, one computer, five hours, a set of problems. RCC hosts a site.

**Timing:** 13:35, Block 5, questions and sign-ups, 10 min.

---

### Slide 16: s16-ask

**Title:** Join the Discord
**Eyebrow:** Next Thursday, Sep 10
**Pillar:** none

**Screen copy:**

QR (Discord invite, generated inline, large), captioned:

> discord.gg/fM2HbsJyBG

Below the QR:

> Sep 10, same room, same time: ICPC. What the contest is, how teams form, how registration works.

Ledger line, 32 px, bottom:

> ACM @ RCC · instagram.com/rcc.acm

**Callout (Check):** Check: join before you leave the room. Everything else gets followed up there.

**Speaker notes:**

- One ask, not three. QR on the screen. Join before you leave the room.
- Next Thursday, same room, same time: ICPC. What the contest is, how teams form, how registration works. If you might want to compete, that is the one to be at.
- The lab decision in one sentence, with a name attached: either "the order goes out today after advisor sign-off, [TBD: name] places it" or "lab day 1 moves to Oct 8 and the decision gets made by [TBD: date]."
- Out by 1:50. The room turns over.

**Timing:** 13:45, Block 6, close: one ask, 5 min. Slide stays up until 13:50.

## 3. Real text requirement

"ACM @ RCC" appears as live text on slide 1 (the title) and slide 16 (the ledger line). The Discord invite discord.gg/fM2HbsJyBG is live text on slides 1 and 16, with an inline-generated QR on both. The Instagram handle rcc.acm is live text on slides 1 and 16 and is said aloud in the slide 6 notes, which is where the prep doc places the housekeeping line.

## 4. Do not say

The presenter does not invent any of these in the room. The answer for all of them is "not confirmed yet, it goes in Discord the day it is."

- Club Rush dates. Student Activities sets them. "Week of Sep 8" has no source in the repo; say "mid September" at most.
- The 2026-27 ICPC season calendar. Registration around Sep 1, rehearsal around Oct 25, regional around Nov 15 are 2025 figures. Check scl.na.icpc.global first.
- Cal Hacks 13.0 dates.
- The FY 2026-27 ASRCC allocation. $12,000 was requested. The outcome is not recorded anywhere.
- Who holds any officer seat. Chair, Vice Chair, Treasurer, and Faculty Advisor are all [TBD] on the roster.
- Whether a fall election is constitutionally required. Election month is [TBD] in elections.md.
- That the Aug 27 vote happened, or that any officer vote approved the lab. No notes exist for Aug 27. Never say "approved by officer vote."
- Quorum for a binding vote. It is [TBD] in the constitution.
- Whether the A-210 booking runs the full semester.
- The UC transfer filing window dates for 2027 entry. Oct 1 to Nov 30 is marked [confirm].
- A sketch count for CI. "Every sketch" is fine; "52" is unverified.
- The name of the person placing the order, unless it has been agreed before 13:11.
- The date the elections answer lands in Discord, unless it has been agreed with the advisor.