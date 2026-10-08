# Agent log

Shared handoff log for anyone (human or agent) working in this repo. Newest entry first. Each entry: date, who, what changed, what is open. Keep entries short; link to files instead of pasting them.

## Open questions

Remove a line once it is answered and note the answer in that day's entry.

- The microcontroller lab kit order (2026-09-20, see `semesters/2026-fall/budget.md`) has no Pico 2 W, but the station cards assume one. Change the cards or the hardware?

<!-- newest entry below: add "## YYYY-MM-DD · Name (via Claude Code)" here and end it with a blank line -->

## 2026-10-07 · Sam (via Claude Code)

**Changed:**

- Committed the uncommitted work on `2026-10-01-deck` (auto beats in the kit, the 10-08 deck, the lab kit purchase in the budget, flyers, the 09-03 deck), then merged it into `main` through PR #3, which also carried PR #2. Branch protection: no PR required, force-pushes and deletion still blocked. Left uncommitted on purpose: `semesters/2026-fall/meetings/2026-09-03-prep.md` (marked "not committed") and the 09-03 deck's working folder (spec, copy, render script; fails markdownlint).
- Added the shared coworking kit (same files as rcc-gdg and the ExplorAI decks repo) and live review: `deck-kit/review.js`, speaker labels in `presenter.js`, `scripts/review.mjs`, the bake step in `scripts/publish-deck.sh`. The 09-24, 10-01, and 10-08 decks load it.
- `CLAUDE.md`, `CONTRIBUTING.md`, maintenance rule 8, `MAINTAINERS.md`, and the decision log now describe working on `main`.

- Shared kit fixes (late evening, all three repos): `scripts/hooks/bridge.sh` judges a shell command by the folder it runs in (a leading `cd`, or `git -C`); `deck-kit/review.js` sets the panel's board link in code, because `publish-deck.sh` refused a bundle carrying a literal local `href`.

**Issues:** the main clone (`rcc-acm`) is still on branch `2026-10-01-deck` with another session's uncommitted edits to the 10-08 deck. Once that session commits, switch the clone to `main` and merge the branch in. The committed 10-08 deck fails 15 clock-slide layout checks in `deck-kit/check.mjs`.

**Next:** Sam: finish the 10-08 deck in its session, commit, then move that clone to `main`. Collaborators: `scripts/install-bridge.sh` once if you start Claude outside the repo, and `node scripts/review.mjs login`.
