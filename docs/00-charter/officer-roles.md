# Officer roles

The chapter answers to two organizations with two naming schemes. RCC requires a President, Treasurer, and ICC Representative. ACM requires a Chair, Vice Chair, and Treasurer. Map them like this and let one person hold both titles.

| RCC title | ACM title | Required by |
|---|---|---|
| President | Chair | RCC and ACM |
| Vice President | Vice Chair | ACM |
| Treasurer | Treasurer | RCC and ACM |
| Secretary | Secretary | Neither (optional under ACM) |
| ICC Representative | (none) | RCC |
| Faculty Advisor | Faculty Sponsor | RCC and ACM |

Who currently holds each seat: `semesters/<term>/roster.md`, roles plus names only with consent. Never list names here.

## Requirements that apply to every officer

- Enrolled RCC student who has paid the Student Services Activity Fee.
- Chair, Vice Chair, and Treasurer must hold ACM Student Membership ($19 per year as of 2026-08-24, [membership options](https://www.acm.org/membership/membership-options)).
- Read [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md), the [maintenance rules](../01-governance/maintenance-rules.md), and the [handoff procedure](../01-governance/handoff-procedure.md).
- Have a GitHub account and be able to open a pull request here.

## Roles

### Chair (President)

Owns: the chapter's direction, the semester plan, and its obligations to ACM and RCC.

- Sets semester goals with the officers (`semesters/<term>/goals.md`).
- Runs weekly meetings or delegates the run.
- Signs off on event go/no-go decisions and logs them.
- Makes sure the ACM annual report and the RCC recharter packet get filed. Does not have to file them, but is accountable if they are not.
- Appoints the nominating committee before elections.
- Sets up financial audit procedures and plans the budget with the Treasurer (ACM expectation).
- Is one of the two required repo admins unless the officers decide otherwise.

Repo folders: `semesters/<term>/goals.md`, `semesters/<term>/retrospective.md`, `docs/00-charter/`, `docs/01-governance/decision-log.md`.

### Vice Chair (Vice President)

Owns: everything the Chair owns when the Chair is unavailable, plus events.

- Must be ready to act as Chair at any time (ACM expectation).
- Coordinates events: plans, run sheets, retros.
- Leads the hackathon trip and ICPC site logistics unless another officer is assigned.
- Runs Club Rush.

Repo folders: `semesters/<term>/events/`, `docs/03-playbooks/`, `templates/event-*.md`.

### Treasurer

Owns: the money and the records.

- Keeps the chapter's financial records and the ledger in `semesters/<term>/budget.md`.
- Prepares the ASRCC funding request each spring ([asrcc-funding.md](../02-operations/asrcc-funding.md)) and the requisitions that spend it.
- Handles reimbursements ([reimbursements.md](../02-operations/reimbursements.md)).
- Files the ACM annual report every fiscal year (July 1 to June 30). Missing it puts the chapter on probation; missing it twice de-charters the chapter.
- Keeps meeting minutes unless a Secretary is elected (ACM Chapter-in-a-Box wording).
- Knows who the trust account signers are and keeps that access alive across handoffs. The old trust account's access problems are the reason this line exists.

Repo folders: `semesters/<term>/budget.md`, `docs/02-operations/asrcc-funding.md`, `docs/02-operations/reimbursements.md`, `templates/funding-line-item.md`.

### Secretary (optional)

Owns: minutes, files, and officer records.

- Records meeting notes in `semesters/<term>/meetings/`.
- Updates the ACM Chapter Administrative Interface with new officers after an election.
- Keeps the chapter's files in this repo tidy: naming, links, `[TBD]` cleanup.
- Corresponds with ACM HQ on bylaw changes.

If no Secretary is elected, the Treasurer takes minutes and the Chair takes the rest.

Repo folders: `semesters/<term>/meetings/`, `templates/meeting-notes.md`, `docs/05-onboarding/`.

### ICC Representative

Owns: the chapter's seat at the Inter-Club Council and its good standing with ASRCC.

- Attends ICC meetings (Mondays, 9:30 AM, Bradshaw Center Hall of Fame, per the [ASRCC page](https://www.rcc.edu/life-at-rcc/student-government.html)). Three absences in a semester costs the club its good standing.
- Reports ICC news back at the next chapter meeting.
- Attends ICC budget training in early March.
- Cannot represent any other club at the same time.

Repo folders: `docs/02-operations/club-recognition-and-icc.md`, `semesters/<term>/calendar.md` (ICC dates).

### Communications lead (optional, appointed)

Owns: Discord, Instagram, and the website.

- Posts announcements using `templates/announcement.md`.
- Keeps Discord roles current ([attendance-tracking.md](../02-operations/attendance-tracking.md)).
- Coordinates website changes in [ACM-RCC/ACMWebsite](https://github.com/ACM-RCC/ACMWebsite).

Repo folders: `docs/02-operations/communications.md`, `docs/04-brand/`, `assets/`.

### Faculty Advisor (Faculty Sponsor)

Owns: continuity and supervision.

- Full-time RCC faculty, as RCC requires. Holds ACM Professional Membership, as ACM requires.
- Provides continuity from year to year as students graduate (ACM wording).
- Exercises financial supervision over chapter accounts.
- Submits 25Live facilities requests; students cannot ([room-booking.md](../02-operations/room-booking.md)).
- Attends chapter events as RCC requires.
- Attends advisor training in early March.
- Is the fallback contact in [MAINTAINERS.md](../../MAINTAINERS.md).

Repo folders: none owned. Reviews `semesters/<term>/handoff.md` at semester close.

## Sources

- ACM officer responsibilities: <https://www.acm.org/chapters/responsibilities-of-chapter-officers>
- ACM chapter requirements: <https://www.acm.org/chapters/students/how-to-start-a-student-chapter>
- RCC club requirements: <https://www.rcc.edu/life-at-rcc/clubs-and-organizations.html>
