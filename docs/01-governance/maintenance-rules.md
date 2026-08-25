# Maintenance rules

These ten rules are what keep this repo useful after the people who built it graduate. Every one of them exists because a club has lost something without it: a doc nobody could tell was stale, a template edited in five copies, an account with one owner who left, a phone number in a public commit.

This file is the canonical statement of the rules. [CONTRIBUTING.md](../../CONTRIBUTING.md), [`scripts/check.sh`](../../scripts/check.sh), and the [docs-check workflow](../../.github/workflows/docs-check.yml) implement them; if they ever disagree with this page, this page wins and the other one gets fixed.

Quick reference:

| # | Rule | Enforced by |
| --- | --- | --- |
| 1 | Evergreen in `docs/`, dated in `semesters/` | PR review |
| 2 | kebab-case names, ISO dates, `YYYY-term` and `YYYY-MM-DD-slug` folders | Scripts create the right names; review catches the rest |
| 3 | Templates change only with a decision log entry | CODEOWNERS review on `templates/` and `semesters/_template/` |
| 4 | No personal data in a public repo | `check.sh` PII patterns; review |
| 5 | Binding decisions are logged | PR template checkbox; review |
| 6 | A semester is not closed until retro, handoff, and next folder exist | Handoff PR review by the incoming team |
| 7 | Two repo admins at all times | MAINTAINERS.md review at every handoff |
| 8 | PRs to `main`, one topic each, checks green | Branch protection; CI lint and link check |
| 9 | Unknowns are `[TBD]`, never guessed | Review; `check.sh` counts open `[TBD]` markers |
| 10 | Small files, plain Markdown, no binaries over 1 MB | Review; large media goes in the shared drive |

## Rule 1: Evergreen vs dated

**The rule.** `docs/` holds evergreen material only. Anything tied to a date, a person, or a semester lives under `semesters/<YYYY-term>/`. If an evergreen doc needs a dated example, it links into a semester folder rather than carrying the date.

**Why.** A reader has to be able to trust that anything in `docs/` is current without checking. The moment `docs/` carries "the Spring 2026 budget was $12,000", every reader has to wonder what else in there is old. Dated content in dated folders makes staleness visible from the path alone.

**Enforced by.** PR review. Reviewers ask one question of every changed line in `docs/`: will this still be true next semester? If not, it moves.

**When violated.** Move the dated content to the right semester folder (create the folder with `scripts/new-semester.sh` if it does not exist yet), replace it in `docs/` with a link, and mention the move in the PR description. Nothing else is needed.

## Rule 2: Naming

**The rule.** Folders and files are kebab-case (`event-checklist.md`, not `Event_Checklist.md`). Dates are ISO `YYYY-MM-DD`. Semester folders are `YYYY-term` (`2026-fall`, `2027-spring`, `2027-summer`). Event folders are `YYYY-MM-DD-slug`: the date the event starts, then a short kebab-case name.

**Why.** ISO dates and `YYYY-term` sort correctly in a plain file listing, so a folder of semesters or events reads as a timeline without any tooling. kebab-case avoids case-sensitivity surprises between macOS, Windows, and Linux, and keeps URLs clean.

**Enforced by.** The scripts (`new-semester.sh`, `new-event.sh`, `new-meeting.sh`) create correctly named files, so use them instead of creating files by hand. Review catches hand-made names.

**When violated.** Rename with `git mv` in its own PR (one topic per PR, see rule 8), then fix every relative link that pointed at the old name. Run `scripts/check.sh` to catch links you missed.

## Rule 3: Templates are contracts

**The rule.** Change `templates/` or `semesters/_template/` only with an entry in [decision-log.md](decision-log.md). Never hand-edit a copy when the template is wrong; fix the template, log it, and then fix the copy.

**Why.** Every semester folder is a copy of `_template/`. If the template has a bad section, every future copy has it too. If someone fixes one copy and not the template, the next team inherits the bug. Templates are also what the scripts and the retrospective compare against, so a silent change to a template changes what "done" means for every semester after it.

**Enforced by.** `.github/CODEOWNERS` requires a maintainer review on `templates/` and `semesters/_template/`. The PR template asks whether a template changed and whether the decision log has an entry.

**When violated.** If a copy was edited instead of the template: open a PR that makes the same change in the template, add the decision log entry, and note which copies already carry the change. If a template was changed without a log entry: add the entry now, dated to the merge, and link the PR that made the change.

## Rule 4: Privacy

**The rule.** Never commit personal phone numbers, personal emails, student IDs, home addresses, signatures, or photos of people without written consent. Rosters are counts only. Officer names appear only with the officer's consent. Financial figures are fine; bank or trust account numbers are not.

**Why.** This repo is public and its history is permanent. A member who joins the Discord did not agree to have their name in a GitHub commit forever. Financial figures (how much a trip cost, how much ASRCC granted) are institutional memory the next team needs; account numbers are not.

**Enforced by.** `scripts/check.sh` scans for phone number and email patterns before you open a PR. Reviewers check rosters, meeting notes, and anything copied from a form. Full detail in [privacy-and-public-repo-policy.md](privacy-and-public-repo-policy.md).

**When violated.** Follow the removal steps in the privacy policy. Deleting the line in a new commit is not enough; the data stays in history until the history is rewritten.

## Rule 5: Decisions are logged

**The rule.** Any binding choice (budget, policy, event go/no-go, template change) gets a one-paragraph entry in [decision-log.md](decision-log.md) with the date and who decided.

**Why.** Six months from now, someone will ask "why do we do it this way?" The log is the only place that answer survives officer turnover. It also stops decisions from being re-litigated every semester because nobody remembers they were already made.

**Enforced by.** The PR template has a "does this PR record or implement a decision?" checkbox. Reviewers check that budget, policy, and go/no-go changes have a matching log row. The decision issue template (`.github/ISSUE_TEMPLATE/decision.yml`) is the front door for proposing one.

**When violated.** Add the entry now. Date it to when the decision was actually made, not when you wrote it down, and link the meeting note or PR where it happened. If nobody can say who decided, write the role (for example "officer meeting") rather than guessing a name.

## Rule 6: Semester close is required

**The rule.** A semester is not done until `retrospective.md` and `handoff.md` in that semester's folder are filled in and the next semester's folder exists. The outgoing team opens the PR; the incoming team reviews and merges it.

**Why.** The close is where the club's memory is actually written down: what worked, what did not, what the next team must do in week one. If the outgoing team leaves without it, that knowledge leaves with them. Having the incoming team merge it forces them to read it.

**Enforced by.** The handoff PR is reviewed by the incoming officers, using the acceptance checklist in [handoff-procedure.md](handoff-procedure.md). The definition of done is in [semester-lifecycle.md](semester-lifecycle.md).

**When violated.** If a semester was never closed: the current team fills in what it can from meeting notes and Discord history, marks the rest `[TBD]`, and merges it with a note that it was reconstructed after the fact. Do not leave the folder half-finished; a reconstructed retro with gaps beats an empty file.

## Rule 7: Two admins minimum

**The rule.** [MAINTAINERS.md](../../MAINTAINERS.md) lists at least two repo admins at all times, one of whom is not graduating this year. The advisor is listed as a fallback contact.

**Why.** A repo with one admin is one graduation, one lost phone, or one forgotten password away from being unreachable. The "not graduating" clause is what makes the rule survive the end of the year instead of just the end of the semester.

**Enforced by.** MAINTAINERS.md is reviewed at every handoff (step in [handoff-procedure.md](handoff-procedure.md)). CODEOWNERS requires a maintainer review on MAINTAINERS.md itself. Note: while the repo lives under a personal GitHub account, GitHub allows only one owner; see the GitHub section of the handoff procedure for how the second-admin requirement is met until the repo moves to a club-owned organization.

**When violated.** Treat it as urgent. The remaining admin adds a second admin the same week, and MAINTAINERS.md is updated in the same PR. If no eligible officer exists, the advisor becomes the second admin until one is elected.

## Rule 8: PRs, not direct pushes, to main

**The rule.** Every change to `main` goes through a pull request. One topic per PR. Any officer can review. Link checks and lint must pass.

**Why.** Review is how rules 1 through 5 actually get checked. One topic per PR keeps reviews short enough that people do them, and makes a bad change easy to revert without losing a good one. Automated checks catch broken links and formatting so reviewers can spend their attention on content.

**Enforced by.** Branch protection on `main` (require a PR, require one review, require the `markdownlint` and `links` status checks). CI runs [docs-check.yml](../../.github/workflows/docs-check.yml) on every PR and push. Run `scripts/check.sh` locally first to avoid a red build.

**When violated.** If something was pushed directly: do not revert it blindly. Open a PR that either reverts it or reviews it after the fact, so the change gets the review it skipped. Then check that branch protection is still on; a direct push usually means it was turned off or the pusher bypassed it as an admin.

## Rule 9: Unknowns are marked [TBD]

**The rule.** Anything you do not actually know is written as `[TBD]`, ideally with a note on what would resolve it (`[TBD: confirm with Student Activities]`). Never guess a date, a name, a dollar amount, a room, or a policy.

**Why.** A plausible-looking wrong fact is worse than an obvious gap. Someone will plan around a guessed date or budget line and find out at the worst time. `[TBD]` is honest and searchable, so the next person can find and close every open question.

**Enforced by.** Review. `scripts/check.sh` counts open `[TBD]` markers and prints the grep command that lists them; it does not fail on them.

**When violated.** If you find a fact that was guessed, replace it with `[TBD]` or the verified value, and say in the PR where the verified value came from. If a guessed fact was already acted on (an event planned around a wrong deadline), add a decision log entry so the history shows what happened.

## Rule 10: Small files, plain Markdown

**The rule.** Text is Markdown. No binaries over 1 MB in the repo. Logos and brand files go in `assets/` as SVG or PNG under 1 MB each. Large media (photos, video, slide decks, PDFs of forms) lives in the club's shared drive and is linked from the repo.

**Why.** Git keeps every version of every file forever, so one 30 MB video makes every future clone 30 MB heavier. Markdown diffs cleanly in review; PDFs and images do not. And the shared drive is where non-technical members already look for media.

**Enforced by.** Review. Before approving a PR that adds a file under `assets/`, the reviewer checks its size. If a file is too large, the PR is not merged until it is replaced with a link.

**When violated.** If a large file was already merged: remove it in a PR, link its shared-drive location, and note that the file stays in git history. Rewriting history to purge it is optional for size (unlike privacy data, where it is required) and needs a decision log entry because it forces everyone to re-clone.
