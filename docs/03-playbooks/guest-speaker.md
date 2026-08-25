# Playbook: Guest speaker

## Purpose

A guest speaker session is the Connect pillar in practice: an alum, a faculty member, or someone from industry talks to members about real work and takes questions. The FY 2026-27 funding request ([2026-spring/budget.md](../../semesters/2026-spring/budget.md)) describes an alumni network at Google, Amazon, and other tech companies; this playbook is how that network turns into a session in A-210.

## When

1 to 2 per semester. Default slot is the Thursday 12:50 to 1:50 PM meeting in BLCIS A-210. Start 6 weeks out; speakers with day jobs need lead time and often reschedule once.

## Owner

The Chair, or an officer the Chair assigns as host. The host is the speaker's single point of contact from invite to thank-you.

## Choosing a speaker

Sources, in order of how likely they say yes:

1. Alumni already in Discord or reachable through a current member
2. RCC faculty and staff (ask the advisor for names)
3. People members met at a hackathon or at the ICPC regional
4. Cold outreach through the advisor or the ACM chapter network

Ask for a talk that has something to do with what members are working on. "What I do at my job and how I got there" is fine. A product pitch is not.

## The invitation

Keep it short. Fill in the brackets; do not commit a filled-in copy with the speaker's contact details.

> Subject: Invitation to speak at the ACM student chapter, Riverside City College
>
> Hi [name],
>
> I am [role] of the ACM student chapter at Riverside City College. We meet Thursdays 12:50 to 1:50 PM and usually have [count] students, most of them working toward transfer in CS. Would you be open to a 30-minute talk plus Q&A on [topic] on one of these dates: [3 dates]?
>
> We can do in person in our room on campus or a video call on the projector. If you are open to it, let me know what topic you would rather cover, any A/V needs, and whether we may record.
>
> Thanks,
> [name], [role], ACM @ RCC

Attach or link the code of conduct: ACM's Policy Against Harassment applies to chapter events (see [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)).

## Money

ASRCC does not fund personnel, so do not promise an honorarium. Whether the club can pay for a speaker's travel, parking, or a meal from any source: [TBD: ask Student Activities before offering anything]. If ASRCC money covers anything at the event (food, swag), acknowledge ASRCC on the slides and out loud; see [asrcc-funding.md](../02-operations/asrcc-funding.md).

## T-minus checklist

### T-6 weeks

- [ ] Shortlist 3 speakers with a topic each; Chair picks the order
- [ ] Send the invitation with 3 candidate dates
- [ ] Event folder created with `scripts/new-event.sh`; event proposal issue if the session is bigger than a normal meeting ([event-proposal.yml](../../.github/ISSUE_TEMPLATE/event-proposal.yml))

### T-4 weeks

- [ ] Date confirmed with the speaker; format confirmed (in person or remote)
- [ ] If A-210 is too small or the time differs: advisor books a room in 25Live (at least 2 weeks before per the Club Advisor Guide); see [room-booking.md](../02-operations/room-booking.md)
- [ ] If food or an open-to-campus event: Student Activities Event Form; see [event-checklist.md](../02-operations/event-checklist.md)
- [ ] Ask the speaker for: title, 2-sentence bio, headshot (optional), A/V needs, recording permission (yes or no)
- [ ] Campus visitor parking and directions for an outside guest: [TBD: confirm the current process with the advisor]

### T-2 weeks

- [ ] Announce in Discord and Instagram using [templates/announcement.md](../../templates/announcement.md)
- [ ] Open a Discord thread to collect member questions ahead of time
- [ ] Remote speaker: send the meeting link and do a 10-minute test call

### T-1 week

- [ ] Confirm with the speaker: date, time, room, where the host will meet them, parking
- [ ] Pick 5 questions from the thread so Q&A does not start with silence
- [ ] Intro written (1 minute, from the bio)
- [ ] Ask the speaker whether a group photo is fine; members in the photo must also consent before it goes anywhere public

### T-1 day

- [ ] Reminder post
- [ ] Tech: laptop, adapter, clicker, the speaker's slides received or a backup plan
- [ ] Thank-you card or message drafted

## Day-of run sheet (60-minute slot)

| Time | Who | Action |
|---|---|---|
| 12:20 | Host | Meet the speaker at [TBD: agreed spot], walk to A-210 |
| 12:30 | Host | Tech check with the speaker's slides; water on the table |
| 12:50 | Note taker | Sign in; headcount |
| 12:53 | Host | Intro: who they are, why they are here, how Q&A works |
| 12:55 | Speaker | Talk, 25 to 30 minutes |
| 13:25 | Host | Q&A; start with a prepared question, then the room |
| 13:43 | Host | Thanks; one ask for members (connect on the speaker's preferred channel, next meeting) |
| 13:45 | Host | Group photo if agreed; walk the speaker out |
| 13:50 | Everyone | Room cleared |

Recording: only if the speaker said yes in writing. Announce at the start that it is being recorded. Where the recording lives (shared drive, not the repo) is up to the host; link it from the event folder.

## After

- [ ] Thank-you email to the speaker within 24 hours; include the headcount and one thing members took from it
- [ ] Headcount to the semester attendance record (see [attendance-tracking.md](../02-operations/attendance-tracking.md))
- [ ] Recording link (if any) and slides (if the speaker shares them) linked from the event folder
- [ ] `retro.md`: what the talk covered, what questions came up, would we invite them back
- [ ] Speaker's contact details go in the club's private contact list, never in this repo
- [ ] Ask the speaker if they know one other person who might come; that is next semester's shortlist
