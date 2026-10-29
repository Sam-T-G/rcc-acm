# Agent log

Shared handoff log for anyone (human or agent) working in this repo. Newest entry first. Each entry: date, who, what changed, what is open. Keep entries short; link to files instead of pasting them.

## Open questions

Remove a line once it is answered and note the answer in that day's entry.

- The microcontroller lab kit order (2026-09-20, see `semesters/2026-fall/budget.md`) has no Pico 2 W, but the station cards assume one. Change the cards or the hardware?

<!-- newest entry below: add "## YYYY-MM-DD · Name (via Claude Code)" here and end it with a blank line -->
## 2026-10-29 · Sam (via Claude Code)

**Changed:**

- `e44df00`: new deck rule, a visual on every slide where possible (deck-kit/CLAUDE.md, README, decision log). A real internet photo comes first. The cover, `giant` and `orange` statements, hero slides, and work clocks are exempt. The same rule went into rcc-gdg.
- `ff84216`, `b128163`, `4209eaa`: optional Playwright browser checks (`npm run test:browser`, deck-kit/README.md "Checking it"). Every meeting deck opens in Chrome and desktop Safari and must move on a Right press with no script error or missing repo file. Built pages in `site/decks/` also open on an iPhone-sized Safari with no sideways scroll. 21 of 21 passed twice. The deck templates now list their packages in a `# /// script` block, so `uv run` sets up the environment; their output is byte-identical to the old venv run, and the two-track build passes check.mjs 164 of 164. check.mjs and every deck are unchanged. `scripts/check.sh` on a clean tree gives the same result before and after (one markdownlint failure that was already there; the 5,688 "personal info" hits on a local run come from gitignored `scratch/` ICPC numbers).
- 10-29 audit (uncommitted until Sam's go): deck copy fixes (185 of 185), the officer guide trimmed of the old projected walkthrough, and fixes to the ICPC and gate pages (one-computer team line, gate paste-over-template step and a Stuck entry, debounce in `gate_stretch`, a button-as-car path for R4 tables, `gate_c2_count` prints only on change). Page sources are in gitignored `scratch/`.

**Decided:** Sam: a visual on every slide where possible; Playwright and uv in all three club repos.

**Next:** Sam's go to republish the 10-29 deck and both pages, and to commit the deck and guide. The real-kit dry run (`sensor_test`, `keypad_test`) still hasn't been done.


## 2026-10-08 · Sam (via Claude Code)

**Changed:**

- Hook pinning: every hook runs a copy each person approved in `~/.config/rcc-coworking/`. A pull that changes `scripts/hooks/`, `sync.sh`, `context.sh`, `review.mjs`, `coworking.conf`, `install-bridge.sh`, or `.claude/` stops with `SYNC HELD` until a person approves the diff in a terminal (`~/.config/rcc-coworking/approve <repo>`). Raw `git pull`, `merge`, and `rebase` are blocked. Same kit in all three repos. (`b743ce2`)
- `deck-kit/check.mjs`: mock keychain, and typed keys without native key codes (`f48866c`).
- Review v2 (`7271e70`, `56eaedb`): `deck-kit/review.js` loads the relay's annotation client (`A` to annotate, `I` for the inbox, `?view=review`, Google sign-in limited to club members). `presenter.js` lists each slide's open notes in the presenter view and remote, never on the room's screen. `scripts/review.mjs` uses the v2 API with an agent token. The relay's v1 passcode review is retired. No published ACM deck loaded v1, so none needed republishing.

**Issues:** Until each person runs `scripts/install-bridge.sh` once in a terminal, hooks here print a one-line notice and do not run. The main clone is still on `2026-10-01-deck` with another session's edits; these commits went to `main` from a worktree.

**Next:** add the officers' emails to the relay's ACM member list (`node admin.mjs add acm <email> <name>` in deck-relay).

## 2026-10-07 · Sam (via Claude Code)

**Changed:**

- Committed the uncommitted work on `2026-10-01-deck` (auto beats in the kit, the 10-08 deck, the lab kit purchase in the budget, flyers, the 09-03 deck), then merged it into `main` through PR #3, which also carried PR #2. Branch protection: no PR required, force-pushes and deletion still blocked. Left uncommitted on purpose: `semesters/2026-fall/meetings/2026-09-03-prep.md` (marked "not committed") and the 09-03 deck's working folder (spec, copy, render script; fails markdownlint).
- Added the shared coworking kit (same files as rcc-gdg and the ExplorAI decks repo) and live review: `deck-kit/review.js`, speaker labels in `presenter.js`, `scripts/review.mjs`, the bake step in `scripts/publish-deck.sh`. The 09-24, 10-01, and 10-08 decks load it.
- `CLAUDE.md`, `CONTRIBUTING.md`, maintenance rule 8, `MAINTAINERS.md`, and the decision log now describe working on `main`.

- Shared kit fixes (late evening, all three repos): `scripts/hooks/bridge.sh` judges a shell command by the folder it runs in (a leading `cd`, or `git -C`); `deck-kit/review.js` sets the panel's board link in code, because `publish-deck.sh` refused a bundle carrying a literal local `href`.

**Issues:** the main clone (`rcc-acm`) is still on branch `2026-10-01-deck` with another session's uncommitted edits to the 10-08 deck. Once that session commits, switch the clone to `main` and merge the branch in. The committed 10-08 deck fails 15 clock-slide layout checks in `deck-kit/check.mjs`.

**Next:** Sam: finish the 10-08 deck in its session, commit, then move that clone to `main`. Collaborators: `scripts/install-bridge.sh` once if you start Claude outside the repo, and `node scripts/review.mjs login`.
