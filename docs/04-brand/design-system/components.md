# Components and page archetypes

Every component resolves against the tokens in [tokens.css](tokens.css). Nothing names a bare color. Every fill role has a paired foreground role, which is why a component drops into a light section, a dark section, or a re-themed event page without a variant.

## 7. Components

Every component below resolves against the tokens in §6. Nothing names a bare color.

## 7.1 Rules that apply to everything

**Depth is tone, then hairline, then shadow.** Separation comes from a step on the surface container ladder. If tone alone will not carry it, add a 1px `--acm-outline-variant` hairline. Shadow is for an element over busy content and for interaction.

**One state layer, in the content's own color.** Hover 8%, focus and pressed 10%, table row hover 4%, dragged 16%. Because the layer takes the content's color, hover reads as more of what is already there and needs no per-theme tuning.

**Focus is a shadow plus a transparent outline.** The shadow gives the ring; the transparent `outline` is what forced-colors mode substitutes a system color into, because box-shadow is dropped there. `:focus-visible` only. A box-shadow ring is clipped by an ancestor with `overflow: hidden`, so any card that clips its media puts the ring on the card and not on an inner element.

**Visual size and hit size are separate.** A control may be 40px tall and look right; its target is 48px, extended with padding or a pseudo-element.

**Radius by footprint. Pills mean actions.** If a container is fully rounded it reads as a control and someone will click it.

**Nested corners get the subtraction.** Inner radius equals outer radius minus the padding between them.

**Every component works with no JavaScript.** Tab panels stay in the DOM with real headings. Disclosure widgets are `<details>`. Nothing carrying content hides behind a hover.

**Both renderings are first-class.** The markdown source is the artifact of record; the HTML page is a rendering of it. No component may depend on markup GitHub strips. Each component below carries a **GitHub form**. A component with no honest GitHub form does not go in a doc.

**One accent per component instance.** At most one of the four hues per instance, and never a row of components cycling through them. Orange and red never share a component (§2.3): a failure state is told by its label or icon, never by hue alone.

**ACM Blue appears nowhere in a component.** It lives inside the ACM chapter logo file, once one exists, and that file is placed unaltered (§1.5). A blue that is not `--acm-secondary` on a club page is a defect.

## 7.2 Buttons

Three treatments.

| Treatment | Fill | Ring | Use |
|---|---|---|---|
| Primary | `--acm-primary` / `--acm-on-primary` | none | One per view. The action the page exists for. |
| Secondary | transparent / `--acm-on-surface` | `--acm-outline` | Everything else that is a real action. |
| Text | transparent / `--acm-primary` | none | Inline and tertiary. Never beside a Primary. |

**Anatomy.** Label, optional leading icon, optional trailing icon. Label is `label-lg` at line-height 1 so the box is a clean multiple. Icons are 20px in `md`, 24px in `lg`.

**Sizing.** Height 32 / 40 / 48. Horizontal padding 24px on the label side and 20px on any icon side. That 4px optical reduction is real: an icon fills its box more than a letterform does.

The Secondary ring is `box-shadow`, not `border`, so a Primary and a Secondary of the same height measure identically with no padding compensation.

**States.** Rest. Hover: state layer 8%, no lift and no color swap. Focus-visible: ring stacked outside the Secondary's 1px ring. Pressed: radius morphs from full to `--acm-radius-sm` on the spatial-fast track, state layer 10%. Disabled: 38% opacity on a designed pair. Loading: label stays at reduced opacity with a spinner in the leading slot; the button never changes width.

**Press feedback is a shape change, not a dim.** Compressing the corner reads as physical, costs one rule, survives dark mode, and needs no second color token.

**Raw-fill variant, for posters and share cards only.** A button drawn in `--acm-fill-orange` takes an ink label (`--acm-on-surface`), never a white one; white on the raw orange measures below the body floor (§2.1). On a web page the Primary treatment above is the only filled button.

**GitHub form.** A link. Button labels are written to survive being a plain link: verb-first, naming the action. "Come Thursday at 12:50", not "Learn more".

## 7.3 Card

The generic container. Station card, officer card, and stat tile are specializations.

**Anatomy.** Optional media band flush to the top edge, then a content well: title, optional supporting line, optional metadata row, optional action row pinned to the bottom.

**Sizing.** `--acm-radius-md` for a grid card, `--acm-radius-lg` for a feature card, `--acm-radius-xl` for a page-level container. Content well padding 16px on a list card, 24px on a feature card. Grid gap 24px. Media band is a fixed height on desktop with `object-fit: cover`; in a single-column mobile layout it goes to `height: auto`, because uniform card heights only exist to serve a grid.

**States.** Rest: `--acm-surface-container-lowest` on the tinted ground, with an `--acm-outline-variant` hairline. Hover: `--acm-elevation-1` and a 2px lift. Focus-visible: ring on the whole card. Status (live, current, changed): the hairline goes to `--acm-outline` and the card gains a labeled chip. The information hierarchy is identical in every state, so a live card and a resting card scan the same.

**Draw the hairline as an `::after` with `border-radius: inherit`, not as a `border`.** The media band can then bleed edge to edge under `overflow: hidden` while the hairline sits crisply on top.

**Whole-card click without nesting interactive elements.** An absolutely positioned transparent `<a>` at `inset: 0; z-index: 1` covers the card; real controls sit at `z-index: 9` above it.

**Responsive.** `container-type: inline-size`, so one component works in a 2-up and a 4-up with no size variants.

**GitHub form.** A level-3 heading, a one-line description, and a metadata line. A card grid becomes a table only when each row carries three or more pieces of data.

## 7.4 Meeting page and station card

The club's two signature documents, and the ones that have to be excellent in both renderings. Every Thursday is one row of the semester's meeting plan; every lab day is four station cards, one per tier. The two share one discipline: a fixed section grammar, a facts table at the top, and a check at the end.

### The meeting page

The fixed spine comes from the [weekly meeting playbook](../../03-playbooks/weekly-meeting.md). The order never varies.

1. H1 with the date and the format ("2026-10-01 Problem session")
2. Facts table: Format, Pillar, Main block, Owner (role), Room, Warm-up lead (role)
3. Announcements (the Board, five minutes; every dated thing in the next four weeks, one line each)
4. Main block, one section, forty minutes
5. Wrap: next week, who is leading, one ask
6. Record: headcount, decisions, action items

The grammar is the payload. GitHub generates heading anchors from headings, so a stable grammar makes `…/meetings/2026-10-01.md#wrap` a working deep link on every meeting forever, and an officer who has read one page can navigate any other by muscle memory. The semester's meeting plan (`semesters/2026-fall/meeting-plan.md`, which lives on the unmerged `meeting-structure` branch as of 2026-09-01, so it is named here and not linked) is the index of these pages; the meeting type (regular, lab day, showcase, no class) lives in that table, never in the page, so a page file is never edited to change its type.

**The pillar sets the Rail.** Problem session is Compete, build session is Build, mini-talk is Learn, open floor is Connect (the format table in the playbook). The page's root element carries `data-pillar`, and the Break in the Rail moves ([accessibility.md](accessibility.md) §2.4). Meeting types and pillars get no hue.

### The station card

The grammar comes from the lab repo's card template and it is the lab repo's to change; this system owns only how a card renders and prints. The order, per that template:

1. H1 with the challenge title
2. Facts table: Tier, Time, Language, Parts, Builds, Prereqs
3. Why this matters
4. What you will build
5. Before the student sits down (facilitator)
6. Steps
7. Stretch goals
8. Check for understanding (60 seconds)
9. Common bugs
10. Solution notes
11. Sources

**Facts table.** Two-column key-value. A key with no value says `none` or `[TBD]` and never disappears, because a missing row and an empty row read the same to a facilitator scanning at 12:49 PM.

**The check is the Check callout.** "Check for understanding (60 seconds)" is the one section a facilitator reads out loud, and it renders as the Check callout (§7.7) with the question and the good answer inside it. On GitHub it is the section heading and its paragraph, which is what the cards already are. Nothing else on a card becomes a callout; the Common bugs table stays a table.

**Steps render as agenda rows.** Each numbered step carries a TODO number, a hint, and a "works when" line. On the web it is the timeline row (§7.12) with the TODO number in the leading column instead of a clock time. Steps 1 and 2 must be reachable in the first ten minutes, and the rendering does not hide that: the first two rows carry the emphasized tier on a lab day page while the station is live.

**Print form.** Cards are printed and laminated, station letter and pin table on both sides, per the lab's facilitator guide. The print layout is in [assets.md](assets.md); the rule that lives here is that the printed card and the rendered page share section order and heading text exactly, so a facilitator who reads one can find the same line in the other.

### The read-aloud block

Two documents carry lines an officer says verbatim: the Club Rush pitch in the [club rush playbook](../../03-playbooks/club-rush.md) and the facilitator's lines on a station card. They are their own block type. Left Rail in `--acm-primary` at `--acm-space-2`, `body-lg`, `--acm-on-surface`, 16px inline-start padding. It is the one block a person reads verbatim, so it stays at full body size while everything around it may compress. Markdown form is a blockquote, which is what the pitch already is.

**On the web the card is a page, not a tile.** `--acm-surface` article column on a `--acm-surface-container` page ground, so the document reads as an object on a desk. Reading column caps at `--acm-container-prose`. The 2:1 heading rhythm does all the sectioning with no rules and no boxes.

**States.** Upcoming, current, past. State lives in the meeting plan or the lab day's index, never in the card.

**GitHub form.** Native. Add a horizontal rule after the facts table so the fold on a phone lands after the table rather than mid-table.

## 7.5 Badges and chips

| Kind | Encodes | Interactive |
|---|---|---|
| Tier chip | `T0`, `T1`, `T2`, `T3` | Yes, as a filter on a lab day page |
| Type chip | regular, lab day, showcase | Yes, as a filter on the meeting plan |
| Pillar chip | Build, Compete, Learn, Connect | Yes, as a filter |
| Role chip | Chair, Vice Chair, Treasurer, Lab lead, Advisor | No |
| Status badge | room confirmed, kit ordered, `[TBD]` | No |

**Anatomy.** Optional 20px leading icon, label, optional trailing dismiss. Tier and role chips carry no icon and are set in the ledger line, because a tier is a token rather than a word.

**Sizing.** Height 28 inside a table cell or heading, 32 standalone, 40 as a filter control. Padding 6px / 16px. `--acm-radius-full`. Label `label-md`.

**No chip carries a hue.** Every chip in the set uses `--acm-surface-container-high` with an `--acm-outline` hairline, and the selected state fills with `--acm-primary-container`. Tiers are told apart by their tokens, pillars by their words and by the Rail's Break ([accessibility.md](accessibility.md) §2.4). A four-tier color scheme would put four hues on one lab day page and fail check 2 in §2.3 four times.

**Filter chips are real form controls**: a visually hidden `<input type="checkbox">` with a `<label>`, so keyboard traversal and screen-reader announcement come free. Never a `<div>` with a click handler.

**A selected filter chip changes fill and ring together**, never fill alone.

**Elevation differs by ground.** On light, a chip carries a real two-layer shadow and a light fill. On dark, no shadow at all, and it separates by taking a lighter fill than the surface behind it. Shadow does nothing on a near-black surface and a value step does nothing on white.

**GitHub form.** Tier and role chips are inline code (`` `T2` ``, `` `Lab lead` ``), the one styled span GitHub gives for free, and the lab repo already does this. Type and pillar chips become plain words in the facts table. Status badges become a `[TBD]` marker or a task-list checkbox. Never shields.io images; they are network dependencies for text.

## 7.6 Tables

The club's densest surface. The meeting plan, the budget, the kit inventory, the pin map, and the Common bugs table are all tables, read on phones and at a lab bench.

**When to use one.** One piece of data per item is a list. Two related pieces is a description list. Three or more is a table. A one-column table is a list that has not been rewritten yet. Every table is preceded by a complete introductory sentence, not a fragment the table completes.

**Styling.** Horizontal rules only. Tinted header row on `--acm-surface-container-high`, `label-lg` heads, sentence case, no terminal punctuation. Body cells at `body-md`, one step below the surrounding prose, with a single `--acm-outline-variant` rule under each row. No vertical rules, no zebra striping, and no merged cells: a merged cell breaks screen-reader traversal and breaks in markdown.

**Sizing.** Cell padding 8px, deliberately tighter than the 16px prose rhythm so the table compresses into a distinct object. `<th scope="col">` on the header row, `<th scope="row">` on a first-column label.

**Numerals.** Every column of numbers, times, dollar amounts, pin numbers, or attendance counts is `tabular-nums`. Every number the club publishes changes.

**Wide table on a narrow screen.** Pin the first column with `position: sticky; inset-inline-start: 0` inside `.acm-table-scroll`, and add a trailing spacer whose width equals the page margin. Without the spacer the last column scrolls flush against the viewport edge and looks clipped.

**States.** Rest, row hover (state layer 4%), sorted column (arrow glyph plus `aria-sort`), empty (one full-width cell with a sentence saying what would appear and what to do about it, never a blank table).

**GitHub form.** Native GFM. Sentence-case heads, no terminal punctuation, no merged cells, the introductory sentence, and the three-or-more rule all survive. Alignment colons only for right-aligning numeric columns.

## 7.7 Callouts

A closed set of three. Nothing else becomes a callout.

| Type | Meaning | Color | GFM alert |
|---|---|---|---|
| Note | Useful, not critical to the task at hand. | Neutral (`surface-container-high`) | `> [!NOTE]` |
| Warning | Do not do this, or it cannot be undone. Money, safety, privacy, a room booking, a pin map change. | `primary-container` | `> [!WARNING]` |
| Check | The 60-second check for understanding, or the one concrete ask a meeting ends with. | `live-container` | `> [!IMPORTANT]` with a bold `Check:` lead-in |

Note is neutral on purpose. It is the most common type, and making it neutral means a doc page carries at most two hues plus grey. Warning takes the primary container because orange is both the caution convention and the club's hue, so a warning adds no second hue to a page. Red is not a callout color: `error` stays a UI state so it keeps its meaning, and it would sit 14 degrees from the Warning's orange.

Check is the club's own type. Every station card ends with a 60-second question that tests the idea rather than the syntax, and every weekly meeting ends with one concrete ask. Both are the thing a person leaves the room holding, and both get the same block.

**Anatomy.** A short Rail as the inline-start edge (the only place the Rail repeats on a page, [accessibility.md](accessibility.md) §2.4), a bold inline label ending in a colon, then the body on the same line. No separate title row and no icon column; the label and the tint carry the meaning. Padding is lopsided: 12px block, 20px inline-end, and an inline-start value equal to the gutter plus the Rail width. Body at `body-md`.

**Every callout carries an `--acm-outline` hairline**, because container fills measure between 1.10:1 and 1.22:1 against the ground (§2.5) and a boundary that carries meaning needs 3:1.

**The admission test is the spec.** All three conditions must hold: the information is relevant but not necessary to the current task, the interruption does not obstruct the reader's progress, and the content does not flow from the sentence before it. Named non-uses: cross-references, prerequisites, procedural steps, and anything critical to succeeding. Most callout systems specify the appearance and let authors decide the usage, which is backwards.

**Scarcity is part of the spec.** Two callouts never sit adjacent. A page with more than three loses the distinctiveness that makes the tint mean anything. If a station card needs four warnings, they belong in Common bugs as rows. [documents.md](documents.md) sets the authoring ceiling at two per file; that is the same rule at the altitude of a single markdown document, and the three here is the ceiling for a built page that may render more than one source.

**GitHub form.** GFM alerts render natively with their own icon and color, so all three survive. The set is capped at three to keep parity with what GitHub shows. `TIP` and `CAUTION` are banned so the three keep their distinctiveness.

## 7.8 Navigation

**Header.** 36px content box with 12px block padding, background at about 85% alpha over `--acm-surface` with `backdrop-filter: blur(5px)`. Left: the club name as text in `title-lg`, or the ACM chapter lockup at a fixed pixel size once one exists, unaltered. Center or right: five section links maximum. Far right: one Primary button.

**Two link colors in one bar.** Navigational items (Meetings, Lab, Playbooks) take `--acm-on-surface-variant`. Transactional items (Join, Email us) take `--acm-primary`. Priority is encoded in color, so the bar stays visually flat with no weight or size changes.

**Until a chapter logo exists, the header carries the club name as text.** No placeholder mark, no Rail in the logo slot; the Rail is a page device and never a logo ([accessibility.md](accessibility.md) §2.4).

**Skip link.** First element in `<body>`, visually hidden until `:focus`, at which point it becomes a real centered Primary button.

**Side nav** (docs and playbooks). 260 to 270px fixed, filter input at 32px, nested collapsible lists. The scrolling list fades at its bottom edge with `mask-image` over a 64px zone rather than being hard-cropped, so a partially visible item reads as "more below".

**On this page rail.** Flat list of the H2 and H3 outline, set in the ledger line so it reads as furniture. Active item gains weight 500 and `--acm-primary`.

**Dropdown panels lead with a sentence and an escape hatch**, never a bare link list. "Every station card, with the starter and the solution." followed by "See all challenges". A truncated list always ends with the escape hatch.

**Named landmarks.** `aria-label` on every nav region: "Primary", "Section", "On this page", "Footer".

**Carry the active and hover state entirely on a pseudo-element** so the link's own box is never touched. Text then cannot shift by a subpixel between rest, hover, and current, which is the flicker that makes most nav bars feel cheap under the cursor.

**GitHub form.** The repo's existing pattern is correct: a relative-link table at the top of each README, breadcrumb links back to the parent, and every folder README listing its children with a one-line predicate sentence per entry.

## 7.9 Hero

**Anatomy, one column, nothing in the margins.** The Rail on the inline-start edge, eyebrow in the ledger line (pillar name, date, or "Fall 2026"), H1, one-line subhead, a pair of buttons, an optional announcement pill. Five elements plus the Rail.

**Two buttons.** One self-serve, one that reaches a person: "Join the Discord" beside "Email an officer". One button leaves out half the audience; three has no primary action.

**The announcement pill** takes the slot where a third button would go and is styled as a message: pale tinted field, full radius, `label-md`, bolded lead-in, plain-weight explainer, small filled arrow at the end. It gives the page one "what's new" hook without a competing action.

**Sizing.** H1 at `display-sm` on mobile reaching `display-lg` at the widest breakpoint. The subhead does not scale. The subhead bolds its last clause only, and that clause carries the date or the ask: "Thursdays at 12:50 in A-210. **Lab day 1 is September 24.**"

**Media is optional and the default hero has none.** Type, the Rail, and two buttons on `--acm-surface` is a finished hero. When there is a photo, the scrim is two-ended: dark at the top where the headline sits, clear across the middle two-thirds so the image reads, dark again at the bottom. A flat overlay protects the text by destroying the photograph.

**The Rail is the hero's only decoration.** Its Break carries the pillar; the pillar name is in the eyebrow. Once per screen: a page with a hero Rail has no second Rail until a callout.

**States: none.** The hero is static. Decorative glyphs are `aria-hidden="true"` with `alt=""` and hidden below the tablet breakpoint.

**GitHub form.** H1, one italic subhead line, a blank line, a short link row. No Rail; GitHub already draws its hairline under the H1.

## 7.10 Footer

**Anatomy, in order.**

1. Three-door closer
2. Link columns: the repo, the Discord, Instagram, the website, the code of conduct
3. ASRCC credit, where ASRCC funded the page's event
4. Freshness stamp

**End every long page with the same three doors** rather than one CTA: **Come Thursday at 12:50 in A-210**, **Join the Discord**, **Read the playbooks**. One CTA loses whichever half of the audience is not in that posture right now.

**There is no disclaimer block.** ACM's chapter policy requires that the chapter not present itself as speaking for ACM; it does not prescribe a sentence. The requirement on a public page is the club name written as [brand.md](../brand.md) writes it, and the ASRCC line wherever ASRCC paid. Do not invent a disclaimer sentence; a made-up compliance line reads as one and teaches the next officer team to trust it.

**The ASRCC credit is a required slot with a `required` flag when the funding source is ASRCC**, not optional copy. "Funded by ASRCC" (or the wording Student Activities asks for), at `body-md` in `--acm-on-surface-variant`, inside `role="contentinfo"`, never inside a collapsed `<details>`.

**Freshness stamp.** Every page and every doc carries a last-updated date. Staleness is the reader's information, and a stale stamp is a maintenance ticket.

**GitHub form.** A horizontal rule, the three-door line, the ASRCC line if funded, and the date.

## 7.11 Code blocks

The club writes real code. Every station card ships a starter and a solution in Arduino C++ or MicroPython, and the lab's setup doc carries multi-line shell and Python. The component is sized for a twenty-line starter, and the single-command case falls out of it.

**Sizing.** `min-height` 52px, `--acm-radius-sm`, `--acm-code-surface` fill, 1px `--acm-outline-variant` ring. Padding `14px 48px 14px 16px`. The 48px inline-end exists so the absolutely positioned copy button can never overlap the longest line.

**Compute the top padding as `max(normal-padding, button-size)`.** Any container with an absolutely positioned control in a corner should do this, so the control cannot collide with the first line no matter how the block is configured. It generalizes to every card with a corner action.

**Header variant, the default for a starter file.** A 32px header row carries the filename and the language in the ledger line, with the copy button at its inline-end. A student needs to know which file they are looking at before they read it. The no-header variant (a single shell command) moves the copy button to `top: 50%; transform: translateY(-50%)` so the command sits optically centered.

**Copy button.** 32×32, transparent, `--acm-radius-xs`, an icon glyph so it inherits color, `translate="no"`. The copyable string lives in a `data-clean-code` attribute on the container rather than being read off the highlighted DOM, so the clipboard never picks up markup.

**Line numbers on anything over ten lines**, in `--acm-on-surface-variant`, set as a CSS counter on a pseudo-element so they never enter the clipboard. A facilitator says "line 14" across a lab bench.

**Ligatures are off** on every code element (§3.6), so `->` and `!=` render as the characters a student types. Teaching material shows what the keyboard produces.

**Wrapping.** `text-wrap: wrap` on a single-line command so it wraps rather than forcing the page into horizontal scroll. Multi-line blocks scroll inside their own `overflow-x: auto`; a wrapped line of C++ is worse than a scrollbar.

**Syntax color.** Every token color in the highlighting theme must clear 4.5:1 against `--acm-code-surface`, comments included, in both themes. Measure before shipping a theme; comments are the usual failure.

**States.** Rest, hover, copied (glyph swaps to a check for the effects-slow duration; the button never changes width).

**GitHub form.** A fenced block with a language tag (`cpp`, `python`, `sh`). GitHub supplies its own copy button at the top right, so the HTML rendering puts its copy affordance in the same place to avoid teaching two habits.

## 7.12 Timeline and agenda rows

The spine of every meeting page, every station card's Steps section, and the showcase run of show. A row is one block: `13:00 Main block (40 min)`.

**Anatomy.** Fixed-width leading column, block name, duration chip, block body. On the web the row is a grid with the leading track at 5.5ch, wide enough for `12:00` plus a space so nothing reflows between a one-digit and two-digit hour. A station card's Steps use the same row with `TODO 2` in the leading column. In markdown it is a table row (the playbook's default agenda) or a numbered step (the card), which is what the files already are.

**Rows are separated by `:not(:last-child)::after`**, so the last row has no trailing line and there is no negative-margin hack to remove one.

**The clock is derived.** Every row's start equals the previous row's start plus its duration. In HTML the times are computed; in markdown they are written by hand, so **`scripts/check.sh` should verify that the default agenda, each meeting page's agenda, and the showcase run of show are consistent with their durations and end at 1:50 PM.** A table whose clock does not add up is a bug and nothing currently catches it.

**States.** Past, current, next, over-running. Current is marked by the emphasized type tier and by the `--acm-outline` hairline, never by a badge. The emphasized tier changes weight at identical size, so it cannot reflow the agenda while someone is reading it.

**Formats carry promises.** Every row on a public agenda states its length. Every meeting states its format and its pillar. A reader should be able to tell from the label alone whether they are about to solve problems, build something, hear a talk, or plan.

**GitHub form.** Native. The three-column table (Time, Block, Notes) exactly as the weekly meeting playbook writes it, and the showcase's two-column run of show. A public agenda variant is the same three columns with the notes column carrying what a member should bring.

## 7.13 Officer cards

The privacy policy is load-bearing: a person's name appears only where written consent is on file, and otherwise the row reads `on file with advisor`. The no-name, no-photo state is the default state and it has to be designed.

**Anatomy.** Square avatar, name or role token, role line, optional "runs" line (which meetings or stations this role owns this term).

**Sizing.** `--acm-radius-lg` container on `--acm-surface-container`, 16px padding, avatar at `aspect-ratio: 1` with `object-fit: cover` and `--acm-radius-md`, 16px below it, then the name at `title-lg` and the role at `body-md` in `--acm-on-surface-variant`. The role steps down by color rather than by weight, so the two lines keep one optical texture.

**Photo source is square at two crops, 400×400 and 165×165.** Enforcing square at upload is what keeps the grid rhythm; cropping in CSS at render time does not.

**States.** Named-with-photo, named-without-photo, unnamed. The unnamed state shows the role token in the avatar slot on `--acm-primary-container`, with `Held by an officer, name on file with the advisor` as the role line. It is a complete card rather than a gap.

**No accent cycling.** Every officer card uses the same `--acm-primary-container` avatar fill, because a row of cards cycling hues is the composition §2.3 rules out. Roles are told apart by their tokens.

**Roles, not seats.** The club names its roles by title (Chair, Vice Chair, Treasurer, Secretary, ICC Representative, Communications lead, Lab lead, Event lead, Advisor), per [officer-roles.md](../../00-charter/officer-roles.md). One table per semester maps role to person, in the roster, with consent.

**GitHub form.** A table: Role, Held by, Runs, Backs up. The semester `roster.md` is the source and it is correct.

---

## 8. Page archetypes

Seven pages cover everything the club ships this semester. Each names its container, its hero treatment, and its required blocks.

## 8.1 Club site home

The club site exists at rccacm.com (per the website source, read 2026-09-01), a Next.js site with its own stylesheet. This system governs docs builds and exported assets; the site converges on these tokens in a later pass (§12). The archetype below is what that convergence targets.

`--acm-container-content`. Hero with no media (§7.9), Rail solid (no pillar). Then, in order: the four pillars as a four-up card row at `--acm-col-quarter` (collapsing to two-up at 8 columns and stacked at 4), a three-up "next three Thursdays" card grid pulled from the meeting plan, one band with the three-door closer, footer.

The pillar row directly under the hero is what makes the home page the club's. It says what the club is in one horizontal object, before a single paragraph.

## 8.2 Event page

`--acm-container-doc`. Ledger line with the date and room, H1 with the event name, one-sentence subhead, two buttons (RSVP, ask an officer). Then a Facts table (What, When, Where, Who should come, Bring, RSVP, Cost, Food, Funded by ASRCC?), the agenda as a three-column public table, the officer cards, and the footer with the ASRCC line if funded.

The Facts table is the same field set as [templates/announcement.md](../../../templates/announcement.md), so the page and the announcement never drift.

## 8.3 Meeting page

`--acm-container-prose` article column on a `--acm-surface-container` page ground. This is one meeting rendered (§7.4), and the HTML must not diverge in section order or heading text from the markdown source. Agenda rows, the read-aloud block, and the Check callout for the one ask do the work. No hero, no media. `data-pillar` set from the format.

## 8.4 Lab day page

`--acm-container-content`. Ledger line with the lab day number and date, H1 ("Lab day 3"), one-line subhead naming the four challenges. Then the four station cards as a card grid at `--acm-col-quarter`, one per tier in tier order, each card showing title, tier chip, "Builds" line, and a link to the full card in the lab repo (`data-xref`, so it takes `--acm-secondary`: it points out of this repo). Below the grid, the day's run sheet as agenda rows and the footer.

Thirds do not exist at 8 columns (§4.2), so four stations collapse to two-up on a tablet and stack on a phone, in tier order. Never reorder to fill a row.

## 8.5 Showcase page

`--acm-container-content`, and it is the page the whole system is designed around this term.

Structure: hero with the date and the ask, the four pillars row, a live run of show built from the timeline component with the current block in the emphasized tier, a project wall as a card grid at `--acm-col-quarter` grouped by tier lane, the three-door closer, and the footer with the ASRCC line if the day was funded.

The live run of show is the only place in the system where content updates during a page view. Everything that changes uses `tabular-nums` and the emphasized tier, so nothing reflows while someone is reading. The visible clock the showcase doc asks for is this component, projected.

## 8.6 Doc page (standalone HTML build of a markdown file)

`--acm-container-doc`. Side nav on the left at desktop, "On this page" rail on the right above 1024px, article column in the middle. Elevation 0 throughout; a documentation page needs no shadows. Every heading level uses the 2:1 rhythm and there are no rules, boxes, or background bands inside the article.

Required blocks: H1, the article, the last-updated stamp, and the ASRCC line if the doc is an event record ASRCC funded.

## 8.7 Share card

1200×630. `--acm-surface-container` ground, the Rail at 24px on the inline-start edge, the ledger line at the top with the date, the page title in the brand face at `display-sm`, and nothing else. No logo. The website already ships a card of this shape (a 24px orange rule on a near-black ground with the club name and the four pillars); the docs card matches it so a link from either reads as one club. Export sizes and the type minimums for every card are in [assets.md](assets.md).

## 8.8 The GitHub dark and light diagram problem

Ship both files behind `<picture>`. GitHub honors this in both themes with no script.

```html
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/diagrams/pin-map-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/diagrams/pin-map-light.svg">
  <img alt="The fixed station pin map: LEDs on GP10 to GP13, buttons on GP14 to GP16, buzzer GP18, servo GP19, NeoPixel GP20, I2C on GP4 and GP5, potentiometer GP26, light sensor GP27."
       src="assets/diagrams/pin-map-light.svg" width="960" height="540">
</picture>
```

The alt text names what the diagram shows and doubles as the art brief. If the diagram carries only strokes and marks and no text, one file using the dual-mode tones in §2.7 is enough.

---

Last updated: 2026-09-01.
