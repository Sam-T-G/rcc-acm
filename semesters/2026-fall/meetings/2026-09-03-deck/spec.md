# Build spec: ACM @ RCC kickoff deck, 2026-09-03

This is the single document a builder implements. Exact copy lives in `deck-copy.md` (same folder) and is quoted here where it matters; every colour, size, and motion value not restated here is in `token-sheet.md`; the MUST and NEVER list is `slide-rules.md`. Where this spec and the deck copy differ in wording, this spec wins (the differences are deliberate and listed in §11).

## 1. Design plan

**Concept.** Dark text on a light background with one accent hue, readable from the back of A-210 in daylight. Every slide is one block of type between two fixed hairlines, sized by what it is: a sentence at 136 px, a table at 40 px, a numeral at 224 px. When content doesn't fit, add a slide instead of shrinking the type. The only marks that are not letters are the Rail on slide 1, two hairlines, and the QR.

**Colour** (light theme only; `<div id="stage" data-theme="light">`; no dark block anywhere).

| Hex | Token | Job on slides |
|---|---|---|
| `#fdf8f7` | `--acm-surface` | Stage ground, `body` background, letterbox |
| `#221f1e` | `--acm-on-surface` | Every title, body line, numeral, QR module |
| `#5c5958` | `--acm-on-surface-variant` | Eyebrow, counter, captions, labels under numerals, table heads (6.59:1) |
| `#dacfcc` | `--acm-outline-variant` | The two structural hairlines, table row rules |
| `#7e7572` | `--acm-outline` | The inset 1 px hairline on every callout, the QR frame |
| `#ae3200` | `--acm-primary` | The Rail on slide 1, the short Rail on Warning and Check callouts, focus ring. Nothing else |
| `#f0e6e3` | `--acm-surface-container-high` | Table header row, Note callout fill |
| `#ffdbd0` / `#661900` | `--acm-primary-container` / `--acm-on-primary-container` | Warning callout fill and ink |
| `#c9f2d0` / `#003e17` | `--acm-live-container` / `--acm-on-live-container` | Check callout fill and ink |
| `#ffffff` | `--acm-surface-container-lowest` | QR quiet zone |

No other colour. Meeting types, tiers, pillars, and dates carry no hue; emphasis is weight 500 and the word itself.

**Type.** Inter and JetBrains Mono from the Google Fonts CSS2 API using the exact link form in `token-sheet.md` §4 (Inter with the `opsz` axis). `font-optical-sizing: auto`; never `font-variation-settings`; never `-webkit-font-smoothing` on `body`. All sizes are px on the 1920 x 1080 stage.

| Role | px / line | Tracking | Weight | Face | Used for |
|---|---|---|---|---|---|
| name | 200 / 200 | -0.02em | 500 | Inter | "ACM @ RCC" on s01 |
| numeral-xl | 224 / 224 | -0.02em | 500, tabular | Inter | s05 figures |
| display | 136 / 143 | -0.02em | 500 | Inter | s03 sentence, s10 figures (tabular) |
| title | 96 / 108 | -0.015em | 500 | Inter | Every slide `<h2>`; `max-width: 20ch`; `text-wrap: balance` |
| dense title | 76 / 96 | -0.01em | 500 | Inter | Pillar names (s04), rungs (s14) |
| lead | 48 / 64 | -0.005em | 400 | Inter | Lists of five lines or fewer, the s16 sentence |
| label | 44 / 60 | 0 | 500 | Inter | s01 date and room, tier codes (s09), leading columns (s02, s07, s08) |
| body | 40 / 64 | +0.005em | 400 | Inter | Running copy, callout body; 40 / 56 inside tables and grid cells |
| table head | 36 / 48 | +0.01em | 500 | Inter | `thead th` only |
| caption | 36 / 48 | +0.008em | 400 | Inter, variant ink | The sentence-length ledger lines in the bottom band |
| ledger | 32 / 48 | +0.08em | 500 | JetBrains Mono, uppercase | Eyebrow and counter only. Never a URL or a sentence |
| url | 40 / 48 | 0 | 500 | JetBrains Mono, ligatures off, no transform | Discord invite text, Instagram handle, repo URL |

Tracking flips sign at the label size (44 is the zero). Weight 700 appears at most once per slide: the bold label of a callout. `text-wrap: balance` on every `<h2>`, `pretty` on body. `font-variant-numeric: tabular-nums lining-nums` on every time, date, count, and dollar amount.

**Layout.** Stage 1920 x 1080. Margins 96 on every side; content box x 96 to 1824, y 96 to 984 (1728 x 888). Twelve columns of 122 with 24 gutters: half 852, third 560, quarter 414. Two full-width hairlines fix every slide: the top band y 96 to 144 (eyebrow left, counter right) with a 1 px hairline at y 160; the bottom hairline at y 880 with the caption band y 896 to 984. Body starts at y 324 after a one-line 96 px title (title box y 184 to 292), at y 432 after a two-line title. Body must end at or above y 848. Every value is px inside the scaled stage; no `vw`, `rem`, or `clamp()`.

## 2. File contract

Single HTML file. No `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags: the host wraps the file and applies a reset (14 px system font, zero body margin, an off-white ground, `[hidden]{display:none!important}`). Order: `<title>ACM @ RCC Kickoff</title>`, the Google Fonts `<link>`, one `<style>`, the markup, one `<script>`. Fonts from `fonts.googleapis.com` only; no other external resource; no framework; no build step. Paint `body { background: #fdf8f7; margin: 0; overflow: hidden }` explicitly. The deck ignores the host's dark mode entirely: no `prefers-color-scheme` block. The file must render identically at 1920 x 1080, 1280 x 720, 1024 x 768, and any other viewport by scaling the stage.

## 3. CSS token block

```css
#stage {
  --acm-surface: #fdf8f7; --acm-on-surface: #221f1e; --acm-on-surface-variant: #5c5958;
  --acm-outline: #7e7572; --acm-outline-variant: #dacfcc;
  --acm-primary: #ae3200; --acm-primary-container: #ffdbd0; --acm-on-primary-container: #661900;
  --acm-live-container: #c9f2d0; --acm-on-live-container: #003e17;
  --acm-surface-container-high: #f0e6e3; --acm-surface-container-lowest: #ffffff;
  --acm-focus-ring: #ae3200;
  --acm-space-2: 8px; --acm-space-3: 12px; --acm-space-4: 16px; --acm-space-6: 24px; --acm-space-12: 48px;
  --acm-rail-w: 40px;              /* 2% of 1920, the share card proportion, snapped to the grid */
  --acm-radius-callout: 16px;
  --acm-font-sans: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --acm-font-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  /* motion: take durations and curves from token-sheet.md §8; effects track only for the crossfade */
}
```

Take the motion durations and the two easing curves from `token-sheet.md` §8 verbatim; do not invent values.

## 4. Stage, scaling, layers

- `#stage` is `position: fixed; left: 50%; top: 50%; width: 1920px; height: 1080px; transform: translate(-50%, -50%) scale(var(--s)); transform-origin: center; background: var(--acm-surface); overflow: hidden;`. `--s = min(innerWidth / 1920, innerHeight / 1080)`, recomputed on `resize` and `orientationchange`. The letterbox is `body`'s background, the same surface colour.
- Slides are `section.slide` stacked absolutely inside the stage, each 1920 x 1080. The active slide has `aria-current="true"`, `opacity: 1`, pointer events on; every other slide `aria-hidden="true"`, `inert`, `opacity: 0`, `visibility: hidden` after its fade. No slide is ever `display: none` (the crossfade needs both in the tree), but hidden ones are `visibility: hidden` so they are unreachable.
- Notes layer: `<aside data-layer="notes" hidden>` inside the stage, a bottom sheet 1920 x 400 at y 680, `--acm-surface-container-high` fill, 1 px `--acm-outline` top edge, padding 48, the active slide's notes as a `<ul>` at 36 / 48 in on-surface (notes are for the presenter's screen, so 36 is acceptable here and nowhere else). Toggled by N; closed by Escape. Never shown on load.
- Overview layer: `<div data-layer="overview" hidden>` inside the stage, surface fill, padding 96, a grid of 17 buttons (4 columns, 122-grid), each showing the counter number in ledger role and the slide title at 40 / 56; the active one carries a 2 px `--acm-primary` outline (the focus-ring token, so it is an active state, which the primary role permits). Toggled by O; Escape closes; Enter or click navigates and closes.
- Live region: `<output aria-live="polite" class="counter">07 / 17</output>` in the top band; it is the visible counter and the announcement.

## 5. Navigation

- Keys: ArrowRight, ArrowDown, Space, PageDown next; ArrowLeft, ArrowUp, PageUp previous; Home, End; N notes; O overview; F fullscreen (`documentElement.requestFullscreen`, exit on second press); Escape closes notes or overview. Ignore key events with modifiers.
- Hash routing: `#<slide id>`. On load, honour the hash (unknown or empty hash shows s01). On `hashchange`, show that slide. Navigation sets `location.hash` (history entries, so back and forward work).
- Pointer: a `click` listener on the stage. If `window.getSelection().toString()` is non-empty, or the target is inside an `<a>`, a `<button>`, the notes layer, or the overview, do nothing. Otherwise x in the right 60% of the stage advances, the left 40% goes back. No element is ever laid over the content, so the club name and every URL remain selectable text.
- Touch: horizontal swipe over 60 px with vertical drift under 40 px advances or goes back.
- Two small `<button>`s "Previous" and "Next" in the letterbox only when a letterbox exists (positioned in `body` outside the stage, `label` role at 16 px screen px, variant ink, visible focus ring); hidden when the viewport is 16:9 within 1%. Keyboard remains the primary control.
- Focus: after every slide change, move focus to the active slide's `<h2>` (`tabindex="-1"`), with `outline: none` on that programmatic focus only; every real control keeps a 2 px `--acm-focus-ring` outline with 4 px offset.

## 6. Motion

Crossfade on the effects track only: the incoming slide fades from 0 to 1 over the token sheet's effects duration with its "enter" curve; the outgoing slide fades over the shorter "exit" duration. Nothing translates. Under `prefers-reduced-motion: reduce` the spatial track is already empty; leave the crossfade as the system allows (effects are exempt) but shorten it to the token sheet's minimum tier. No element is parked at `opacity: 0` at rest; the first slide is fully visible on load without any script running (set `aria-current` and the visible state on s01 in the markup, not only in JS).

## 7. Shared furniture on every slide except s01 and s03

- Eyebrow at (96, 96): ledger role, uppercase, on-surface-variant. Text per slide below. Dates are wrapped in `<time datetime>`.
- Counter at the right edge of the top band, right-aligned to x 1824, ledger role, tabular: `NN / 17`.
- Top hairline: 1 px `--acm-outline-variant` from x 96 to 1824 at y 160.
- Bottom hairline at y 880, same rule. The caption band beneath holds the slide's caption sentence (caption role) when it has one; otherwise it holds nothing.
- `<h2>` in the title role at (96, 184).

s01 has the Rail instead of the top band; s03 has no eyebrow and no title (its top band carries only the counter).

## 8. Slide-by-slide

Ids and order are fixed. Copy is verbatim from `deck-copy.md` except where §11 says otherwise. Speaker notes go in the notes layer verbatim from `deck-copy.md` for each slide.

**s01-title.** No top band. The Rail: `.acm-rail` on the hero block, the hero block being the whole content box (x 96 to 1824, y 96 to 984). Rail is a solid bar in `--acm-primary`, 40 px wide, at x 96, full block height y 96 to 984, drawn with the exact `::before` construction from `slide-rules.md` §3 with `--acm-rail-break` unset (200% fallback, solid; no `data-pillar` anywhere). Content starts at x 184 (rail 40 + gutter 48). Eyebrow "FALL 2026" ledger at (184, 96). `<p class="name">` "ACM @ RCC" name role 200 at y 200 (box to 400). `<h1>` "First meeting" title role 96 at y 448 (box to 556). Two label-role lines: "Thursdays, 12:50 to 1:50 PM" at y 620 inside `<time datetime="2026-09-03T12:50">`, and "BLCIS A-210" at y 688; the time line at weight 500, the room at 400 (the bold clause carries the date, per the hero rule). Right column: QR 480 x 480 at (1248, 324) on a white quiet-zone square with a 1 px `--acm-outline` frame, `role="img" aria-label="QR code for https://discord.gg/fM2HbsJyBG"`, modules in on-surface; "discord.gg/fM2HbsJyBG" in the url role centred beneath at y 836. Caption band: "instagram.com/rcc.acm" in the url role at (184, 896). No callout. Counter omitted on this slide.

**s02-board.** Eyebrow "THURSDAY, SEP 3". Title "The next four weeks". A `<dl>` of five rows from y 324, row height 80, hairline under rows 1 to 4: `<dt>` in the label role, weight 500, in a 300 px column ("Today", "Sep 10", "Sep 17", "Sep 24", "Club Rush"); `<dd>` at lead 48 / 64 on the same line. Ends y 724. "[TBD]" is literal text. No callout, no caption.

**s03-sentence.** Top band holds only the counter. The sentence is the `<h2>` at display 136 / 143, `max-width: 20ch`, left at x 96, vertically centred between y 160 and y 880 (four lines: "Where RCC students / who want to get good / at computing / practice together."). Caption band: "Chartered under ACM, the professional association for computing." caption role, not uppercased. No callout.

**s04-pillars.** Eyebrow "FALL 2026". Title "Four pillars". A `<dl>` as a 2 x 2 grid: cells at x 96 and x 972 (852 wide), rows at y 324 and y 588. `<dt>` pillar name at dense title 76 / 96; `<dd>` at body 40 / 56, two lines. No hue, no boxes. Ends by y 812. No callout.

**s05-proof.** Eyebrow "COMPETE". Title "Proof". Three columns at x 96, 680, 1264 (560 wide) from y 324: numeral-xl 224 ("2000", "1998", "11"), then the label at body 40 / 48 in variant ink from y 572 (the third label wraps to two lines, ends y 668). Markup `<dl>`. No callout.

**s06-what-you-get.** Eyebrow "FALL 2026". Title "What you get". `<ul>` of four lines at lead 48 / 64 with 24 px gaps from y 324 to y 652. Note callout at y 700: fill `--acm-surface-container-high`, ink on-surface, inset 1 px `--acm-outline` hairline, radius 16, padding 24 block and 48 inline, no Rail; "Note:" at 700 then "Any major, any level. Nobody gets screened at the door." on the same line at body 40 / 64. Ends y 812.

**s07-shape.** Eyebrow "FALL 2026". Title "Fifteen Thursdays". `<dl>` of five rows at 64 each from y 324: `<dt>` the count in a 132 px column at label 44, weight 500, tabular; `<dd>` at lead 48 / 64. Ends y 644. Note callout at y 692, two lines: "Note: Every regular meeting opens with a 15-minute contest problem. The warm-up lead rotates." Ends y 868. No caption.

**s08-dates.** Eyebrow "FALL 2026". Title "The dates". Two `<dl>` ledgers side by side: left x 96 to 948 holds Sep 3 through Oct 22 (eight rows), right x 972 to 1824 holds Oct 29 through Dec 10 (seven rows). Rows are one line, 64 tall, hairline under each: `<dt>` date in the label role (44, weight 500, tabular, `<time>`) in a 200 px column, then `<dd>` at body 40 / 56. Rows run y 324 to 836 (left) and y 324 to 772 (right). Lab days and the showcase set the `<dd>` at weight 500; Nov 26 sets both parts in variant ink. No colour on any row. Cell text exactly as the deck copy's grid (e.g. "Today: kickoff", "Lab day 1", "Career: resume, transfer", "No class", "Showcase"). Caption band: "Lab days depend on today's order. ICPC dates follow the season calendar once it is published." No callout.

**s09-lab.** Eyebrow "BUILD". Title "Six lab days". Lead line at lead 48 / 64 from y 324: "Four stations on a Pico 2 W, one per tier, 30 minutes each." Tier `<dl>` in four quarters (414 wide, 24 gutters) from y 436: `<dt>` "T0" to "T3" in the label role, weight 500; `<dd>` at body 40 / 56, two lines ("Never written code. MicroPython", "CIS-5. Arduino C++", "CIS-17A. Arduino C++", "CIS-17B/C. Arduino C++"); a 1 px `--acm-outline-variant` rule under the strip at y 620. Nothing else on screen; the three station names are spoken (they stay in the notes). Caption band: "Same board and same pin map at every station. The same build comes back at a higher tier." No callout.

**s10-money.** Eyebrow "BUILD". Title "The money". `<dl>` as a 2 x 2 grid of 852 px cells from y 324, row gap 40: figure at display 136 / 143, tabular, on-surface; label beneath at body 40 / 48 in variant ink ("cap", "base order", "max order", "restock reserve, held until after lab day 2"; the last wraps to two lines). Row 1 y 324 to 515, row 2 y 555 to 794. Caption band, two lines: "Both totals include 8.75% tax and a shipping estimate. Six station kits plus spares." then "Code and wiring: github.com/Sam-T-G/rcc-acm-microcontroller-lab" with the URL in the url role. No callout. No colour on any figure.

**s11-decision.** Eyebrow "BUILD". Title "Order today, or lab day one moves". Title wraps to two lines (box y 184 to 400); body from y 432: `<ul>` of three lines at body 40 / 56 with 12 px gaps (the third wraps), ends y 664. Warning callout at y 704: fill `--acm-primary-container`, ink `--acm-on-primary-container`, inset 1 px `--acm-outline` hairline, radius 16, a 20 px short Rail in `currentColor` at the inline-start edge (clipped by `overflow: hidden`), padding 24 block, 48 inline-end, 68 inline-start; "Warning:" at 700 then "Hands today are a count, not a binding vote. The spend needs advisor sign-off before anyone orders." two lines at body 40 / 56. Ends y 864. No caption.

**s12-seats.** Eyebrow "CONNECT". Title "Six seats, all open". Visible `<caption>` sentence at body 40 / 56 at y 324: "Two names for each job, one person holds both." Table from y 404: header row 56 tall on `--acm-surface-container-high`, table-head role, columns "RCC title" (400), "ACM title" (400), "What it costs per week" (928); six rows at 64 (cells 40 / 56, padding 4 block 16 inline), a `--acm-outline-variant` rule under each row, no vertical rules, `scope="col"` on every `th`. Table ends y 844. Caption band, one line: "Chair, Vice Chair, and Treasurer hold ACM Student Membership: $19 a year." No callout on this slide.

**s12b-icc.** Eyebrow "CONNECT". Title "Six seats, all open" (a continuation slide, same title). One body line at lead 48 / 64 at y 324: "ICC Representative: Mondays 9:30 AM, Bradshaw Center." Warning callout at y 420, same anatomy as s11: "Warning: ICC Representative is every Monday at 9:30 AM. Three absences and the club loses its standing." Ends y 580. No caption. Speaker notes: the ICC lines from the s12 notes.

**s13-jobs.** Eyebrow "CONNECT". Title "Four more jobs". Visible `<caption>` sentence at y 324: "These are not officer seats." Table from y 404: header row 56 ("Job" 560, "What it costs" 1168), four rows at 64. Ends y 716. Note callout at y 764, one line: "Note: Warm-up lead is the best first task." Ends y 876. No caption band text.

**s14-on-ramp.** Eyebrow "CONNECT". Title "The on-ramp". `<ol>` of four rungs at dense title 76 / 96 from y 324 with 24 px gaps, the numeral in the label role (44, 500, tabular) in a 120 px column: "Run one 15-minute warm-up problem" / "Back up a lab day. Hand out kits" / "Take notes at one meeting" / "Then an officer seat". Ends y 780. No callout, no caption.

**s15-questions.** Eyebrow "FALL 2026". Title "Questions". Two lines at lead 48 / 64 from y 324: "The sheet going around: name, email, what you are interested in." / "Officer seat, lab, ICPC, hackathon, just meetings." Ends y 516. Note callout at y 580, two lines: "Note: The sheet does not go online. Names are published only with written consent." Ends y 756.

**s16-ask.** Eyebrow "NEXT THURSDAY, SEP 10". Title "Join the Discord". Left: QR 560 x 560 at (96, 324) on a white quiet-zone square with the outline frame, same aria as s01; "discord.gg/fM2HbsJyBG" in the url role centred beneath at y 900 inside the caption band's left half. Right column x 972 to 1824: the sentence at lead 48 / 64 from y 324: "Sep 10, same room, same time: ICPC. What the contest is, how teams form, how registration works." (three lines, ends y 516). Check callout at y 572: fill `--acm-live-container`, ink `--acm-on-live-container`, short Rail as on Warning, "Check:" at 700 then "join before you leave the room. Everything else gets followed up there." two lines, ends y 748. Caption band right half, one line right-aligned to x 1824: "ACM @ RCC · instagram.com/rcc.acm" with the name in Inter caption role at weight 500 and the handle in the url role. The club name is real text.

## 9. Accessibility

- Every control keyboard reachable; visible 2 px `--acm-focus-ring` outline, 4 px offset.
- Inactive slides `aria-hidden="true"` and `inert`. Notes and overview `hidden` until toggled.
- The Rail pseudo-element is invisible to AT by construction; the QR `<svg>` has `role="img"` and an `aria-label` naming the URL, and the URL is printed as text beside it.
- `<output aria-live="polite">` counter announces "07 / 17"; the active `<h2>` receives focus on change.
- Contrast pairs (from the token sheet): on-surface on surface 16.2:1; on-surface-variant on surface 6.59:1; primary on surface 6.13:1; on-primary-container on primary-container 9.56:1; on-live-container on live-container 10.05:1.
- Nothing relies on colour alone; every emphasis is also weight or a word.
- Real text everywhere; sentence case everywhere except proper names and the uppercase ledger role.

## 10. Pre-flight checklist (tick before returning)

- [ ] One Rail, on s01 only, solid, 40 px, x 96, y 96 to 984, never rounded; short Rails only on Warning and Check callouts, one callout per slide
- [ ] No `#0182ac`, no gradient other than the Rail's own construction, no Google four, no `{}` or `<>` glyphs, no diamond, no photos
- [ ] Inter and JetBrains Mono only, via the Google Fonts link; `font-optical-sizing: auto`; no `font-variation-settings`; no `-webkit-font-smoothing` on body
- [ ] No hue on any meeting type, tier, pillar, or date
- [ ] Every visible text at or above 40 px except the caption (36), the ledger eyebrow and counter (32), and the notes layer (36)
- [ ] Every text box inside the 96 px margins on every slide (run `render.py` and read `audit.md`)
- [ ] "ACM @ RCC" as real text on s01 and s16; "[TBD]" literal on s02
- [ ] 17 sections with exactly these ids in order: s01-title, s02-board, s03-sentence, s04-pillars, s05-proof, s06-what-you-get, s07-shape, s08-dates, s09-lab, s10-money, s11-decision, s12-seats, s12b-icc, s13-jobs, s14-on-ramp, s15-questions, s16-ask
- [ ] Hash routing, key map, click zones, swipe, fullscreen, N, O, Escape all working; zero console errors
- [ ] No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`; no external resource except fonts.googleapis.com

## 11. Deliberate differences from deck-copy.md

- s01 `<h1>` is "First meeting" (the club name is the display line above it; the year is in the eyebrow), so the h1 is a sentence-case meeting title with no digits.
- s09 title is "Six lab days"; the board moves into the lead line. The three station names come off the screen and stay in the notes.
- s11 title spells "one" so the heading carries no digit.
- s12 gains a visible caption sentence and loses its Warning to the continuation slide s12b, which carries one body line restating the ICC row. s13 gains a visible caption sentence. Both sentences are lifted from the deck copy's own notes.
- Deck is 17 slides.
- Review deviations recorded 2026-09-03 (rule over spec where they conflict):
  - s01: the QR sits at stage x 1344, not 1248, because the name line "ACM @ RCC" ends at x 1304; its right edge lands on the 1824 margin and the url is centred beneath it.
  - s16: the QR is 555 x 555 (37 modules x 15 px, integer pitch), 5 px under the spec's 560, so it ends at y 879 and the hairline at y 880 spans the full width.
  - s16: the club name in the sign line is set at the body role (500, 40 / 48), not the 36 px caption role, per the 40 px body floor (slide-rules.md MUST 4, MUST 20).
  - s16: a freshness stamp "Updated 2026-09-03" in the ledger role sits right-aligned at y 808 above the bottom hairline (slide-rules.md MUST 39).
  - s12, s13: table header cells are 40 / 48, not 36, per the 40 px body floor; the header row stays 56.
  - s11, s12b: the Warning body is 40 / 56 (a role on the sheet), so the callouts end at y 864 and y 580.
  - Focus: the programmatic heading focus hides its outline only under `:focus:not(:focus-visible)`; keyboard-visible focus on the heading and every button uses the shipped ring (3 px transparent outline, 2 px offset, 2 px surface gap plus 3 px `--acm-focus-ring` box-shadow), not a 2 px outline (slide-rules.md MUST 53, NEVER 60).

## 12. Known [TBD]s that must stay [TBD] in the deck

Club Rush dates ("Club Rush: mid September, dates [TBD]" on s02). Nothing else on screen is [TBD]; the presenter's do-not-say list is in `deck-copy.md` §4 and belongs in the notes for s08 and s14 verbatim.
