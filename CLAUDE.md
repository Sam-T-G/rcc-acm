# ACM @ RCC: club docs and decks

Public docs repo for the ACM chapter at Riverside City College, plus the weekly meeting decks (`deck-kit/`, `semesters/<term>/meetings/<date>-deck.html`). Several collaborators run Claude Code against it, so this file, `docs/status.md`, `docs/agent-log.md`, and the live deck review are how agents on different machines share context. Deck-building rules: [deck-kit/CLAUDE.md](deck-kit/CLAUDE.md). Repo rules: [CONTRIBUTING.md](CONTRIBUTING.md).

The **Context rule**, **Sync**, and **Review** rules below are mandatory, and hooks in `.claude/settings.json` enforce the first two. They are the shared coworking kit, the same in rcc-gdg and pcolee/explorAI; `scripts/coworking.conf` is the only per-repo part.

## Context rule (hard)

Before building anything, meaning any edit to a repo file or any commit, cross-reference new and existing context:

1. **New:** what others did since you last worked here. The session-start brief lists their commits and the files each touched; `git show <sha>` for detail. It also lists open review notes on the decks.
2. **Existing:** `docs/status.md`, the open questions and recent entries in `docs/agent-log.md`, this file, the files you are about to change, and the previous week's deck (structure, style, bugs already fixed).
3. **Say it:** before the first edit, tell the user under **Context check:** in 1 to 3 lines what is relevant and how your plan accounts for it, or that nothing affects it. If the context conflicts with the request (someone else already built it, a decision went the other way, an open question is unresolved), ask before building.

Enforcement: the first edit or commit of every session, and the first one after someone else's commits arrive, is blocked once and returns the brief (`scripts/hooks/context-gate.sh`). It opens when the check shows up in the session transcript, or after `scripts/context.sh --ack "Context check: ..."` with the same lines. Run `scripts/context.sh` any time to see the brief. Edit repo files with the edit tools, not shell rewrites, so the gate sees them.

Where context lives: `docs/status.md` (current snapshot, rewritten at every `/handoff`), `docs/agent-log.md` (one entry per person per day, plus open questions), commit messages (step-by-step progress), this file (rules that stay true, never dated facts), and the live review (what people flagged on each slide).

## Sync

- **Set up once per machine (a person, in a terminal):** `scripts/install-bridge.sh`. The hooks then run an approved copy of their scripts from `~/.config/rcc-coworking/`, never the repo's own files, and also run in sessions started outside the repo once a prompt names ACM. Until it is run, sessions print a one-line notice and no hooks run.
- **Pull before you work.** Hooks run `scripts/sync.sh pull` at session start and before every prompt. New commits from others are their progress. On `SYNC CONFLICT`, `SYNC BLOCKED`, or edits sent to the stash, stop and tell the user before editing anything. Never `git pull`, `merge`, or `rebase` directly; a hook blocks it.
- **`SYNC HELD` means someone changed a file the hooks run** (`scripts/hooks/`, `sync.sh`, `context.sh`, `review.mjs`, `coworking.conf`, `install-bridge.sh`, `.claude/`). Nothing was pulled. Stop and tell the user who changed what; they review and approve it in a terminal with `~/.config/rcc-coworking/approve <repo>`. Never run `approve` or `install-bridge.sh` yourself, never pull around a hold, and treat a change to those files as code that will run on everyone's machine.
- **Work on `main`.** No branches or PRs for collaborators. Commit small, one change per commit, with a message that says what changed and why.
- **Push after every verified change, without asking.** Stage files by name (`git add <paths>`, never `-A` or `.`), commit, then `scripts/sync.sh push` (pull, `scripts/push-check.sh` on exactly what is committed, push, retry on a race). Never `git push` directly; a hook blocks it.
- **Verified means opened in a browser.** For a deck: `node deck-kit/check.mjs <deck>` passes and you looked at its screenshots.
- **Publishing is separate.** `main` is the source; a deck goes live only through `scripts/publish-deck.sh <deck> <slug> --push`, and only when the user asks. Push the source to `main` first so the live deck matches it.
- **On conflict: stop.** `sync.sh` aborts the rebase and leaves your commits as they were. Never force-push, `reset --hard`, or delete someone else's changes.
- **During a meeting** (Thursdays, BLCIS A-210; the time is on each deck's ledger line), do not publish that week's deck unless the presenter asks.
- **Hand off before you stop.** After committing work, run `/handoff`. A Stop hook reminds you if work is unlogged, unpushed, or uncommitted.
- `docs/agent-log.md` merges with git's `union` driver, so two entries added at once both survive.

## Review (notes and speakers on the decks)

- Every deck loads `deck-kit/review.js`, which loads the club relay's annotation client. In a deck, `A` toggles annotate mode: pin a note to a spot, a selected phrase, or the whole slide, or suggest replacement text. `I` opens the notes inbox. `?view=review` on the deck's URL is the whole-deck board with speakers. Sign-in is Google, limited to each club's member list on the relay. Changes reach everyone in about a second.
- Open notes show in the presenter view (`S`) and the remote, never on the screen the room sees.
- Agents use `node scripts/review.mjs` (commands at the top of the file): `brief`, `inbox <deck>` (each note with the source line it points at), `claim`, `resolve <deck> <id> --commit <sha> <what changed>`, `reply`, `annotate`, `assign`, `status`, `watch`. Anything an agent writes is marked agent. The relay also serves the same tools over MCP (`/mcp`).
- A note is a request from a person. When you edit a deck, run `inbox` first, `claim` each note you take, set `status` while you work, then fix it or reply why not. Apply an accepted suggestion exactly as written. Resolve each fixed note with the commit that fixed it, in the same turn (`/handoff` checks).
- Slides are keyed by `data-id`, else `id`, else the `aria-label` slug. Renaming a slide's `aria-label` orphans its notes and speaker; set `data-id` to the old key first if a slide has either.
- The agent token comes from "Connect an agent" in a deck (your avatar in the review bar) and lives in `~/.config/rcc-review/agent-token` (`node scripts/review.mjs login`). It never goes in the repo, and neither does note text or anyone's email: the repo is public.
- `publish-deck.sh` bakes the current speakers into the published deck as `data-owner`, so the presenter view shows them offline.

## Rules

- This repo is public. Never commit member names, sign-in or form responses, phone numbers, or emails ([privacy policy](docs/01-governance/privacy-and-public-repo-policy.md)). Officers by role unless they consented.
- Keep this file short and only for things that stay true. Dated facts, decisions, and open questions go in `docs/agent-log.md`; binding decisions also go in the [decision log](docs/01-governance/decision-log.md).
