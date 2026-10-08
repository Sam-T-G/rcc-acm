# Status

Where everything stands right now. `/handoff` rewrites this file in place (it is a snapshot, not a log). History and reasons go in [agent-log.md](agent-log.md). Slide counts, last changes, and open review comments are computed by `scripts/context.sh`, so they are not repeated here.

Last updated: 2026-10-07 by Sam.

## Decks

| Date | Deck | State | Next / blocking |
|---|---|---|---|
| 2026-09-03 | First meeting (`semesters/2026-fall/meetings/2026-09-03-deck.html`) | Presented | None. Single-file deck from before the kit; no review panel. |
| 2026-09-24 | `2026-09-24-deck.html` | Presented | None. |
| 2026-10-01 | `2026-10-01-deck.html` (career disk) | Presented | None. Live at `/decks/2026-10-01/`. |
| 2026-10-08 | `2026-10-08-deck.html` (feed warm-up, Arduino fan and strobe) | Drafting | Another session was still editing it on 2026-10-07 in the main clone (branch `2026-10-01-deck`). The committed copy fails 15 layout checks on its clock slides; that session's newer working copy should replace it. Live at `/decks/2026-10-08/` from an earlier publish. |

## Standing facts

- Meetings: Thursdays in BLCIS A-210 (the time is on each deck's ledger line).
- Live decks: `https://sam-t-g.github.io/rcc-acm/decks/<slug>/`, published from `main` with `scripts/publish-deck.sh` (the `gh-pages` branch).
- Collaborators push to `main` through `scripts/sync.sh push` (since 2026-10-07; see the decision log). Branch protection blocks force-pushes and deletion only. PR #1 (the microcontroller lab proposal) is still open.
- Review: `C` in a deck, `?view=review` for the whole deck, `node scripts/review.mjs` for agents. The passcode is shared by the club officers out of band and lives in `~/.config/rcc-review/key`.
- Presenter tools: `S` presenter view, `M` phone or tablet remote, `?view=runsheet` (`deck-kit/README.md`).
