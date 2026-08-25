# Playbook: Club Rush

## Purpose

Club Rush is the campus tabling event run by Student Activities where clubs recruit. It is where most of the semester's new members first hear of ACM @ RCC. The goal is simple: get people into Discord and to the first meeting after Rush.

## When

Early each semester. Student Activities sets the dates and the location. The RCC Club Rush page (https://www.rcc.edu/life-at-rcc/events/club-rush.html) last showed 2021 dates: three days in mid September on Terracina Drive next to the Quad. Fall 2026 dates: [TBD: confirm with Student Activities, studentactivities@rcc.edu]. Record the confirmed dates in the semester `calendar.md`.

The club has to be rechartered for the semester to table. The Club Packet is due to Student Activities within the first six weeks of the Fall semester per the RCC clubs page; see [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md) and get it in before Rush, not after.

## Owner

The outreach owner (an officer the Chair assigns). Every officer takes at least one table shift.

## What is on the table

| Item | Where it lives |
|---|---|
| QR code to the Discord | [assets/rcc-acm-qr-code.png](../../assets/rcc-acm-qr-code.png) or the dark version [assets/rcc-acm-qr-dark.png](../../assets/rcc-acm-qr-dark.png) |
| Sign-up form (name, RCC email, interests) | Outside the repo. Link and owner: [TBD: club shared drive] |
| Banner or tablecloth | [TBD: check the club's storage; brand rules in brand.md](../04-brand/brand.md) |
| A laptop showing the website or a demo | Website source: https://github.com/ACM-RCC/ACMWebsite |
| Printed one-pager: meeting time, room, Discord, Instagram | Make from [templates/announcement.md](../../templates/announcement.md) |
| Something to do at the table | A short coding puzzle on a whiteboard, or a demo from a past hackathon |

## The pitch (20 seconds)

Say it the same way every time so anyone on shift can deliver it:

> We are the ACM student chapter. We meet Thursdays 12:50 to 1:50 in BLCIS A-210. We build projects, go to hackathons like Cal Hacks, and RCC hosts the Southern California ICPC regional programming contest. Scan the QR for Discord; the first meeting is [date].

Then ask one question: "What are you into?" and match it to a pillar (Build, Compete, Learn, Connect).

## T-minus checklist

### T-4 weeks

- [ ] Confirm Rush dates, location, and how tables are assigned with Student Activities
- [ ] Confirm the recharter packet is submitted and the club is in good standing
- [ ] Set the date of the first meeting after Rush; put it on everything
- [ ] Event folder created with `scripts/new-event.sh`

### T-2 weeks

- [ ] Shift schedule: 2 people per hour for every hour the table is open; officers first, then volunteers from Discord
- [ ] Print QR codes (both versions) and the one-pager
- [ ] Sign-up form created and tested on a phone
- [ ] Banner and table items located
- [ ] Pitch script shared with everyone on shift

### T-1 week

- [ ] Discord announcement asking members to stop by and to bring a friend
- [ ] Instagram post with dates and table location (https://www.instagram.com/rcc.acm/)
- [ ] Welcome message drafted for new Discord joins (what channel to read first, when the meeting is)

### T-1 day

- [ ] Bag packed: QR prints, one-pagers, tape, pens, laptop and charger, banner, a portable battery
- [ ] Reminder to everyone on shift with the time and where to find the table

## Day-of run sheet

| Time | Who | Action |
|---|---|---|
| 30 min before open | First shift | Set up: banner, QR codes facing out, laptop demo running, sign-up form open on a phone |
| Open | On shift | Stand, do not sit. Pitch, ask what they are into, point at the QR |
| Each shift change | Outgoing shift | Hand over the sign-up count so far and the phone with the form |
| Close | Last shift | Pack everything; write the day's sign-up count in the event folder |

Rules on shift:

- One person talks, the other watches for people hovering and invites them over.
- Never ask for anything beyond name, RCC email, and interests. Student IDs and phone numbers stay off the form.
- If someone asks a question you cannot answer (funding, ICPC eligibility, hackathon travel), take their contact and have an officer reply in Discord.

## After

- [ ] Within 48 hours: send one message to everyone who signed up (Discord invite, first meeting date and room). Send from the club account, not a personal one
- [ ] Total sign-ups and Discord joins recorded in the event folder and `roster.md` as counts only
- [ ] The first meeting after Rush follows the [weekly meeting](weekly-meeting.md) playbook with the open-floor format; new people should leave knowing one person's name and one thing to come back for
- [ ] `retro.md`: sign-ups per shift, what people asked about, what to change
- [ ] Sign-up sheet stays in the shared drive; it never gets committed (see [privacy-and-public-repo-policy.md](../01-governance/privacy-and-public-repo-policy.md))
