# ACM @ RCC: club docs and decks

Public docs repo for the ACM chapter at Riverside City College, plus the weekly meeting decks (`deck-kit/`, `semesters/<term>/meetings/<date>-deck.html`). Several collaborators run Claude Code against it, so this file, `docs/status.md`, `docs/agent-log.md`, and the live deck review are how agents on different machines share context. Deck-building rules: [deck-kit/CLAUDE.md](deck-kit/CLAUDE.md). Repo rules: [CONTRIBUTING.md](CONTRIBUTING.md).

The **Context rule**, **Sync**, and **Review** rules below are mandatory, and hooks in `.claude/settings.json` enforce the first two. They are the shared coworking kit, the same in rcc-gdg and pcolee/explorAI; `scripts/coworking.conf` is the only per-repo part.

## Context rule (hard)

Before building anything, meaning any edit to a repo file or any commit, cross-reference new and existing context:

1. **New:** what others did since you last worked here. The session-start brief lists their commits and the files each touched; `git show <sha>` for detail. It also lists open review comments on the decks.
2. **Existing:** `docs/status.md`, the open questions and recent entries in `docs/agent-log.md`, this file, the files you are about to change, and the previous week's deck (structure, style, bugs already fixed).
3. **Say it:** before the first edit, tell the user under **Context check:** in 1 to 3 lines what is relevant and how your plan accounts for it, or that nothing affects it. If the context conflicts with the request (someone else already built it, a decision went the other way, an open question is unresolved), ask before building.

Enforcement: the first edit or commit of every session, and the first one after someone else's commits arrive, is blocked once and returns the brief (`scripts/hooks/context-gate.sh`). It opens when the check shows up in the session transcript, or after `scripts/context.sh --ack "Context check: ..."` with the same lines. Run `scripts/context.sh` any time to see the brief. Edit repo files with the edit tools, not shell rewrites, so the gate sees them.

Where context lives: `docs/status.md` (current snapshot, rewritten at every `/handoff`), `docs/agent-log.md` (one entry per person per day, plus open questions), commit messages (step-by-step progress), this file (rules that stay true, never dated facts), and the live review (what people flagged on each slide).

## Sync

- **Starting Claude outside this folder?** Project hooks only load when Claude starts inside the repo. Run `scripts/install-bridge.sh` once per machine so they also run in sessions started elsewhere, once a prompt names ACM or an edit lands here.
- **Pull before you work.** Hooks run `scripts/sync.sh pull` at session start and before every prompt. New commits from others are their progress. On `SYNC CONFLICT`, `SYNC BLOCKED`, or edits sent to the stash, stop and tell the user before editing anything.
- **Work on `main`.** No branches or PRs for collaborators. Commit small, one change per commit, with a message that says what changed and why.
- **Push after every verified change, without asking.** Stage files by name (`git add <paths>`, never `-A` or `.`), commit, then `scripts/sync.sh push` (pull, `scripts/push-check.sh` on exactly what is committed, push, retry on a race). Never `git push` directly; a hook blocks it.
- **Verified means opened in a browser.** For a deck: `node deck-kit/check.mjs <deck>` passes and you looked at its screenshots.
- **Publishing is separate.** `main` is the source; a deck goes live only through `scripts/publish-deck.sh <deck> <slug> --push`, and only when the user asks. Push the source to `main` first so the live deck matches it.
- **On conflict: stop.** `sync.sh` aborts the rebase and leaves your commits as they were. Never force-push, `reset --hard`, or delete someone else's changes.
- **During a meeting** (Thursdays, BLCIS A-210; the time is on each deck's ledger line), do not publish that week's deck unless the presenter asks.
- **Hand off before you stop.** After committing work, run `/handoff`. A Stop hook reminds you if work is unlogged, unpushed, or uncommitted.
- `docs/agent-log.md` merges with git's `union` driver, so two entries added at once both survive.

## Review (comments and speakers on the decks)

- Every deck loads `deck-kit/review.js`. `C` opens a side panel: who covers the slide and its comment threads. `?view=review` on the deck's URL is the whole-deck board. Changes reach everyone's screen in about a second, through the club relay (`/review/` on `deck-relay`, saved in Firestore).
- Agents use `node scripts/review.mjs`: `brief`, `show <deck>`, `add <deck> <slide> <text>`, `reply`, `resolve <deck> <id> <what changed>`, `assign <deck> <3-7> <name|->`. Anything an agent writes is marked agent.
- A comment is a request from a person. Treat open comments on a deck you are editing as part of the task: fix them or reply why not, and resolve each one you fixed in the same turn (`/handoff` checks).
- Slides are keyed by `aria-label` (or `data-id`). Renaming a slide's `aria-label` orphans its comments and speaker; set `data-id` to the old key first if a slide has either.
- The passcode is in `~/.config/rcc-review/key` (`node scripts/review.mjs login`). It never goes in the repo, and neither does comment text: the repo is public.
- `publish-deck.sh` bakes the current speakers into the published deck as `data-owner`, so the presenter view shows them offline.

## Rules

- This repo is public. Never commit member names, sign-in or form responses, phone numbers, or emails ([privacy policy](docs/01-governance/privacy-and-public-repo-policy.md)). Officers by role unless they consented.
- Keep this file short and only for things that stay true. Dated facts, decisions, and open questions go in `docs/agent-log.md`; binding decisions also go in the [decision log](docs/01-governance/decision-log.md).
