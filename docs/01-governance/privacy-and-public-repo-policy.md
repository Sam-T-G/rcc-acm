# Privacy and public repo policy

This repo is public and its git history is permanent. Anything committed here can be read by anyone, indexed by search engines, and copied by anyone who clones it. This page says what may go in, what may not, and what to do when something slips through. It is rule 4 in [maintenance-rules.md](maintenance-rules.md).

The short version: the club's institutional memory belongs here; people's personal information does not.

## What may be committed

| Allowed | Example |
| --- | --- |
| Financial figures | "ASRCC request for FY 2026-27: $12,000"; a trip's lodging total; a workshop's supply cost |
| Attendance and membership as counts | "14 members attended"; "31 registered, 22 checked in" |
| Institutional contacts | `studentactivities@rcc.edu`, `ASRCC.ICC@rcc.edu`, a department office phone published on rcc.edu |
| Public club links | `https://discord.gg/fM2HbsJyBG`, `https://www.instagram.com/rcc.acm/`, `https://github.com/Sam-T-G/rcc-acm` |
| Officer roles without names | "Treasurer submitted the request on 2026-04-29" |
| Officer names, with that officer's consent | A name in MAINTAINERS.md after the person has agreed in writing (a message in Discord counts; save the date in `handoff.md`) |
| Names already published by the officer on a public ACM (Association for Computing Machinery) chapter or organizer page | Name and title only, with a link to that page |
| Meeting minutes with decisions and counts | "Voted 14 to 3 to run the workshop in week 6" |
| Logos and brand files | SVG or PNG under 1 MB in `assets/` |
| Room numbers and meeting times | BLCIS A-210, Thursdays, 12:50 to 1:50 PM |

## What may not be committed

| Not allowed | Why |
| --- | --- |
| Personal phone numbers | Permanent, searchable, and not the club's to publish |
| Personal email addresses (gmail, student email, any address that belongs to a person) | Same |
| Student ID numbers | Identity and account risk |
| Home addresses | Safety |
| Signatures, scanned or as images | Forgeable |
| Photos of people without written consent | The person did not agree to be in a public repo; a Discord photo post is not consent for GitHub |
| Rosters with names | Members did not sign up to be listed publicly. Counts only. |
| Bank, trust, or ASRCC account numbers | Fraud risk. The dollar amounts are fine; the account number is not. |
| Passwords, recovery codes, API keys, shared-login details | Anyone can read them. Use a club-controlled password manager (`[TBD]`) and share in person. |
| Exports from attendance or RSVP tools (CSV with names and emails) | Bulk personal data. Pull the counts into `roster.md` and delete the export. |
| Filled-out RCC or ASRCC forms as PDFs or images | They carry signatures, phone numbers, and student IDs. Transcribe the numbers into `budget.md` instead. |
| Links to private spreadsheets or form-response sheets | The link itself may grant access. Link the blank form, never the responses. |
| A person's name in a complaint, conduct report, or dispute | Handle through [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md), off the repo. |

When in doubt, leave it out and write `[TBD]` or a role instead. You can always add something later; you cannot cleanly take it back.

## Consent for names

An officer's name may appear in the repo only after the officer has agreed. The practical rule:

1. Ask in writing (Discord DM or email is fine). Say where the name will appear (MAINTAINERS.md, decision log "Who" column, a playbook byline).
2. Save the date of consent in the current semester's `handoff.md` under account and consent records. Do not commit the message itself.
3. Consent covers name and role. Anything more (photo, email, phone, LinkedIn) needs its own consent and is usually better left out anyway.
4. Consent can be withdrawn. If someone asks to be removed, follow the removal steps below. Do not argue about it.
5. An officer who has published their own name and title on a public ACM (Association for Computing Machinery) chapter or organizer page may be listed by name and title with a link to that page, since they have already published it. Anything beyond name and title still needs consent under this policy.

Members who are not officers are never named. Meeting notes say "14 members attended", not who.

## How to request removal

If you find your own information, or anyone's, in this repo:

1. Do not open a public issue quoting it. That puts it in a second place.
2. Contact a maintainer privately: a Discord DM to a current officer listed in [MAINTAINERS.md](../../MAINTAINERS.md), or email the advisor listed there.
3. Say which file and roughly where. You do not need to explain why.
4. A maintainer removes it within a few days and confirms to you when history has been rewritten.

## How maintainers remove data

Deleting the line in a new commit is not enough. The old commit is still in the repo's history, still viewable on GitHub, and still in every clone. Removal means rewriting history.

1. Remove the data from the current files and commit.
2. Rewrite history so the data never appears in any commit. GitHub's guide covers both tools and the GitHub-side cleanup: <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>. The recommended tool is git filter-repo: <https://github.com/newren/git-filter-repo>.
3. Force-push the rewritten history. Branch protection on `main` will block this; an admin lifts it for the push and turns it back on immediately after.
4. Ask GitHub Support to purge cached views of the old commits (the guide above explains how). Until then, direct links to the old commit SHAs still work.
5. Tell every collaborator to delete their local clone and re-clone. Old clones still hold the old history and a careless push would bring it back.
6. Check forks. Anyone who forked the repo before the rewrite still has the data. Ask them to delete or rebase the fork; you cannot force it.
7. Add a decision log row: date, "history rewritten to remove personal data", who did it. Do not describe the data.

Because a rewrite disrupts everyone, prevention matters more than cleanup. `scripts/check.sh` scans for phone and email patterns before every PR; run it.

## Financial records

Money is the exception to the "leave it out" instinct. The next team needs to know what a hackathon trip cost, what ASRCC granted, and what a workshop's supplies ran. Commit those figures in `semesters/<YYYY-term>/budget.md` and event `plan.md` and `retro.md` files. What stays out: account numbers, requisition form scans, receipts with a member's name and card digits (transcribe the amount and vendor instead).

## Photos and media

Photos of people go in the club's shared drive, not the repo, unless every identifiable person has consented in writing and the file is under 1 MB. Event posters, banners, and logos are fine in `assets/` if they contain no photographs of people. Link the drive folder from the event's `retro.md`.
