# ACM @ RCC

![ACM AI Hackathon banner](assets/acm-ai-hackathon-banner.png)

The ACM Student Chapter at Riverside City College is a student-run community around computing education, problem solving, and competitive programming. We meet every week, host a site for the Southern California ICPC Regional Contest, travel to collegiate hackathons, and run our own ACM AI Hackathon. Four words cover what we do: Build, Compete, Learn, Connect.

This repo is the chapter's institutional memory. It holds the rules, the playbooks, and one folder per semester that every officer team copies and works through. It is not a code project. The website source lives in [ACM-RCC/ACMWebsite](https://github.com/ACM-RCC/ACMWebsite).

## Meet us

| | |
|---|---|
| When | Thursdays, 12:50 to 1:50 PM |
| Where | BLCIS A-210 |
| Discord (the real hub) | <https://discord.gg/fM2HbsJyBG> |
| Instagram | <https://www.instagram.com/rcc.acm/> |
| Current semester | [semesters/2026-fall/](semesters/2026-fall/) |
| All links | [docs/04-brand/links.md](docs/04-brand/links.md) |

## Where things live

| Path | What is in it |
|---|---|
| [docs/00-charter/](docs/00-charter/) | Mission, constitution (draft), officer roles, elections, membership |
| [docs/01-governance/](docs/01-governance/) | Maintenance rules, semester lifecycle, decision log, handoff procedure, privacy policy for this public repo |
| [docs/02-operations/](docs/02-operations/) | ASRCC funding, club recognition and ICC, room booking, reimbursements, event checklist, communications, attendance tracking |
| [docs/03-playbooks/](docs/03-playbooks/) | Step-by-step guides: weekly meeting, workshop, club rush, hackathon trip, ICPC regional site, ACM AI Hackathon, guest speaker |
| [docs/04-brand/](docs/04-brand/) | Brand rules and every public link |
| [docs/05-onboarding/](docs/05-onboarding/) | New member, new officer, repo tour |
| [templates/](templates/) | Blank forms: meeting notes, event plan, run sheet, retro, decision record, semester goals, handoff, funding line item, workshop outline, announcement |
| [semesters/](semesters/) | One folder per semester. Dated material only goes here |
| [scripts/](scripts/) | `new-semester.sh`, `new-event.sh`, `new-meeting.sh`, `check.sh` |
| [assets/](assets/) | Logos, banners, QR codes (each under 1 MB) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to change anything in this repo |
| [MAINTAINERS.md](MAINTAINERS.md) | Who holds admin rights and how that gets handed off |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | ACM Policy Against Harassment plus RCC reporting routes |

## Start here

### New member

1. Join the [Discord](https://discord.gg/fM2HbsJyBG). Announcements, problem sets, and ride shares happen there.
2. Show up Thursday, 12:50 PM, BLCIS A-210.
3. Read [docs/05-onboarding/new-member.md](docs/05-onboarding/new-member.md) (five minutes).
4. Look at the current semester's [calendar](semesters/2026-fall/calendar.md) and [goals](semesters/2026-fall/goals.md).
5. Want to compete? See the [ICPC playbook](docs/03-playbooks/icpc-regional-site.md) and the [hackathon trip playbook](docs/03-playbooks/hackathon-trip.md).

### New officer

1. Read [docs/05-onboarding/new-officer.md](docs/05-onboarding/new-officer.md), then [docs/05-onboarding/repo-tour.md](docs/05-onboarding/repo-tour.md).
2. Find your role in [docs/00-charter/officer-roles.md](docs/00-charter/officer-roles.md). It lists what you own, including which folders here.
3. Read the ten [maintenance rules](docs/01-governance/maintenance-rules.md). They are short. CI checks lint, links, and file size; reviewers check the rest.
4. Read the [handoff procedure](docs/01-governance/handoff-procedure.md) and the previous semester's `handoff.md`.
5. Know the money calendar: [docs/02-operations/asrcc-funding.md](docs/02-operations/asrcc-funding.md). Requests are due in late April; miss it and the club runs on nothing.
6. Get added to [MAINTAINERS.md](MAINTAINERS.md) if you are one of the two required repo admins.

### Advisor

1. [docs/02-operations/club-recognition-and-icc.md](docs/02-operations/club-recognition-and-icc.md): what RCC requires of the club and of you each semester.
2. [docs/02-operations/room-booking.md](docs/02-operations/room-booking.md): 25Live requests go through you, not students.
3. [docs/01-governance/handoff-procedure.md](docs/01-governance/handoff-procedure.md): you are the continuity when officers graduate.
4. [MAINTAINERS.md](MAINTAINERS.md): you are listed as the fallback contact for this repo.
5. The ACM side: the chapter's Faculty Sponsor holds financial supervision and must have an ACM Professional Membership. See [officer-roles.md](docs/00-charter/officer-roles.md).

## How this repo stays maintained

Evergreen material lives in `docs/`. Anything with a date, a person, or a semester lives in `semesters/<YYYY-term>/`. Templates are contracts. Unknowns are written as `[TBD]`, never guessed. Changes go through pull requests that pass lint and link checks. A semester is not closed until its retrospective and handoff are filled in and the next folder exists.

The full list, with the reasons behind each rule, is in [docs/01-governance/maintenance-rules.md](docs/01-governance/maintenance-rules.md). Run `scripts/check.sh` before opening a PR.

## License

Content is licensed [CC BY 4.0](LICENSE). Logos and trademarks belong to their owners; see [docs/04-brand/brand.md](docs/04-brand/brand.md).
