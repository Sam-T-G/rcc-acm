# Attendance tracking

Why we count: ASRCC asks for an active member count in every funding request (22 as of Spring 2026), ACM asks for a member census and meetings held in the annual report, and the ICC representative's attendance decides the club's good standing. Counts are the evidence. Names are not, and names never go in this repo.

## Two systems

| System | What it tracks | Owner |
|---|---|---|
| Discord roles | Who is in the community and which cohort they joined in | Communications lead (or Chair) |
| Sign-in sheet or form at meetings and events | Who was physically there | Whoever runs the meeting |

Sign-in method: [TBD: paper sheet or a form]. Pick one and write it here. Either way, the sheet or form results stay with the advisor or in the club's private drive, not in this repo.

## Discord roles

- `Member`: anyone who joined the server and reacted to the rules post [TBD: confirm the server's onboarding flow].
- `Officer`: current officers only. Remove at handoff.
- Cohort role per semester, for example `Fall 2026`: assigned to people who signed in at least once that semester. Makes "active this semester" a one-click filter.
- `ICPC 2026`, `Cal Hacks 2025`, and similar: per-contest or per-trip roles. Handy for pinging teams and for counting travelers in the retro.

At semester close, count members per role and put the numbers in `semesters/<term>/retrospective.md`. Prune stale roles; do not delete members.

## Sign-in at meetings

1. Open the sheet or form before the meeting starts.
2. Ask everyone to sign in during the first ten minutes. Repeat once mid-meeting.
3. After the meeting, record the count (not the names) in the meeting notes: `semesters/<term>/meetings/YYYY-MM-DD.md`, using [templates/meeting-notes.md](../../templates/meeting-notes.md).
4. Assign the semester cohort role to first-timers in Discord.

## Sign-in at events

Same as meetings, plus:

- Funded events: keep the count with the event retro, because ASRCC and the funding request will ask. Write it in `semesters/<term>/events/<date>-<slug>/retro.md`.
- Trips: the roster of who traveled is a private file with the advisor. The repo records the count and the per-person costs, as in the Cal Hacks 12.0 folder under `semesters/2025-fall/`.
- ICPC site: the contest registers teams itself; the chapter records how many RCC teams competed and how many volunteers staffed the site.

## What goes in the repo

| Goes in | Stays out |
|---|---|
| Count per meeting, per event, per semester | Names on a sign-in sheet |
| Discord member and role counts | Discord usernames tied to attendance |
| "11 members accepted to Cal Hacks 12.0" | Who the 11 were |
| Count of active members for the funding request | Student IDs, emails, phone numbers |

Full rules: [../01-governance/privacy-and-public-repo-policy.md](../01-governance/privacy-and-public-repo-policy.md).

## Definitions

- Active member: [TBD: see membership.md]. Whatever the definition, compute it from the sign-in data plus the cohort role, and state which measure the retrospective uses.
- Meeting attendance: signed-in count, not Discord online count.

## Semester close checklist

- [ ] Total meetings held and average attendance in `retrospective.md`
- [ ] Each event's attendance in its retro
- [ ] Active member count, with the definition used
- [ ] Discord member count and cohort role count
- [ ] Sign-in sheets or form exports handed to the advisor, then removed from any shared officer drive that graduating officers still hold
- [ ] `Officer` role updated for the incoming team
