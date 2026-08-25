# Playbook: ACM AI Hackathon

Runbook for the club's own on-campus hackathon. The brand assets exist (banner, icon, QR code in `assets/`). The first run's date and outcome are [TBD]; when they are known, they go in a semester event folder, not here.

## Purpose

- Give RCC students a hackathon they can reach without a flight: one building, one weekend or one long day, AI-themed projects.
- Produce projects and demos the club can show at Club Rush and in the ASRCC funding request.
- On-campus student engagement is ASRCC's top funding priority, so this event is the club's strongest funding case.

## When

- Pick a date at least 10 weeks out. Avoid the ICPC regional weekend (mid November in 2025), Thanksgiving week, and finals week. Exact dates for the current term are in `semesters/<YYYY-term>/calendar.md`, sourced from the RCCD academic calendar.
- Spring is easier for a first run: no clash with ICPC hosting, and the FY funding request (due late April) can carry the next one.
- First run date: [TBD].

## Decide the shape first

Write these decisions into the event plan and the decision log before booking anything.

| Decision | Options | Default |
| --- | --- | --- |
| Length | One day (8 to 10 hours) or overnight (24 to 36 hours) | One day for the first run. Overnight needs a room the college will keep open, plus a Campus Safety plan. |
| Theme | Open AI theme, or a fixed problem set | Open theme with 2 to 3 suggested tracks |
| Who can enter | RCC students only, or any college student | RCC students only for the first run; ASRCC funds RCC student engagement |
| Team size | 1 to 4 | Up to 4, matching the collegiate norm |
| MLH membership | Independent, or apply as an MLH Member Event | Independent for the first run. MLH requires at least 80 percent students, a public MLH Code of Conduct, overnight accommodations for off-campus attendees, and a finalized registration list the Wednesday before. |
| Judging | Officer panel, faculty and alumni panel, or peer vote | Faculty and alumni panel of 3; alumni network reaches Google and Amazon per the funding request |
| Prizes | Swag, gift cards, or trophies | [TBD]; confirm what ASRCC money may buy before promising anything |

## Owner roles

| Role | Who | Does |
| --- | --- | --- |
| Event lead | An officer | Owns this checklist and the go/no-go |
| Advisor | Faculty advisor ([TBD]) | 25Live request, Student Activities Event Form, must attend the event |
| Logistics lead | Officer or member | Room layout, power, Wi-Fi, signage, check-in |
| Food lead | Officer or member | Food Authorization form, order, dietary needs |
| Judging lead | Officer or member | Recruits judges, builds the rubric, runs demos |
| Comms lead | Officer or member | Discord, Instagram, faculty announcements, banner and QR placement |
| Treasurer | Treasurer | Budget, purchases, receipts, ASRCC acknowledgment |

## T-minus checklist

### T-10 weeks

- [ ] Fill in the shape table above. Log the go/no-go and the budget cap in the [decision log](../01-governance/decision-log.md).
- [ ] Create the event folder: `scripts/new-event.sh <semester> <YYYY-MM-DD> acm-ai-hackathon`. Fill in the [event plan](../../templates/event-plan.md).
- [ ] Advisor submits the 25Live request at least 2 weeks ahead (do it now; popular rooms go early). Tables and chairs must be in the original request. See [room booking](../02-operations/room-booking.md). Room: [TBD]; the regular meeting room BLCIS A-210 is the fallback for a small first run.
- [ ] Confirm funding: which ASRCC line item, or club funds. See [ASRCC funding](../02-operations/asrcc-funding.md).

### T-8 weeks

- [ ] Advisor files the Student Activities Event Form with the printed 25Live confirmation. Approval arrives in the second automated email, not the first.
- [ ] Draft the rules page (below). Publish the code of conduct link.
- [ ] Open registration (Google Form or the club website). Collect: name, RCC email, team status, dietary needs, laptop yes or no. Registration data stays in the club's drive, never in this repo.
- [ ] Recruit judges and 2 to 3 mentors. Ask alumni through the officers' contacts.

### T-6 weeks

- [ ] Comms: post the banner and QR code (`assets/acm-ai-hackathon-banner.png`, `assets/rcc-acm-qr-code.png`) in Discord and Instagram. Ask CIS faculty to announce in class.
- [ ] Sponsors or API credits: ask companies with alumni connections for credits or swag. Track asks and answers in the event folder.
- [ ] Draft the judging rubric: working demo, technical difficulty, use of AI, presentation. Weights: [TBD].

### T-4 weeks

- [ ] Food lead files the Food Authorization form and prices the order for the registered headcount plus 15 percent.
- [ ] Advisor contacts College Safety and Police about the event, building hours, and parking, especially for anything past normal hours.
- [ ] Logistics lead walks the room: outlets per table, extension cords needed, projector, Wi-Fi capacity, restrooms, where check-in goes.
- [ ] Second comms push. Registration cutoff announced.

### T-2 weeks

- [ ] Close registration or set a walk-in cap. Confirm the count with the food lead and the room capacity.
- [ ] Publish the schedule and rules to registrants.
- [ ] Build the submission form (project name, team, repo link, 2-minute demo video link, AI tools used).
- [ ] Judges and mentors confirmed with arrival times.
- [ ] Fill in the [run sheet](../../templates/event-run-sheet.md).

### T-1 week

- [ ] Volunteer shifts assigned: check-in, food, runners, judging timekeeper.
- [ ] Print signage, name tags, rubric sheets. Test the projector and the demo laptop.
- [ ] Buy supplies (extension cords, tape, markers). Treasurer keeps receipts.
- [ ] Final reminder post with what to bring: laptop, charger, student ID.

## Day-of run sheet

One-day version. Stretch the middle block for an overnight run.

| Time | Item | Owner |
| --- | --- | --- |
| Start minus 90 min | Setup: tables, power, signage, check-in table, projector test. | Logistics lead, volunteers |
| Minus 30 min | Check-in opens. Student ID checked against the registration list. Name tags. | Volunteers |
| 0:00 | Opening: welcome, theme, rules, schedule, code of conduct, ASRCC acknowledgment, where mentors sit. | Event lead |
| 0:20 | Team formation for solo registrants. Hacking starts. | Event lead |
| About 2:00 | Mentor rounds begin. Mentors circulate; teams flag questions in a Discord channel. | Judging lead |
| Midpoint | Lunch or dinner. Announce the submission form link and deadline. | Food lead |
| End minus 2 h | Submission reminder. Judges arrive, briefed on the rubric. | Judging lead |
| End minus 30 min | Submissions close. No edits after this. | Judging lead |
| End | Demos: 3 minutes per team plus 1 minute of questions. Timekeeper enforces it. | Judging lead |
| Demos plus 20 min | Judges deliberate. Group photo (consent asked out loud first). | Event lead |
| Demos plus 30 min | Awards. Thank sponsors, judges, ASRCC, the advisor. | Event lead |
| After awards | Teardown: room to its original layout, trash out, lost items to the event lead. | Everyone |

Attendance: count at check-in and again at demos. Record both counts in the retro. See [attendance tracking](../02-operations/attendance-tracking.md).

Incidents: tell the event lead or the advisor. Conduct issues follow the [code of conduct](../../CODE_OF_CONDUCT.md).

## Rules to publish

Keep these short and put them on the registration page. Modeled on the MLH standard rules, which are the norm at collegiate hackathons.

- Teams of up to 4. Everyone on the team participates.
- You may bring an idea from before the event. All code is written during the event. Public libraries and APIs are fine.
- AI tools are allowed if you say which ones you used in your submission.
- Submit by the deadline: repo link and a demo video of at most 2 minutes. Judges watch only the first 2 minutes.
- Code of conduct violations mean removal from the event and disqualification.
- Judges' decisions are final.

## After

- [ ] Same day: Treasurer collects receipts. Within 3 days: file reimbursements. See [reimbursements](../02-operations/reimbursements.md).
- [ ] Within 1 week: [retro](../../templates/event-retro.md) in the event folder. Record registrations, check-ins, teams submitted, spend versus budget, judge feedback, and what to change.
- [ ] Post winners and project links to Discord and Instagram, with the ASRCC acknowledgment. Photos of people only with consent.
- [ ] Add the outcome numbers to the next ASRCC funding request draft.
- [ ] Update this playbook for process changes only.

## Budget shape

No verified figures exist for this event yet. The FY 2026-27 ASRCC request totals $12,000 for the club; the share for this event is [TBD]. Fill in the first real numbers after the first run.

| Line item | How to estimate | Figure |
| --- | --- | --- |
| Food | Registered headcount plus 15 percent, times meals | [TBD] |
| Prizes | Confirm what ASRCC allows | [TBD] |
| Printing and signage | Rubrics, name tags, posters (banner file exists) | [TBD] |
| Supplies | Extension cords, tape, markers, whiteboard markers | [TBD] |
| Swag | Stickers or shirts; ASRCC "marketing" category | [TBD] |
| API credits | Usually donated; $0 if a sponsor covers it | [TBD] |
| Room, custodial, Safety | Ask the advisor whether the college charges for after-hours use | [TBD] |
| Contingency | 5 to 10 percent | [TBD] |

ASRCC does not fund fundraisers, personnel, instructional equipment, or things the college must provide. Do not put a room rental or a staff hourly line in the request without asking Student Activities first.

## Assets

- Banner: `assets/acm-ai-hackathon-banner.png`
- Icon: `assets/acm-ai-hackathon-icon.png`
- QR codes: `assets/rcc-acm-qr-code.png`, `assets/rcc-acm-qr-dark.png`
- Brand rules: [brand](../04-brand/brand.md)

## Links

- MLH standard hackathon rules: <https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md>
- MLH Member Event guidelines: <https://github.com/MLH/mlh-policies/blob/main/member-event-guidelines.md>
- MLH Code of Conduct: <https://github.com/MLH/mlh-policies/blob/main/code-of-conduct.md>
- Event checklist: [event-checklist](../02-operations/event-checklist.md); communications: [communications](../02-operations/communications.md)
- Templates: [event-plan](../../templates/event-plan.md), [event-run-sheet](../../templates/event-run-sheet.md), [event-retro](../../templates/event-retro.md), [funding-line-item](../../templates/funding-line-item.md)
- Playbook index: [README](README.md)
