# Contributing to ACM @ RCC docs

This repo is the club's memory. Anyone in the club can propose a change. Officers review and merge. Nothing here is code; it is Markdown, and the bar for a good change is "the next officer team can find it and trust it."

## Before you start

- Read [docs/01-governance/maintenance-rules.md](docs/01-governance/maintenance-rules.md). The table below is the short version.
- Not sure where something goes? Read [docs/05-onboarding/repo-tour.md](docs/05-onboarding/repo-tour.md).
- Quick question? Ask on Discord (https://discord.gg/fM2HbsJyBG) before opening an issue. Issues are for work that changes the repo.

## The ten rules, short version

| # | Rule | What it means when you edit |
| --- | --- | --- |
| 1 | Evergreen vs dated | `docs/` holds material that stays true year to year. Anything tied to a date, a person, or a semester goes under `semesters/<YYYY-term>/`. If an evergreen doc needs an example, link into a semester folder. |
| 2 | Naming | Folders and files are kebab-case. Dates are `YYYY-MM-DD`. Semester folders are `YYYY-term` (`2026-fall`). Event folders are `YYYY-MM-DD-slug`. |
| 3 | Templates are contracts | Changing `templates/` or `semesters/_template/` needs a decision record in [docs/01-governance/decision-log.md](docs/01-governance/decision-log.md). If a copy is wrong because the template is wrong, fix the template, not the copy. |
| 4 | Privacy | Personal phone numbers, personal emails, student IDs, home addresses, signatures, and photos of people without written consent never go in. Rosters are counts only. Officer names appear only with that officer's consent. Dollar figures are fine; bank and trust account numbers are not. |
| 5 | Decisions are logged | Any binding choice (budget, policy, event go/no-go, template change) gets a one-paragraph entry in the decision log with the date and who decided. |
| 6 | Semester close is required | A semester is done when `retrospective.md` and `handoff.md` are filled in and the next semester folder exists. Outgoing team opens the PR; incoming team reviews and merges. |
| 7 | Two admins minimum | [MAINTAINERS.md](MAINTAINERS.md) lists at least two repo admins, one of whom is not graduating this year. The advisor is the fallback contact. |
| 8 | PRs, not direct pushes, to `main` | Every change to `main` goes through a pull request. One topic per PR. Any officer can review. Lint and link checks must pass. |
| 9 | Unknowns are marked `[TBD]` | Write `[TBD]` when you do not know. Never guess a date, a name, a room, or a dollar amount. |
| 10 | Small files, plain Markdown | No binaries over 1 MB; large media lives in the club's shared drive and is linked from here. |

## What goes where

| You want to add | Put it in | Start from |
| --- | --- | --- |
| A rule, procedure, or how-to that will still be true next year | `docs/<section>/` | The nearest existing doc |
| Meeting notes | `semesters/<term>/meetings/YYYY-MM-DD.md` | `scripts/new-meeting.sh` |
| An event plan, run sheet, or retro | `semesters/<term>/events/YYYY-MM-DD-slug/` | `scripts/new-event.sh` |
| Semester goals, calendar, budget, roster counts | `semesters/<term>/` | Already created by `scripts/new-semester.sh` |
| A binding decision | `docs/01-governance/decision-log.md` | `templates/decision-record.md` |
| A reusable playbook (how we run X every time) | `docs/03-playbooks/` | `docs/03-playbooks/README.md` |
| A logo or brand file under 1 MB | `assets/` | `docs/04-brand/brand.md` |
| A new fill-in form for future semesters | `templates/` | Needs a decision record first (rule 3) |

## Naming

- Files and folders: lowercase kebab-case. `room-booking.md`, not `Room Booking.md`.
- Dates: ISO, `2026-10-15`. Never `10/15/26`.
- Semester folders: `2026-fall`, `2027-spring`, `2027-summer`.
- Event folders: `2026-10-15-guest-speaker`.
- Branches: `<area>/<short-slug>`. Examples: `docs/room-booking`, `sem/2026-fall-budget`, `event/2026-10-15-guest-speaker`, `fix/broken-links`.
- Commit messages: one line, imperative, under 72 characters, says what changed. `Add 25Live lead time to room-booking.md`.
- PR title: same style as a commit message. If the PR closes an issue, write `Closes #NN` in the description.

## PR flow

1. Optional: open an issue with one of the forms (event proposal, workshop proposal, task, decision). Use it when other people need to weigh in before you write.
2. Create a branch from `main`. Direct pushes to `main` are blocked.
3. Make one topic of change. A budget update and a playbook rewrite are two PRs.
4. Run `scripts/check.sh`. Pre-PR check: leftover placeholders and semester literals, personal-data patterns, em dashes, broken relative links, files over 1 MB, leftover template fill markers, and markdownlint if installed. It also counts open `[TBD]` markers without failing on them.
5. Open the PR. Fill in the template; it is a checklist, not a form letter.
6. Any officer reviews. CI runs `markdownlint` and `links` and both must be green.
7. The reviewer merges (squash) and deletes the branch. You do not merge your own PR.

Special cases:

- Template change: link the decision record in the PR. No record, no merge.
- Semester close: the outgoing team opens it, the incoming team reviews and merges it. See [docs/01-governance/semester-lifecycle.md](docs/01-governance/semester-lifecycle.md).
- Anything that names a person: confirm consent is on file before you request review. See [docs/01-governance/privacy-and-public-repo-policy.md](docs/01-governance/privacy-and-public-repo-policy.md).

## What never goes in this repo

This repo is public. Assume every commit is visible to everyone forever, including after deletion.

- Personal phone numbers, personal email addresses, home addresses
- Student ID numbers, signatures, scans of forms with any of the above
- Photos of people without written consent
- Full rosters or attendee exports (counts only; the export stays in the shared drive)
- Bank, trust account, or card numbers; passwords; API keys; shared-account logins
- Files over 1 MB (link to the shared drive instead)

If something slipped in, do not just delete it in a new commit. Open an issue tagged `privacy` and ping a repo admin; the history needs rewriting.

## Writing style

- Short sections, checklists, tables. Write for a member reading this at 11 PM before a meeting.
- No em dashes inside sentences. Use periods, colons, semicolons, parens, or "and".
- Plain words. Say "use", not "utilize".
- Mark unknowns `[TBD]`. A `[TBD]` is honest; a guess is a trap for the next team.

## Local tools (optional)

CI runs these for you, but running them locally saves a round trip.

| Tool | Install | Run |
| --- | --- | --- |
| markdownlint-cli2 | `npm install -g markdownlint-cli2` | `markdownlint-cli2 "**/*.md"` |
| lychee | see <https://github.com/lycheeverse/lychee> | `lychee --offline './**/*.md'` (relative links only) or `lychee './**/*.md'` (external too) |
| check.sh | none (bash) | `scripts/check.sh` |

Config lives in `.markdownlint.yml` and `lychee.toml` at the repo root.
