# Page kit

A companion page is the page students open on their own laptop or phone beside a deck: the ICPC practice page and the parking gate lab for 2026-10-29 are the first two. This folder makes every such page look like the same club, from the design system, without copying CSS into each generator.

| File | What it is |
|---|---|
| `pagekit.py` | Python helpers. Each returns an HTML string. `page()` wraps the body and inlines the CSS |
| `page.css` | The page layer: masthead, start block, progress strip, cards, steps, the code block, reveals, figures, wiring groups, input/output pair, footer |
| `viz.css` | The `.viz` picture classes deck.css gives a slide, so labkit drawings render the same on a page |
| `check-page.mjs` | The check. Run it on every page before publishing |
| `../templates/companion-page.py` | A starting point to copy |

## How it is built

`page()` inlines, in order: `docs/04-brand/design-system/tokens.css` verbatim (tokens, reset, headings, prose flow, tables, `.acm-card`, `.acm-callout`, `.acm-button`, `.acm-rail`, dark mode, print), `viz.css`, labkit's `lab_css()` when the page draws boards, then `page.css`. Nothing in `page.css` is a raw number: every size, gap, radius and color is a token or a sum of tokens, so the page follows the system when the system changes. Headings stay at weight 500 (`--acm-weight-strong`), as documents.md §6.3 asks. Dark mode comes from tokens.css, through `prefers-color-scheme` and `data-theme`.

Two page-level values the system does not carry, both in `page.css`: `--pk-start-bg` and `--pk-start-ink`. Light uses the sanctioned orange fill with `--acm-on-surface` (4.92:1, foundations §2.2). Dark has no orange fill token, so the start block falls back to the primary container pair.

## Helpers

| Helper | Use it for |
|---|---|
| `mast(h1, lede, pic_html='')` | The top: the Rail, the club name, the h1, one line. A picture beside it on wide screens |
| `start_block(eyebrow, do, detail, href, button)` | One action above the fold, on the orange fill. One per page |
| `progress([(mark, words, '#anchor'), ...])` | A sticky strip of jump links (Set up, 1 to 4, Challenges; or 1 to 12) |
| `section(id, title, body, eyebrow, intro)` | An h2 section; eyebrow is the ledger line above the heading |
| `steps([html, ...])` | Short numbered steps, like the phase rows in components.md §7.12 |
| `code(key, label, text, preview=None, mark=None)` | The code block from components.md §7.11: a header row with the file label and a Copy button that copies the whole text from `data-clean-code`, line numbers past ten lines. With `preview` (0-based line numbers) it shows only those lines, wrapped, with `mark` highlighting the lines a student edits, and the full listing one tap away |
| `reveal(kind, body, label)` / `reveals(...)` | Closed blocks: `starter`, `hint`, `mistake`, `answer`, `more` |
| `card(n, title, body, meta, cid)` / `cards([...])` | A numbered card in a list |
| `table(head, rows, cls)` | `th scope="col"`, tinted header, horizontal rules only (§7.6) |
| `figure(svg, caption, board=False)` | A picture with a caption. `board=True` leaves room for the sensor that hangs past a breadboard's edge |
| `io(input, output)` | Input and output side by side |
| `callout(kind, label, body)` | The closed set: `note`, `warning`, `check` |
| `qr(url, label)` | A QR tile, dark on white in both themes |
| `footer(lines, updated)` | Sources, the meeting line, and the freshness stamp (§7.10) |

Text arguments are plain text; `md()` turns `` `code` `` and `**bold**` into markup, and most helpers run it for you.

## Rules learned building the first two pages

- **One Start block with one action.** A beginner should know what to do first within five seconds. Everything else is a step below it.
- **Basics first, but short.** Show the four things a beginner needs before the first task; put the rest after the tasks, closed.
- **Show only the lines a student edits.** A 40 to 60 line starter is a wall; `code(..., preview=...)` shows the edit lines and keeps the rest one tap away. Copy still copies everything.
- **Never clip code on a phone.** On narrow screens code wraps (a sideways scrollbar on a phone only shows while scrolling, so a long line looks cut off). Wider screens scroll inside the block as §7.11 says.
- **Split a wiring table by group**, each with a small board picture of only that group. When two neighboring wire tags would collide at page size, add `pk-group--quiet` and name the parts in the caption.

## Checking it

```sh
node deck-kit/page/check-page.mjs site/decks/<slug>/index.html --shots /tmp/page-shots --click
```

It fails on token drift from tokens.css, any `--acm-*` token the system does not define, duplicate ids, text under 13 px, text under 4.5:1 (3:1 for large text) against its real background in light and in dark with every `<details>` open, horizontal page scroll at 1280 and 390 px, and console errors. `--shots` writes full-page screenshots at both widths in both themes (closed and opened); look at them. `--click` presses the first Copy button with a real mouse event at its center, after checking it is the element under that point, and reports what reached the clipboard.

---

**Last updated: 2026-10-28.**
