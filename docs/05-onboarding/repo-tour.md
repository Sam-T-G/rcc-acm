# Repo tour

A walk through <https://github.com/Sam-T-G/rcc-acm> from the top of the tree to the bottom. Ten minutes. The one idea to hold onto: `docs/` is evergreen and `semesters/` is dated. Everything else exists to keep those two honest.

## Top level

| File | What it is for |
| --- | --- |
| [README.md](../../README.md) | The front door. What the club is, where things live, and a start-here list for members, officers, and the advisor. |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | How to change anything: naming, PR rules, what never goes in the repo. |
| [MAINTAINERS.md](../../MAINTAINERS.md) | Who administers the repo, by role. At least two admins at all times, plus the advisor as fallback. |
| [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) | Conduct expectations for meetings, events, and online spaces, and where to report. |
| [LICENSE](../../LICENSE) | CC BY 4.0. Anyone can reuse the club's docs with credit. |
| `.editorconfig`, `.gitignore`, `.gitattributes` | Editor and git settings so files look the same on every machine. You will not need to touch them. |
| `.markdownlint.yml`, `lychee.toml` | Config for the lint and link checks that run on every PR. |

## `.github/`

| Path | What it is for |
| --- | --- |
| `CODEOWNERS` | Which maintainers must review changes to charter, governance, templates, and workflows. |
| `PULL_REQUEST_TEMPLATE.md` | The checklist every PR starts with: one topic, checks green, decision logged if needed, no personal data. |
| `ISSUE_TEMPLATE/` | Forms for proposing an event, a workshop, a task, or a decision. Use these instead of a blank issue. |
| `workflows/docs-check.yml` | CI. Runs markdownlint and an offline relative-link check on every PR and push. |

## `docs/`

Evergreen material only. If it would be wrong next semester, it does not belong here. Index at [docs/README.md](../README.md).

| Folder | Read it when |
| --- | --- |
| [00-charter](../00-charter/mission.md) | You want to know what the club is, how officers are chosen, and what membership means. |
| [01-governance](../01-governance/maintenance-rules.md) | You are about to change the repo, close a semester, hand off, or wonder whether something may be committed. |
| [02-operations](../02-operations/asrcc-funding.md) | You need money, a room, recognition, or to run an event at RCC. |
| [03-playbooks](../03-playbooks/README.md) | You are running something the club has run before. Start from the playbook, not from scratch. |
| [04-brand](../04-brand/brand.md) | You are making a flyer, a post, or a slide, or need the club's public links. |
| [05-onboarding](new-member.md) | You are new. You are here. |

## `assets/`

Logos and brand files, SVG or PNG, each under 1 MB. Nothing with people's faces. Photos and large media live in the shared drive and get linked.

## `templates/`

Blank files that the scripts copy from. Meeting notes, event plan, run sheet, retro, decision record, semester goals, officer handoff, funding line item, workshop outline, announcement. Changing a template changes every future copy, so it needs a [decision log](../01-governance/decision-log.md) entry (rule 3).

Start with [templates/meeting-notes.md](../../templates/meeting-notes.md) to see the shape.

## `semesters/`

One folder per term, named `YYYY-term` (`2026-fall`, `2027-spring`). Each is a copy of `_template/` filled in over the term. [semesters/README.md](../../semesters/README.md) explains the open, run, close cycle.

Inside a semester folder:

| File or folder | What goes there |
| --- | --- |
| `README.md` | The open, run, close checklist for this term; tick it as you go. Scripts add rows to `calendar.md` and to `semesters/README.md`, not here. |
| `goals.md` | What the team set out to do, seeded from the previous handoff. |
| `calendar.md` | Every date that matters this term: RCC holidays, Club Rush, deadlines, events. `scripts/new-event.sh` adds a row here for each event folder. |
| `budget.md` | Requested, granted, spent, per line item. |
| `roster.md` | Member counts. Counts only; names never. |
| `meetings/` | One note per weekly meeting, `YYYY-MM-DD.md`. |
| `events/` | One folder per event, `YYYY-MM-DD-slug/`, with plan, run sheet, and retro. |
| `projects/` | Anything members are building together this term. |
| `retrospective.md` | Filled at the end: what happened vs the goals. |
| `handoff.md` | Filled at the end: what the next team must know. |

The current semester is the highest-numbered folder. As of this repo's creation that is [2026-fall](../../semesters/2026-fall/README.md).

## `scripts/`

Four shell scripts. Run them from the repo root.

| Script | Does |
| --- | --- |
| `new-semester.sh` | Copies `_template/` to `semesters/YYYY-term/`, fills in the semester name, adds a row to the semesters index. |
| `new-event.sh` | Creates `semesters/<sem>/events/YYYY-MM-DD-slug/` with plan, run sheet, and retro. |
| `new-meeting.sh` | Creates `semesters/<sem>/meetings/YYYY-MM-DD.md`. |
| `check.sh` | Pre-PR check: leftover placeholders and semester literals, personal-data patterns, em dashes, broken relative links, files over 1 MB, leftover template fill markers, and markdownlint if installed. It also counts open `[TBD]` markers without failing on them. Run it before every PR. |

## How a change flows

1. You edit a file on a branch (or use a script to create one).
2. You run `scripts/check.sh`.
3. You open a PR. The template asks the questions the rules care about.
4. CI runs lint and link checks. Any officer reviews. A maintainer reviews if CODEOWNERS says so.
5. Merge. Nothing goes to `main` any other way.

That is the whole repo. If something here does not match what you see in the tree, the tree is right and this page needs a PR.
