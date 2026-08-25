# Playbook: Hackathon trip

Runbook for taking a group of members to an off-campus collegiate hackathon (Cal Hacks and similar collegiate hackathons). Evergreen: the rules and the checklist live here; each actual trip gets its own folder under `semesters/<YYYY-term>/events/` with a plan, run sheet, and retro.

## Purpose

- Members compete as teams at a real hackathon, ship a project in 24 to 36 hours, and meet students and sponsors from other schools.
- The club covers as much of the cost as ASRCC and club funds allow, so the trip is not limited to members who can pay their own way.

## When

- Most large collegiate hackathons run in fall (October to November) and spring (March to April). Cal Hacks 12.0 was October 24 to 26, 2025. The Cal Hacks 13.0 sponsorship packet says Fall 2026, San Francisco, 36 hours; exact dates [TBD].
- Planning starts at least 8 weeks before the hackathon date. Applications close about 3 to 4 weeks before the event (Cal Hacks 12.0 regular deadline was October 1 for an October 24 start).
- Money from ASRCC takes weeks. If the trip depends on an ASRCC allocation, the request must be in the fiscal-year funding packet (due late April) or go to the ASRCC Senate starting in August. See [ASRCC funding](../02-operations/asrcc-funding.md).

## Owner roles

| Role | Who | Does |
| --- | --- | --- |
| Trip lead | An officer (Chair or Vice Chair by default) | Owns this checklist, the headcount, and the go/no-go decision |
| Treasurer | Treasurer | Budget, receipts, reimbursement paperwork, trust account contact |
| Housing lead | Any officer or trusted member | Books lodging, collects the per-person share, keeps the guest list |
| Transport lead | Any officer or trusted member | Flights or carpool plan, airport and venue transit |
| Advisor | Faculty advisor ([TBD]) | Signs anything RCC requires, is the emergency contact of record |

One person can hold two roles on a small trip. Nobody holds all of them.

## Hackathon rules the trip has to respect

These come from the Cal Hacks FAQ and the MLH policies. Confirm them against the current event page each year; hosts change details.

- Everyone must be accepted and confirmed by the event's deadlines. Cal Hacks: "only hackers who were accepted and confirmed by the deadlines will be allowed in the venue. We will not make exceptions." Do not book anything for a member who is not confirmed.
- Teams are up to 4 people (Cal Hacks). A "beginner" team means every member is a first-time hacker. Team matching exists at the event for people without a team.
- Everyone must be in person. Bring a school ID and a government ID, laptop and charger, headphones, a change of clothes, and toiletries.
- The venue has a quiet sleeping room and hotels within a 10-minute walk; meals, snacks, and drinks are provided. Members can skip lodging if they are willing to sleep at the venue.
- Travel is self-funded. Cal Hacks offers $100 travel stipends to first-year university students, first-come-first-serve; everyone else covers their own travel. A free bus runs from Montgomery BART to the venue.
- MLH rules: you may reuse a prior idea but not prior code; all team members must actively participate; AI tools are allowed if disclosed in the submission; a 2-minute demo video is required; stop when time is up.
- Code of conduct: the event's own code (Cal Hacks 12.0 on Devpost) plus the MLH Code of Conduct. MLH reporting for North America: +1 409 202 6060, <incidents@mlh.io>; reporters may stay anonymous. Our own [code of conduct](../../CODE_OF_CONDUCT.md) still applies to members on the trip. <!-- pii-ok: public MLH organizational hotline -->

## T-minus checklist

### T-8 weeks

- [ ] Pick the event. Confirm dates, location, application deadline, team size, and travel stipend rules from the event site.
- [ ] Run a Discord poll for interest. Get a rough headcount and who can drive.
- [ ] Create the event folder: `scripts/new-event.sh <semester> <YYYY-MM-DD> <slug>`. Fill in [event-plan](../../templates/event-plan.md).
- [ ] Draft the budget using the shape below. Decide what the club can cover (housing first; see funding notes).
- [ ] Log the go/no-go decision and the funding split in the [decision log](../01-governance/decision-log.md).

### T-6 weeks

- [ ] Every member applies to the hackathon individually. Post the deadline in Discord with two reminders.
- [ ] Ask the advisor what RCC requires for a student-organized trip (forms, waivers, insurance): [TBD]. Record the answer in `docs/02-operations/` once known.
- [ ] Open a flight or drive comparison. For the Bay Area, ONT to SFO was $180 per person in Fall 2025.

### T-4 weeks

- [ ] Acceptances arrive. Final headcount = accepted and confirmed members only.
- [ ] Book lodging for the confirmed headcount. Split into rooms; collect each person's share or confirm the club covers it.
- [ ] Book flights or lock the carpool list (drivers, seats, departure point). Cars need a driver with insurance and a backup driver.
- [ ] Publish the per-person cost and what the club covers. No surprises at the airport.

### T-2 weeks

- [ ] Every member confirms attendance on the hackathon platform by the host's confirmation deadline.
- [ ] Form teams of up to 4 in Discord. Unmatched members plan to use team matching at the venue.
- [ ] Collect emergency contacts (kept by the trip lead and advisor, never in this repo).
- [ ] Build the packing list post: both IDs, laptop, charger, headphones, clothes, toiletries, reusable water bottle.
- [ ] Fill in the [run sheet](../../templates/event-run-sheet.md) with departure times, meeting points, and the venue address.

### T-1 week

- [ ] Reconfirm flights, lodging, and cars. Share confirmations in a private officer channel.
- [ ] Post the run sheet in Discord. Pin it.
- [ ] Treasurer posts the receipts rule (below) and who to send receipts to.

## Day-of run sheet

### Departure day

| Time | Item | Owner |
| --- | --- | --- |
| [TBD] | Meet at departure point (airport or campus lot). Headcount against the confirmed list. | Trip lead |
| [TBD] | Flight or drive. Drivers share live location with the trip lead. | Transport lead |
| [TBD] | Arrive. Transit to lodging (Cal Hacks: free bus from Montgomery BART to the venue). | Transport lead |
| [TBD] | Check in to lodging. Room assignments as posted. | Housing lead |
| [TBD] | Hackathon check-in with both IDs. Opening ceremony. | Everyone |

### Hack day

- Trip lead does a headcount check in Discord at [TBD] morning and [TBD] evening.
- Anyone leaving the venue overnight tells the housing lead.
- Treasurer photographs every group receipt the same day.
- Incidents: tell the trip lead and the event organizers. MLH line if it is an MLH event.

### Return day

| Time | Item | Owner |
| --- | --- | --- |
| [TBD] | Submissions due (per event schedule). Demo video uploaded. | Teams |
| [TBD] | Judging and closing ceremony. | Everyone |
| [TBD] | Lodging checkout. Room sweep for chargers and IDs. | Housing lead |
| [TBD] | Transit to airport or cars. Headcount. | Trip lead |
| [TBD] | Arrive home. Trip lead posts "everyone is back" in Discord. | Trip lead |

## After

- [ ] Within 3 days: Treasurer collects all receipts and files reimbursements. See [reimbursements](../02-operations/reimbursements.md).
- [ ] Within 1 week: fill in the [retro](../../templates/event-retro.md) in the event folder. Record actual spend against the budget, per-person cost, what broke, and what to change.
- [ ] Post project links and photos (with consent) to Discord and Instagram. Acknowledge ASRCC if ASRCC money paid for any part of the trip.
- [ ] Update this playbook if a rule or cost changed. Dated numbers go in the semester folder, not here.

## Budget shape

Line items, in the order the money usually goes out. Figures in the right column are from the Cal Hacks 12.0 request and are the club's most recent real numbers.

| Line item | How to estimate | Cal Hacks 12.0 (Fall 2025) |
| --- | --- | --- |
| Flights | Per-person fare times confirmed headcount | $180 per person, $1,980 total (11 people, ONT to SFO) |
| Cars | Gas plus parking; 2 cars listed in the request, what they covered is [TBD] | included in ground transit below or [TBD] |
| Ground transit | Airport to lodging, lodging to venue, return | about $320 |
| Housing | Nightly rate times nights times rooms | $3,662.82 total; $110.99 per person per night; $332.98 per person for the weekend |
| Per diem | Rate per day per person; travel days at the lower rate | $69 per travel day, $92 per full day |
| Registration | Most collegiate hackathons are free | $0 |
| Contingency | 5 to 10 percent of the total | [TBD] |

## Worked example: Cal Hacks 12.0

October 24 to 26, 2025, Palace of Fine Arts, San Francisco. 11 members accepted. This is the cost model in the Cal Hacks 12.0 trip budget; whether the FY 2026-27 request reused it is [TBD]. The dated plan and retro live in [semesters/2025-fall](../../semesters/2025-fall/README.md).

### Group totals

| Item | Amount | Source |
| --- | --- | --- |
| Flights, ONT to SFO, 11 people at $180 | $1,980.00 | request |
| Ground transit | about $320.00 | request |
| Housing (AirBnB, whole group, weekend) | $3,662.82 | request |
| Per diem, 11 people at $230 each | $2,530.00 (estimate) | assumes 2 travel days at $69 and 1 full day at $92; the claimed split is [TBD] |
| Total | about $8,492.82 (estimate) | sum of the rows above; depends on the per diem assumption |

### Per person

| Item | Amount | Note |
| --- | --- | --- |
| Flight | $180.00 | request |
| Housing | $332.98 | request; $110.99 per night, which works out to three nights |
| Ground transit | about $29.09 | $320 split 11 ways |
| Per diem | $230.00 (estimate) | assumes $69 + $92 + $69; the claimed split is [TBD] |
| Total | about $772.07 (estimate) | depends on the per diem assumption |

### Where the money came from

| Source | Amount | Status at the time of the request |
| --- | --- | --- |
| ASRCC aid requested | $2,500 | requested [TBD: annual packet or Senate, and when]; outcome [TBD] |
| Old ACM trust account | about $1,063 | access problems, see below |
| Members, out of pocket | the remainder: about $4,930 total or about $448 per person (estimate, using the per diem assumption above) if both sources above came through in full | |

Housing was the members' stated first priority for club money. $2,500 of ASRCC aid covers about 68 percent of the $3,662.82 housing bill; add the trust account and the two sources together ($3,563) land about $100 short of the full housing bill.

## Funding notes: ASRCC and the trust account

- ASRCC funds come from the Student Services Fee Fund on a July 1 to June 30 fiscal year. The annual funding packet is due late April (April 29 in 2026), with 15-minute hearings in mid May and allocation notice by July 1. A fall trip has to be in the request the previous spring. The FY 2026-27 request asked for $12,000 total for the club; the share for travel is [TBD]. Details: [ASRCC funding](../02-operations/asrcc-funding.md).
- ASRCC gives funding priority to on-campus student engagement and does not fund fundraisers, personnel, instructional equipment, or things the college must provide. Frame a trip request around what members bring back (workshops, projects, recruiting), and expect travel to be a harder sell than an on-campus event.
- ASRCC must be acknowledged at anything it funds. Put "Supported by ASRCC" in the trip announcement and the retro post.
- The old ACM trust account held about $1,063 as of the Cal Hacks 12.0 planning in Fall 2025. The account is old enough that getting access is its own project. Treasurer's job: find out who the signers of record are, work with the Student Activities office and the advisor to update them, and log the result in the decision log. Never put the account number in this repo.
- Cal Hacks's own travel stipend is $100, first-year university students only, first-come-first-serve. Point eligible members at it; it does not change the club budget much.

## Receipts rule

Every reimbursement, from ASRCC or from a hackathon stipend, depends on receipts that show the price and the date of purchase. Photograph or save the PDF the day of purchase and send it to the Treasurer. Card statements are not receipts. Missing receipt means no reimbursement.

## Links

- Cal Hacks: <https://www.calhacks.io/>
- MLH Code of Conduct: <https://github.com/MLH/mlh-policies/blob/main/code-of-conduct.md>
- MLH standard hackathon rules: <https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md>
- Event checklist: [event-checklist](../02-operations/event-checklist.md)
- Templates: [event-plan](../../templates/event-plan.md), [event-run-sheet](../../templates/event-run-sheet.md), [event-retro](../../templates/event-retro.md), [funding-line-item](../../templates/funding-line-item.md)
- Playbook index: [README](README.md)
