# New officer checklist

You were elected or appointed. This page gets you working in the first two weeks. Start with the "every officer" list, then your role. Role definitions are in [officer-roles.md](../00-charter/officer-roles.md); this page is the to-do version.

RCC requires every chartered club to have a President, a Treasurer, and an ICC Representative, plus a full-time faculty advisor. Other roles are set by the club's [constitution](../00-charter/constitution.md).

## Every officer, week one

- [ ] Read [maintenance-rules.md](../01-governance/maintenance-rules.md). It is the one page that explains how this repo stays trustworthy.
- [ ] Read the previous semester's `retrospective.md` and `handoff.md` under `semesters/`. That is your inheritance.
- [ ] Read this semester's `goals.md` and `calendar.md`. If they are empty, opening them is your first job (see [semester-lifecycle.md](../01-governance/semester-lifecycle.md)).
- [ ] Get a GitHub account if you do not have one, and ask a maintainer in [MAINTAINERS.md](../../MAINTAINERS.md) to add you as a collaborator.
- [ ] Take the [repo tour](repo-tour.md) (ten minutes).
- [ ] Decide whether your name may appear in the repo, and tell the maintainer in writing. See [privacy-and-public-repo-policy.md](../01-governance/privacy-and-public-repo-policy.md).
- [ ] Get an officer role in Discord from the president.
- [ ] Read the [code of conduct](../../CODE_OF_CONDUCT.md) again, this time as the person people will report to.
- [ ] Confirm the recharter registration for this semester lists you, if your role is on it (president, treasurer, ICC rep). See [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md).

## Every officer, every week

- [ ] Attend the weekly meeting (Thursdays, 12:50 to 1:50 PM, BLCIS A-210) or say in Discord that you cannot.
- [ ] Anything you decide that binds the club goes in the [decision log](../01-governance/decision-log.md).
- [ ] Anything you learn that is not written down: write it down. Evergreen facts go in `docs/`; dated ones go in the semester folder.

## President

- [ ] You own the semester lifecycle. Run `scripts/new-semester.sh` if nobody has, and fill `goals.md` with the team.
- [ ] Confirm the advisor is still the advisor and knows the meeting time and room.
- [ ] Confirm [MAINTAINERS.md](../../MAINTAINERS.md) lists two admins, one not graduating this year. If not, fix it this week.
- [ ] Hold Discord server ownership, or know who does.
- [ ] Know the recharter deadline (RCC publishes it as the first six weeks of the semester; confirm each term) and who is submitting the packet.
- [ ] Skim every playbook in [03-playbooks](../03-playbooks/README.md) so you know what the club already knows how to run.

## Treasurer

- [ ] Read [asrcc-funding.md](../02-operations/asrcc-funding.md) and [reimbursements.md](../02-operations/reimbursements.md) in full.
- [ ] Open this semester's `budget.md`. Every line needs requested, granted, and spent; start with what was granted for this fiscal year (July 1 to June 30).
- [ ] Find out who is authorized on the club's ASRCC trust account and whether you need to be added. Record the answer in `handoff.md` for the semester, never the account number.
- [ ] Put the ASRCC funding cycle in `calendar.md`: packets early February, request due late April, hearings mid May, allocation notice by July 1.
- [ ] If ACM (Association for Computing Machinery) requires any financial or activity report from the chapter, find the deadline and put it in `calendar.md`. Details: [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md).
- [ ] Keep receipts. Transcribe amounts into the repo; the receipt images go in the shared drive.

## ICC representative

- [ ] Find the ICC meeting time and place in [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md) and put every meeting in your own calendar. Three absences in a semester costs the club its good standing.
- [ ] Confirm you are on file with Student Activities as the club's representative.
- [ ] After each ICC meeting, post anything that affects the club (deadlines, event rules, funding news) in Discord and add dates to `calendar.md`.
- [ ] Attend ICC budget training when it is offered (early March in past years).

## Secretary (or whoever keeps notes)

- [ ] Run `scripts/new-meeting.sh` before each meeting and fill the note the same day. Counts and decisions, not names of attendees.
- [ ] Watch for decisions that belong in the [decision log](../01-governance/decision-log.md) and add them.
- [ ] Keep `roster.md` for the semester current as counts.
- [ ] Track attendance the way [attendance-tracking.md](../02-operations/attendance-tracking.md) says.

## Outreach or communications lead

- [ ] Get Instagram access and confirm the recovery email and phone are club-controlled, not a graduated officer's personal phone.
- [ ] Read [communications.md](../02-operations/communications.md) and [brand.md](../04-brand/brand.md). Use the club's name and logo the way the brand doc says.
- [ ] Use [templates/announcement.md](../../templates/announcement.md) for anything that goes out in more than one place.
- [ ] Own Club Rush prep with [club-rush.md](../03-playbooks/club-rush.md).

## Event lead (any officer running an event)

- [ ] Run `scripts/new-event.sh` to create the event folder with plan, run sheet, and retro.
- [ ] Follow [event-checklist.md](../02-operations/event-checklist.md). Room requests go through the advisor with at least two weeks' notice; students cannot submit them.
- [ ] Fill `retro.md` within a week of the event. Attendance as counts.

## Repo admin

- [ ] Read [handoff-procedure.md](../01-governance/handoff-procedure.md), especially the GitHub section on what "admin" means while the repo is under a personal account.
- [ ] Make sure branch protection on `main` is on: require a PR, one review, and the `markdownlint` and `links` checks.
- [ ] Add yourself to `.github/CODEOWNERS` where maintainers are listed.
- [ ] Run `scripts/check.sh` on a clean checkout so you know what it reports.
- [ ] Know how to remove personal data from history before you need to: [privacy-and-public-repo-policy.md](../01-governance/privacy-and-public-repo-policy.md).

## Advisor

- [ ] You are the fallback contact in [MAINTAINERS.md](../../MAINTAINERS.md). Confirm the entry is right.
- [ ] Room requests go through you in 25Live; see [room-booking.md](../02-operations/room-booking.md) for the lead time and paperwork.
- [ ] Advisor training happens in early March; new advisors attend.
- [ ] You do not need to use GitHub day to day. If the officer team disappears, the handoff procedure explains how the next team recovers accounts through you.
