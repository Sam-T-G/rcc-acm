# Status

Where everything stands right now. `/handoff` rewrites this file in place (it is a snapshot, not a log). History and reasons go in [agent-log.md](agent-log.md). Slide counts, last changes, and open review comments are computed by `scripts/context.sh`, so they are not repeated here.

Last updated: 2026-11-19 by Sam.

## Decks

| Date | Deck | State | Next / blocking |
|---|---|---|---|
| 2026-09-03 | First meeting (`semesters/2026-fall/meetings/2026-09-03-deck.html`) | Presented | None. Single-file deck from before the kit; no review panel. |
| 2026-09-24 | `2026-09-24-deck.html` | Presented | None. |
| 2026-10-01 | `2026-10-01-deck.html` (career disk) | Presented | None. Live at `/decks/2026-10-01/`. |
| 2026-10-08 | `2026-10-08-deck.html` (breadboard rounds, servo and button) | Presented | None. Live at `/decks/2026-10-08/`. |
| 2026-10-15 | `2026-10-15-deck.html` (upload crash course, transistor fan) | Presented | None. Live at `/decks/2026-10-15/`. |
| 2026-10-29 | `2026-10-29-deck.html` (ICPC or parking gate) | Presented | None. Live at `/decks/2026-10-29/` with its ICPC and gate pages. |
| 2026-11-19 | `2026-11-19-deck.html` (spring project ideas; plan `2026-11-19-plan.md`) | Live at `/decks/2026-11-19/` (republished after the copy pass, `2a027f6`) | 12 slides, 202 of 202 checks. Sign-up on paper. After the meeting: transcribe the board photo and sign-ups into a `2027-spring` projects folder. No record of the 11-05 and 11-12 meetings. |

## Standing facts

- Meetings: Thursdays in BLCIS A-210 (the time is on each deck's ledger line).
- Live decks: `https://sam-t-g.github.io/rcc-acm/decks/<slug>/`, published from `main` with `scripts/publish-deck.sh` (the `gh-pages` branch).
- Collaborators push to `main` through `scripts/sync.sh push` (since 2026-10-07; see the decision log). Branch protection blocks force-pushes and deletion only. PR #1 (the microcontroller lab proposal) is still open.
- Review: `A` in a deck to annotate, `I` for the notes inbox, `?view=review` for the board, `node scripts/review.mjs` for agents. Google sign-in, limited to each club's member list on the relay. Decks published before 2026-10-08 still run the older passcode panel (`C`) until they are republished.
- Presenter tools: `S` presenter view, `M` phone or tablet remote, `?view=runsheet` (`deck-kit/README.md`).
