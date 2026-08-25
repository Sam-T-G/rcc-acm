# Playbook: Weekly meeting

## Purpose

The weekly meeting is the club. It is where members show up, where new people decide whether to come back, and where the pillars (Build, Compete, Learn, Connect) turn into something you actually do for an hour. A regularly scheduled meeting is also a good-standing requirement with Student Activities (see [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md)).

## When

| | |
|---|---|
| Day and time | Thursdays, 12:50 to 1:50 PM |
| Room | BLCIS A-210 |
| Runs | Every week classes are in session |
| Skips | Campus holidays, finals week, and any week the semester calendar marks as off |

Check the current semester's `calendar.md` for holidays and finals before announcing (Fall 2026: [2026-fall/calendar.md](../../semesters/2026-fall/calendar.md)).

Whether the A-210 booking is on 25Live for the whole semester or needs renewing: [TBD: confirm with the advisor at the start of each term].

## Owner

Chair runs the meeting. Vice Chair runs it when the Chair is out; ACM expects the Vice Chair to be ready to step in at any time. One other person (any officer or member) takes notes and the headcount.

## Meeting formats

Rotate so the semester is not four months of the same thing. Pick the format a week ahead and say it in the announcement.

| Format | Pillar | What happens in the main block |
|---|---|---|
| Problem session | Compete | Pick 2 or 3 problems, solve in pairs, walk one solution on the board |
| Build session | Build | Work on a member project or a hackathon idea; short demos at the end |
| Mini-talk | Learn | A member or officer teaches one thing in 20 minutes, then hands-on |
| Open floor | Connect | Planning, project matching, hackathon team forming, guest visit |

Bigger sessions with setup, food, or a different room use the [workshop](workshop.md) or [guest speaker](guest-speaker.md) playbook instead.

## Default agenda (60 minutes)

| Time | Block | Notes |
|---|---|---|
| 12:50 | Doors, sign in | Headcount sheet or form at the door |
| 12:55 | Announcements | Upcoming events, deadlines, funding news; 5 minutes max |
| 13:00 | Main block | The format you picked; 40 minutes |
| 13:40 | Wrap | Next week's format, who is leading, one ask (join Discord, sign up for X) |
| 13:50 | Out | Clear the room on time |

## T-minus checklist

### T-7 days

- [ ] Pick the format and the person leading the main block
- [ ] Post the plan in Discord (https://discord.gg/fM2HbsJyBG)
- [ ] Confirm the room is still booked if anything changed (holiday week, campus event)

### T-2 days

- [ ] Slides, problem set, or repo link ready and tested
- [ ] Create the notes file: `scripts/new-meeting.sh` makes `semesters/<term>/meetings/YYYY-MM-DD.md` from [templates/meeting-notes.md](../../templates/meeting-notes.md)
- [ ] Fill in the agenda in that file

### T-1 day

- [ ] Reminder in Discord; Instagram story if someone has time (https://www.instagram.com/rcc.acm/)

### Day of, T-15 minutes

- [ ] Arrive early; open the room
- [ ] Projector on, laptop connected, adapter works
- [ ] Sign-in sheet or form open
- [ ] Discord link and any repo links posted in the channel so people can copy them

## Day-of run sheet

| Time | Who | Action |
|---|---|---|
| 12:35 | Chair | In the room, tech check |
| 12:50 | Note taker | Start headcount; greet new faces and point them at Discord |
| 12:55 | Chair | Announcements from the notes file |
| 13:00 | Block lead | Main block |
| 13:40 | Chair | Wrap: next week, one ask |
| 13:50 | Everyone | Room cleared, chairs back, projector off |

If the projector fails: run from a laptop screen for a problem session, or switch to open floor. Do not spend 15 minutes on HDMI.

## After

- [ ] Notes filed in `semesters/<term>/meetings/YYYY-MM-DD.md` within 24 hours: what happened, headcount, decisions, action items
- [ ] Any binding decision copied into the [decision log](../01-governance/decision-log.md)
- [ ] Headcount added to the semester attendance record (see [attendance-tracking.md](../02-operations/attendance-tracking.md)); counts only, no names
- [ ] Action items pinged in Discord with an owner
- [ ] New members pointed at [new-member.md](../05-onboarding/new-member.md)

## Rules of thumb

- Announcements are 5 minutes. If they run long, the meeting has become a status update and people stop coming.
- Every meeting ends with one concrete ask.
- Never cancel silently. If the meeting is off, say so in Discord by Wednesday.
- Officer names and member names stay out of the notes unless the person has consented (see [privacy-and-public-repo-policy.md](../01-governance/privacy-and-public-repo-policy.md)). Use roles.
