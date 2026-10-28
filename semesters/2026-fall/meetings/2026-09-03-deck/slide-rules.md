# Slide rules

Every rule in the seven assigned files that constrains a slide deck, as a MUST and NEVER checklist for the ACM @ RCC first meeting deck (Thursday 2026-09-03, 12:50 to 1:50 PM, BLCIS A-210). Files read in full: `bright-lines.md`, `accessibility.md`, `assets.md`, `components.md`, `documents.md`, `checklist.md` (all under `docs/04-brand/design-system/`), and `docs/04-brand/brand.md`. Where an assigned file points at a value that lives only in `foundations.md` §5 or `tokens.css` (motion durations, the shipped CSS), that value is quoted from there and the citation says so. Every file is stamped "Last updated: 2026-09-01"; brand.md still marks colors and typography `[TBD: the decision]`, so every color and face below is provisional (brand.md Colors, Typography; checklist.md open item 1).

Precedence when two lines disagree: ACM's Visual Identity Standards and chapter policies, then brand.md, then the design language, then the reference surfaces. "The website does it" is never the reason a docs artifact does it (bright-lines.md §1.1).

## 1. MUST

### Format and the projector

1. Design and export at exactly 1920 x 1080 (assets.md §10.5).
2. Margins 96 px on every side (assets.md §10.5).
3. Run on the light theme: "A-210 projects onto a wall in daylight, which flattens dark grounds and low-chroma tints" (assets.md §10.5; foundations.md §2.4 as cited there). The ground is a flat surface role, `--acm-surface` (accessibility.md §2.3 item 1; tokens.css light: `#fdf8f7`).
4. Type minimums on a 1920 x 1080 slide: title 72 px; body 40 px; ledger line, footers, sources, and code line numbers 32 px; code 40 px in the code face, twelve lines at most (assets.md §10.5). These are "a judgment call, to be tested on the projector and recorded here" (assets.md §10.5).
5. One idea per slide (assets.md §10.5).
6. The Rail once, on the title slide (assets.md §10.5; "Once per screen", accessibility.md §2.4).
7. At most one callout per slide (assets.md §10.5).
8. The Board is one slide, one line per dated thing (assets.md §10.5): "every dated thing in the next four weeks, one line each" (components.md §7.4, meeting page spine item 3).
9. Faces: Inter for text and JetBrains Mono for code, both OFL, loaded by linking the Google Fonts CSS2 API or self-hosting from the `google/fonts` OFL directories (bright-lines.md §1.3 Typefaces, Font delivery; brand.md Typography, provisional). `font-optical-sizing: auto` over Inter's `opsz` axis (bright-lines.md §1.3 Optical type). Every face gets a real fallback stack (foundations.md §3.8 is the owner; not read in this pass).
10. Spacing on a 4 px base; corner scale capping at 24 px; nested inner radius equals outer radius minus the padding between them (bright-lines.md §1.3 Spacing, Shape; components.md §7.1).
11. Depth is tone first, then a 1 px `--acm-outline-variant` hairline, then shadow; shadow only for an element over busy content or for interaction (components.md §7.1). Nothing at rest uses elevation 4 (checklist.md Craft 7). A documentation-style page is elevation 0 throughout (components.md §8.6).
12. Every color resolves to a role token; "Nothing names a bare color" (components.md §7 intro). One lead hue (orange) against a warm-tinted neutral ramp, spent sparingly (bright-lines.md §1.3 Accent). Orange covers at least 70% of the non-neutral area (checklist.md Brand 4).
13. One accent per component instance; at most one of the four hues per instance (components.md §7.1).
14. Tokens are defined on `:root`; if the file carries dark redefinitions they sit under `prefers-color-scheme: dark` and again under an explicit `data-theme` attribute (documents.md §6.3). The projected deck stays on the light theme regardless (assets.md §10.5).
15. Every component works with no JavaScript: "Tab panels stay in the DOM with real headings. Disclosure widgets are `<details>`. Nothing carrying content hides behind a hover" (components.md §7.1). For a deck: every slide is in the DOM with a real heading; script only moves between them.
16. If a raw fill is used as a band (the two sanctioned fills are `--acm-fill-orange #ff4d00` and green `#22c55e`), it takes ink text, `--acm-on-surface`, never white: white on `#ff4d00` is 3.33:1 (accessibility.md §1.1 rule 3; components.md §7.2 Raw-fill variant; assets.md §10.3 Layout of the master). "The raw fills are for large areas, not controls" (accessibility.md §1.1).
17. Blue means "this points somewhere else": `--acm-secondary` on cross-references out of the repo only (foundations.md §2.6 as cited by components.md §8.4). Green (`live`) only for a state true right now (foundations.md §2.6; tokens.css).
18. Every `*-container` role is a fill, never a text color (foundations.md §2.6 Caution, as cited by components.md §7.7 contrast note).

### Name, compliance, and copy

19. The club name, written "ACM @ RCC", on the title slide and the final slide (brand.md Names: short name for "social, slides, this repo"; bright-lines.md §1.4 The three lines, Where the name goes: "Slide deck | Title slide and final slide").
20. The name is "Real selectable text, never inside an image alone, a collapsed `<details>`, a tooltip, or a hover state. Body role type at normal body size. `--acm-on-surface-variant` is the color floor and it must clear 4.5:1 against its background; measure it, do not estimate it" (bright-lines.md §1.4 How it is set). On a slide, body size is the 40 px floor (assets.md §10.5). The name line is body text for contrast purposes: "Do not set either in a light grey at 11px in the footer" (accessibility.md §1.2).
21. Nothing on the deck implies ACM made, endorsed, or funded it (assets.md §10.9 item 2; checklist.md Brand 2; documents.md §6.4).
22. ACM, ICPC, Cal Hacks, and MLH are program and event names "used under their own rules, with their own marks, never restyled into ours" (bright-lines.md §1.3 Names).
23. Spoken, at the event: "Host names the club at 0:00" (bright-lines.md §1.4 Where the name goes, Spoken row). Not a slide rule, but the deck's first slide is where it happens.
24. Exactly one `h1`, and it is the meeting's actual title: "On an event page that is the event name, not the club name" (accessibility.md §1.5; documents.md §2 Depth).
25. Sentence case everywhere, including the h1 (documents.md §2 Grammar; checklist.md Craft 1; bright-lines.md §1.3 Docs).
26. Heading grammar: task section is a bare infinitive ("Run one."), concept section is a noun phrase ("The pin map."), no `-ing` openers, and "No numbers, links, or inline code inside a heading text" (documents.md §2 Grammar). The closed exceptions: playbook title prefixes, station-card timings like "(60 seconds)", and role or tier tokens in table cells (documents.md §2 Grammar).
27. Never skip a heading level; `h2` to `h4` is a defect; `h4` does not exist in the system (documents.md §2 Depth; accessibility.md §1.5).
28. A complete introductory sentence before every list and table, "not a fragment the table completes" (components.md §7.6; documents.md §3.3; checklist.md Craft 2).
29. List versus table: "One datum per item is a bulleted list, two is a description list, three or more is a table. A single-column table is a list. A table with one row is two sentences" (documents.md §3.3; components.md §7.6).
30. Roles, not names. Officer roles by title: Chair, Vice Chair, Treasurer, Secretary, ICC Representative, Communications lead, Lab lead, Event lead, Advisor (components.md §7.13 Roles, not seats). A person's name appears only where written consent is on file; otherwise the row reads `on file with advisor` and the unnamed state is "a complete card rather than a gap" (components.md §7.13; documents.md §1 Roles, not names). Members who are not officers are never named (accessibility.md §1.7 event photography).
31. Unknowns stay `[TBD]`: "Never guess a date, a room, a name, or an amount" (documents.md §4 template footer). A facts key with no value "says `none` or `[TBD]` and never disappears" (components.md §7.4 Facts table).
32. Copy: verb-first CTAs that name the action ("Come Thursday at 12:50", not "Learn more"); one sentence of what plus one of how; formats publish their own length and capacity (bright-lines.md §1.3 Copy; components.md §7.2 GitHub form; components.md §7.12 Formats carry promises).
33. Prose: second person, active voice, present tense; paragraphs cap at four sentences; **must** or a bare imperative for required, "we recommend" for recommended, **can** for optional, **might** for a possible outcome, and "Generally avoid 'should'"; no em dashes inside sentences (`check.sh` fails on U+2014); conditions before instructions (documents.md §5 Density conventions; §1 block 6).
34. No pre-announcing: "Delete every sentence that describes what the document is about to do" (documents.md §5 The tests, item 3; §1 block 2).
35. Every date and time in `<time datetime="2026-12-10T12:50">` form (accessibility.md §1.5).
36. The pillars are four verbs, Build, Compete, Learn, Connect, and the pillar name is always in text (accessibility.md §2.4 Rules of use; components.md §7.5).
37. Agenda or run-of-show rows, if used: fixed leading column at 5.5ch, `tabular-nums`, block name, duration, rows separated by `:not(:last-child)::after`; "Every row on a public agenda states its length. Every meeting states its format and its pillar"; the clock adds up and ends at 1:50 PM (components.md §7.12; tokens.css `.acm-phase`).
38. The meeting line, when used: "Thursdays, 12:50 to 1:50 PM, BLCIS A-210" (assets.md §10.1). The club line: "ACM @ RCC meets Thursdays, 12:50 to 1:50 PM in BLCIS A-210. Everyone is welcome." (assets.md §10.3 The caption, item 3).
39. A last-updated date: "Every page and every doc carries a last-updated date" (components.md §7.10 Freshness stamp; documents.md §1 block 9; checklist.md Craft 6). The files place it in the footer; the final slide is the deck's footer position.
40. The one concrete ask a meeting ends with renders as the Check callout (components.md §7.7; §8.3).
41. The title slide is "type as the image": the title at the display role on a flat surface role, the Rail at the inline-start edge, the date and room in the label role, "No picture at all" (accessibility.md §2.3 item 1). Hero anatomy: the Rail, an eyebrow in the ledger line (pillar name, date, or "Fall 2026"), H1, one-line subhead whose last clause alone is bold and carries the date or the ask (components.md §7.9). The two buttons and the announcement pill are page controls; nothing in the files adds them to a slide.
42. A slide index or progress rail, if one exists, follows the "On this page rail": a flat list of the H2 and H3 outline set in the ledger line, active item at weight 500 in `--acm-primary`, with `aria-label="On this page"` (components.md §7.8).
43. Chips and badges, if used (tier, type, pillar, role, status): `--acm-surface-container-high` with an `--acm-outline` hairline, `--acm-radius-full`, `label-md`, height 28 in a cell or heading, 32 standalone; tier and role chips carry no icon (components.md §7.5). assets.md §10.5 lists no chip size; the smallest text it allows on a slide is 32 px.
44. Diagrams (the semester map, the lab's pin map): a three-weight stroke ladder, open chevron arrowheads with `markerUnits="strokeWidth"`, three hues plus neutral, never four; "write the part name" instead of a vendor logo (bright-lines.md §1.3 Diagrams). Pre-render Mermaid to inline SVG so the page carries no runtime dependency (documents.md §6.1). Every diagram gets alt text and the same content in text or a table nearby; "A diagram whose information exists nowhere else in text is a defect" (accessibility.md §1.7).
45. Charts, if any: categorical hues capped at three, further series from lightness steps inside a hue, neutral grey for out of scope, legend carries the numbers with a total row, one reserved meaning for a dashed outline (bright-lines.md §1.3 Charts).
46. Every column of numbers, times, dollar amounts, pin numbers, or counts is `tabular-nums` (components.md §7.6; checklist.md Craft 4).
47. Code on a slide: JetBrains Mono at 40 px, twelve lines at most (assets.md §10.5); fenced with a language token; ligatures off "so `->` and `!=` render as the characters a student types"; line numbers on anything over ten lines as a CSS counter on a pseudo-element, in `--acm-on-surface-variant` (32 px on a slide); every token color in the highlight theme clears 4.5:1 against `--acm-code-surface`, comments included; the header variant carries the filename (components.md §7.11; documents.md §3.3; assets.md §10.5).
48. Icons: Lucide, stroke icons on a 24 grid, 1.5 px, one weight everywhere, 24 px in prose and large controls, 20 px in medium and small; `currentColor` always; vendored SVGs, "Do not hotlink a CDN"; "If a needed icon does not exist in the set, use a word instead of drawing one"; one icon per row maximum (accessibility.md §2.1). For a single-file deck that means inline SVG.
49. Photos, if any: hardware-only shots need no consent; an identifiable face needs the signed slip and the badge dot; strip EXIF; no faces without dots, no screens with personal data, no legible full names; alt text with no names and no demographic description (accessibility.md §2.2; §1.7). A deck "that gets a public link" never carries a photo without consent (accessibility.md §2.2 What happens to photos without consent).
50. Every image has alt text that names what is happening, and explicit `width` and `height` (checklist.md Accessibility 6; accessibility.md §1.7). If a slide screenshot with text on it is embedded, "The alt carries the slide's text. If it is more than about 150 characters, put it in the page body and use `alt=""`" (accessibility.md §1.7).
51. Run the pre-publish procedure before the deck is shown or linked: axe with zero critical and serious, Lighthouse accessibility, contrast on the specific pairs with DevTools, keyboard pass, structure pass, W3C Nu validator, reflow at 320 px and 200% zoom, reduced motion and forced-colors emulation, screen-reader rotor pass once per template, and the two things a tool cannot check (accessibility.md §1.9; checklist.md).

### Accessibility and structure (detail in section 8)

52. Contrast measured, not estimated, on every text pair: 4.5:1 for body text and any text under 24 px regular or 18.66 px bold; 3:1 for large text and for non-text that carries meaning (accessibility.md §1.2; checklist.md Accessibility 1).
53. Focus: the shipped `:focus-visible` ring, `:focus-visible` only, never `outline: none` without a replacement in the same rule (accessibility.md §1.3; components.md §7.1).
54. Landmarks on the HTML page: skip link first in `<body>`, `<header>` with `<nav aria-label="Main">`, `<main id="main" tabindex="-1">`, `<footer>`; distinct `aria-label` on every nav (accessibility.md §1.5; components.md §7.8).
55. Keyboard: tab order equals DOM order; everything clickable is a `<button>` or an `<a href>`; no keyboard traps; Escape closes anything that opens (accessibility.md §1.6).
56. Targets: 44 x 44 CSS px for anything tapped on a phone, 24 x 24 absolute minimum for dense desktop-only controls with 24 px of clear space; icon-only buttons carry an accessible name (accessibility.md §1.4).
57. The Rail is decorative: `aria-hidden="true" focusable="false"` on any inline SVG instance; a CSS pseudo-element needs nothing (accessibility.md §1.7, §2.4). Decorative icons and glyphs are `aria-hidden="true"` (accessibility.md §2.1; components.md §7.9).
58. Lists of things are `<ul>`; tables get `<th scope="col">` or `scope="row"` and a `<caption>` in HTML (accessibility.md §1.5).
59. No meaning by color alone: links underlined, pillars named in text, status as a word, error states labeled by a word or icon (accessibility.md §1.8, §1.9 step 9; checklist.md Accessibility 3).
60. The `prefers-reduced-motion` block is present (bright-lines.md §1.3 Reduced motion; tokens.css).
61. The page body never scrolls horizontally; at 200% zoom nothing is clipped or overlapping (accessibility.md §1.9 step 5; checklist.md Accessibility 5).
62. Forced-colors mode: text readable, focus ring visible, no content lost (accessibility.md §1.3, §1.9 step 6).

## 2. NEVER

### Chrome that makes the deck read as ACM or as Google

1. ACM Blue, PANTONE Process Blue C, `#0182ac`, anywhere: "ACM Blue appears nowhere except inside the unaltered ACM logo" (bright-lines.md §1.4 line 3; §1.3 Color, Accent; components.md §7.1; checklist.md Brand 3; assets.md §10.9 item 7; brand.md Colors; foundations.md §2.6 as cited). "A blue that is not `--acm-secondary` on a club page is a defect" (components.md §7.1).
2. A gradient of any kind: "The docs system ships no gradient" (bright-lines.md §1.3 Gradients); the website's `.text-gradient-orange` "in docs, slides, or print" because "gradient text has no single background pair to measure, so it fails contrast by definition, and a banded headline on the A-210 projector reads as a defect" (bright-lines.md §1.3 Gradients); the ACM Diamond's gradient (bright-lines.md §1.3, §1.5); gradient meshes (accessibility.md §2.3 Not used). Reviewer note: the Rail's own `::before` is drawn with a hard-stop `linear-gradient` and the Rail field with a `repeating-linear-gradient`; both are the system's sanctioned construction of a solid bar and hairlines, not a visible gradient (accessibility.md §2.4, §2.3).
3. The Google four (blue, red, yellow, green) "in any arrangement", including "three of them at similar weight" (bright-lines.md §1.3 Our hues; §1.5; assets.md §10.3, §10.9 item 7; checklist.md Brand 4; brand.md Files in assets/).
4. The ACM Diamond, or any rotated-square silhouette, as decoration, icon, bullet, or favicon glyph: "Do not use the ACM diamond symbol within headlines or text" (bright-lines.md §1.3 Shape, Icons; §1.5; accessibility.md §2.1, §2.4).
5. The `{}` and `<>` glyphs from community pages (bright-lines.md §1.3 Icons).
6. Google Sans or Product Sans; Myriad Pro (bright-lines.md §1.3 Typefaces).
7. Material Symbols or Google Symbols (bright-lines.md §1.3 Icons; accessibility.md §2.1).
8. Any ACM mark at all until the chapter lockup is pulled from ACM's matrix page: "Until then, no artifact carries an ACM mark at all; the club name does the work" (bright-lines.md §1.5; brand.md Files in assets/). If a lockup ever appears, none of the improper-use alterations, including "a white knockout, a scroll animation, a rounded tile, a stretched aspect ratio, a size under 0.5 inch" (checklist.md Brand 5; bright-lines.md §1.5).
9. The two AI Hackathon PNGs in `assets/`; they "are not a logo and are retired for new artifacts" (assets.md §10.1; bright-lines.md §1.5; brand.md).
10. ACM's secondary seven as a set, or ACM Orange `#fc9200` in place of the club's `#ff4d00` lead (bright-lines.md §1.3 Our hues; §1.6 Orange as the lead). A fifth hue (foundations.md §2.6 as cited by bright-lines.md §1.3 Diagrams).
11. A blue action color of any kind on a chapter page; the sibling chapter's green as an accent (bright-lines.md §1.3 Accent).
12. ACM's stock "community" and "innovation" photography; stock people at laptops; AI-generated images of people; any Google product screenshot, Pixel photography treatment, or Google marketing imagery; the website's hero video (bright-lines.md §1.3 Imagery; accessibility.md §2.2 Never used).
13. Freehand illustration, clip art, 3D blob renders, watercolor, hand-drawn doodle borders, isometric packs, "anything with the soft rounded optimistic character of Google's AI illustration style" (accessibility.md §2.3).
14. Vendor logos (Raspberry Pi, Arduino) as diagram labels; Google Cloud product icons (bright-lines.md §1.3 Diagrams).
15. Copy "borrowing ACM's institutional authority: first-person-as-ACM, ACM's membership numbers, 'ACM says'"; the website's manifesto register (bright-lines.md §1.3 Copy).
16. "ACM" alone as the club's name; "ACM Riverside"; an `acm.org` lookalike; any Google mark in a handle (bright-lines.md §1.3 Names, Domains and handles; §1.4).
17. An invented independence sentence or disclaimer block: "There is no independence sentence" (bright-lines.md §1.4); "Do not invent a disclaimer sentence; a made-up compliance line reads as one and teaches the next officer team to trust it" (components.md §7.10).
18. The website's `.glass-panel` blur surface, its 32 px and 48 px radii, its `-webkit-font-smoothing: antialiased` on `body`, pinned `font-variation-settings`, its numbered `--step-N` scale, or Tailwind classes as vocabulary (bright-lines.md §1.3 Depth, Shape, Optical type, Type roles, Spacing).
19. Hotlinking any font or media from the website's host or from ACM's (bright-lines.md §1.3 Font delivery). Hotlinking an icon CDN or shipping a webfont of the icon set (accessibility.md §2.1). `shields.io` badges (components.md §7.5).
20. The names "Material Design", "Material 3", "M3" for the system (bright-lines.md §1.3 Type roles).

### Hue and the Rail

21. Any hue on pillars, tiers, meeting types, or chips: "Meeting types and pillars get no hue" (components.md §7.4); "No chip carries a hue" (components.md §7.5). A row of components cycling hues; accent cycling on officer cards (components.md §7.1, §7.13).
22. More than one Rail per slide: "Once per screen. One Rail on the hero or the page's first block" (accessibility.md §2.4); "The Rail once, on the title slide" (assets.md §10.5).
23. The Rail anywhere but the title slide, with one exception: a callout's short Rail as its inline-start edge, "the only repetition allowed", and at most one callout per slide (accessibility.md §2.4; assets.md §10.5; components.md §7.7). "Never both on the same block" (accessibility.md §2.4).
24. Rounding, rotating, stroking, or gradient-filling the Rail: "Fill only, no stroke. Never a gradient, never rounded, never rotated" (accessibility.md §2.4 The form). Reviewer note: the shipped callout clips its short Rail to the callout's `--acm-radius-lg` via `overflow: hidden` (tokens.css Callouts); that is the shipped construction, not a rounded bar.
25. The Rail as a logo, an avatar, or a favicon: "The Rail is never the club's logo and never becomes the favicon on its own" (accessibility.md §2.4; components.md §7.8; assets.md §10.3 Profile picture).
26. The Rail and any ACM mark in "a shared box, a shared color field, or any arrangement that could read as one combined mark"; on merch, the two on the same object (accessibility.md §2.4; bright-lines.md §1.3 Merch).
27. The Rail's Break carrying meaning alone; "a break at 20% versus 40% is invisible to a lot of people" (accessibility.md §2.4).
28. `--acm-rail-break` set on `.acm-rail` itself, or anywhere other than `:root` (accessibility.md §2.4 CSS comment; tokens.css The Rail).
29. A Break on this deck at all: the deck has no single pillar, and "Club pages, footer, anything without a pillar" omit `data-pillar` so "the bar runs solid" (accessibility.md §2.4 Break table). Which pillar each meeting type maps to is open (checklist.md open item 5).
30. The Rail field (hairlines at column positions) anywhere except "behind a hero or on the showcase page", and untested on the projector (accessibility.md §2.3 item 3; checklist.md open item 12).

### Ground, contrast, and imagery

31. A dark ground: "decks run on the light theme" (assets.md §10.5). The website's `#050505` is not a docs surface either way (bright-lines.md §1.6).
32. A photo behind text: "No photo sits behind text, ever, because the contrast of text over a photo cannot be measured" (assets.md §10.2; accessibility.md §1.2). A control on a photograph (accessibility.md §1.3).
33. Any of the four website hexes as body text on the light surface (best is orange at 3.16:1); green `#22c55e` or gradient orange `#ff8800` as text or as a meaningful shape on light (accessibility.md §1.1 rules 1 and 2).
34. White labels on the raw orange or green fills (accessibility.md §1.1 rule 3; components.md §7.2).
35. A `*-container` role used as a text color: "`#ffdbd0` as text on `#fdf8f7` is 1.22:1" (foundations.md §2.6 as cited).
36. Error told from primary by hue alone, or an error control beside a primary control in one component (accessibility.md §1.1 rule 4; components.md §7.1). Red as a callout color (components.md §7.7).
37. Green as decoration or a second accent (foundations.md §2.6 as cited by tokens.css).
38. Estimated contrast: "Contrast of every text pair measured against the tokens, not eyeballed" (assets.md §10.9 item 7; checklist.md Accessibility 1).
39. Status encoded in color or emoji alone (accessibility.md §1.8; checklist.md Accessibility 3).
40. An identifiable face without consent on file, a subject who may be under 18, a name badge photographed for public posting, or a whiteboard with a phone number (accessibility.md §2.2; assets.md §10.6 Name tag row; §10.9 item 3).
41. A QR code without its URL as real text beside it (accessibility.md §1.7); the QR target is still `[TBD]` (brand.md).

### Structure and callouts

42. More than one callout per slide (assets.md §10.5). Two callouts adjacent, a callout immediately after a heading, more than two per source document or three per built page (documents.md §3.2; components.md §7.7).
43. A callout type outside Note, Warning, Check: `TIP` and `CAUTION` are banned; so are `!!! note`, `:::note`, a bolded `> **Note:**` blockquote, and an emoji-prefixed line (documents.md §3.2; components.md §7.7).
44. A callout for "cross-references, prerequisites, procedural steps, and anything critical to succeeding" (components.md §7.7; documents.md §3.2 admission test).
45. More than one idea per slide (assets.md §10.5).
46. Merged table cells: "a merged cell breaks screen-reader traversal and breaks in markdown" (components.md §7.6; documents.md §3.3).
47. Vertical rules or zebra striping (components.md §7.6; documents.md §3.3).
48. A table for layout (accessibility.md §1.5). A one-column table; a table with one row (components.md §7.6; documents.md §3.3).
49. A skipped heading level; an `h4`; a second `h1`; an `h1` that is the club name instead of the meeting title (documents.md §2; accessibility.md §1.5). Heading level picked by how it looks (accessibility.md §1.5).
50. Title Case, `-ing` openers, or numbers, links, or inline code in heading text (documents.md §2 Grammar).
51. An em dash inside a sentence (U+2014 fails `check.sh`); "should" as a prescriptive word; a pre-announcing sentence; paragraphs over four sentences (documents.md §5).
52. A guessed date, room, name, or amount; a facts key dropped instead of marked `[TBD]` (documents.md §4; components.md §7.4).
53. A non-officer member's name; an officer's name without consent on file; an individual named in alt text (documents.md §1; components.md §7.13; accessibility.md §1.7).
54. A fully rounded container that is not an action: "Pills mean actions. If a container is fully rounded it reads as a control and someone will click it" (components.md §7.1).
55. More than one Primary button per view; a Text button beside a Primary; a filled button other than Primary on a web page (components.md §7.2).
56. Content that depends on JavaScript, or content hidden behind a hover (components.md §7.1).

### Motion and interaction

57. The website's 0.3 / 0.6 / 1.2 second durations; the magnetic cursor, the scramble text, the velocity text; "A pulsing 'thinking' treatment. A four-color loader" (bright-lines.md §1.3 Motion).
58. Omitting the `prefers-reduced-motion` block (bright-lines.md §1.3 Reduced motion).
59. `--acm-ease-spatial` on opacity or color: "a color that overshoots renders as a flash" (foundations.md §5.3).
60. `outline: none` without a replacement in the same rule; a positive `tabindex`; a `<div onclick>`; CSS `order` or `grid-area` separating visual and DOM order for interactive content; `display: none` or `visibility: hidden` on the skip link; a keyboard trap (accessibility.md §1.3, §1.6).
61. A focused control fully hidden behind a sticky header or footer (accessibility.md §1.3, SC 2.4.11).
62. Elevation 4 on anything at rest (checklist.md Craft 7).

## 3. The Rail and the Break: exact CSS

Verbatim from accessibility.md §2.4 ("The CSS here is the explanation. The shipping copy lives in tokens.css", accessibility.md intro):

```css
/* Set the pillar ONCE on :root. Never set --acm-rail-break on .acm-rail
   itself; a value declared on the element shadows the inherited one and
   the page-level switch stops working. */
:root[data-pillar="build"]   { --acm-rail-break: 20%; }
:root[data-pillar="compete"] { --acm-rail-break: 40%; }
:root[data-pillar="learn"]   { --acm-rail-break: 60%; }
:root[data-pillar="connect"] { --acm-rail-break: 80%; }

.acm-rail {
  position: relative;
  padding-inline-start: calc(var(--acm-space-2) + var(--acm-space-4));
}
.acm-rail::before {
  content: "";
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  width: var(--acm-space-2);
  color: var(--acm-primary);
  /* A break at 200% sits off the element, so an unset pillar renders solid. */
  background: linear-gradient(
    to bottom,
    currentColor 0 calc(var(--acm-rail-break, 200%) - 6px),
    transparent  calc(var(--acm-rail-break, 200%) - 6px) calc(var(--acm-rail-break, 200%) + 6px),
    currentColor calc(var(--acm-rail-break, 200%) + 6px) 100%
  );
}
```

The form: "A solid vertical bar in `--acm-primary`, flush to the inline-start edge of a block, full block height. One width per medium. Fill only, no stroke. Never a gradient, never rounded, never rotated" (accessibility.md §2.4). Screen width is `--acm-space-2` (8 px) for "hero, script block, the left edge of a Warning or Check callout"; 24 px on the 1200 x 630 share card; 0.25 in in print (accessibility.md §2.4 width table). The Break's gap height is `--acm-space-3` (12 px) on screen (accessibility.md §2.4).

Where `--acm-rail-break` may be set: "Set once on the page's root element; `--acm-rail-break` carries the percentage" (accessibility.md §2.4 The Break). Never on `.acm-rail` itself (the CSS comment above; tokens.css The Rail block repeats it: "a value declared on the element shadows the inherited one and the page-level switch stops working").

The shipping copy in tokens.css differs in two names only: `width: var(--acm-rail-w)` where `--acm-rail-w: var(--acm-space-2)`, and `padding-inline-start: calc(var(--acm-rail-w) + var(--acm-space-4))`; `--acm-rail-gap: var(--acm-space-3)` names the Break height (tokens.css The Rail, Motion blocks). A reviewer accepts either spelling.

**Does the title slide carry a Break? No.** The Break table's last row: "Club pages, footer, anything without a pillar | omit | unset; the bar runs solid" (accessibility.md §2.4). This deck spans the club intro, the semester map, the lab decision, and recruitment, so it has no single pillar: no `data-pillar` on `:root`, `--acm-rail-break` unset, and the Rail renders solid because the fallback puts the gap at 200%, off the element. Two further reasons the files give: "Which pillar each meeting type maps to is an open item in checklist.md, not a decision this file makes" (accessibility.md §2.4; checklist.md open item 5), and the club site home hero is the precedent: "Hero with no media (§7.9), Rail solid (no pillar)" (components.md §8.1). If a Break is ever used, "Verify the gap edges in a browser at 1x and at 2x device pixel ratio before shipping; a 12px gap on a percentage position can land on a half pixel" (accessibility.md §2.4; checklist.md open item 12).

Forced colors: the Rail and the callout Rails take `background: CanvasText` (tokens.css Forced colors block).

## 4. Callouts and the script block

The set is closed at three; "Nothing else becomes a callout" (components.md §7.7). Light-theme hexes are from tokens.css.

| Type | Meaning | Fill and text tokens | GFM form | Short Rail |
|---|---|---|---|---|
| Note | "Useful, not critical to the task at hand." | `--acm-surface-container-high` `#f0e6e3` / `--acm-on-surface` `#221f1e` | `> [!NOTE]` | No. tokens.css: "Warning and Check carry a short solid Rail as their inline-start edge"; accessibility.md §2.4 lists only "a Warning or Check callout" |
| Warning | "Do not do this, or it cannot be undone. Money, safety, privacy, a room booking, a pin map change." | `--acm-primary-container` `#ffdbd0` / `--acm-on-primary-container` `#661900` | `> [!WARNING]` | Yes, solid, in `currentColor` |
| Check | "The 60-second check for understanding, or the one concrete ask a meeting ends with." | `--acm-live-container` `#c9f2d0` / `--acm-on-live-container` `#003e17` | `> [!IMPORTANT]` with a bold `Check:` lead-in | Yes, solid, in `currentColor` |

Anatomy (components.md §7.7; documents.md §6.3; tokens.css Callouts): a short Rail as the inline-start edge, "a bold inline label ending in a colon, then the body on the same line. No separate title row and no icon column; the label and the tint carry the meaning." Padding "12px block, 20px inline-end, and an inline-start value equal to the gutter plus the Rail width" (tokens.css: `var(--acm-space-3) var(--acm-space-5) var(--acm-space-3) calc(var(--acm-space-5) + var(--acm-space-8))`). Body at `body-md` on a page; on a slide the 40 px body floor governs (assets.md §10.5). `--acm-radius-lg`, `max-width: var(--acm-measure-prose)`. "Every callout carries an `--acm-outline` hairline" (`#7e7572`, inset box-shadow) "because container fills measure between 1.10:1 and 1.22:1 against the ground" (components.md §7.7). The Rail inside a callout is solid: "no Break inside a callout" (tokens.css). Note is neutral on purpose so a page "carries at most two hues plus grey"; Warning takes the primary container "so a warning adds no second hue to a page" (components.md §7.7).

Admission test, all three must hold: "the information is relevant but not necessary to the current task, the interruption does not obstruct the reader's progress, and the content does not flow from the sentence before it" (components.md §7.7; documents.md §3.2). Scarcity: at most one per slide (assets.md §10.5); "Two callouts never sit adjacent"; "never immediately after a heading" (components.md §7.7; documents.md §3.2). The meeting's one concrete ask is the sanctioned use of Check on this deck (components.md §7.7, §8.3).

**The read-aloud (script, verbatim) block** (components.md §7.4): "Left Rail in `--acm-primary` at `--acm-space-2`, `body-lg`, `--acm-on-surface`, 16px inline-start padding. It is the one block a person reads verbatim, so it stays at full body size while everything around it may compress. Markdown form is a blockquote." Its Rail width is the screen width, 8 px (accessibility.md §2.4 table names "script block"). Constraint for this deck: the files allow the Rail once, on the title slide, and the only sanctioned repetition is a callout's short Rail (assets.md §10.5; accessibility.md §2.4). A read-aloud block on any other slide would be a second Rail; the files do not sanction it. Conservative path per bright-lines.md §1.7: carry verbatim lines as plain body text or, where it is the meeting's ask, as the Check callout.

## 5. Table styling

From components.md §7.6 and documents.md §3.3, with the HTML rules from accessibility.md §1.5:

- "Horizontal rules only." A single `--acm-outline-variant` rule under each row (`#dacfcc`; tokens.css `th, td { border-block-end: var(--acm-hairline) solid var(--acm-outline-variant) }`).
- Tinted header row on `--acm-surface-container-high` (`#f0e6e3`), heads at `label-lg`, sentence case, no terminal punctuation.
- Body cells at `body-md`, "one step below the surrounding prose"; on a slide the 40 px body floor governs (assets.md §10.5).
- "No vertical rules, no zebra striping, and no merged cells."
- Cell padding 8 px, "deliberately tighter than the 16px prose rhythm so the table compresses into a distinct object."
- `<th scope="col">` on the header row, `<th scope="row">` on a first-column label, and a `<caption>` (accessibility.md §1.5). Never a table for layout.
- Every column of numbers, times, dollar amounts, pin numbers, or counts in `tabular-nums`.
- A complete introductory sentence before every table; three or more facts per row to be a table; six columns is the practical ceiling (documents.md §3.3).
- A facts table is two-column key-value with an empty header row; a missing value reads `none` or `[TBD]` (documents.md §1 block 3; components.md §7.4).
- Row hover is a 4% state layer; an empty table is "one full-width cell with a sentence saying what would appear and what to do about it, never a blank table" (components.md §7.6).
- A wide table scrolls inside its own container on a page; a fixed 1920 x 1080 slide has no scroll, so the table must fit inside the 96 px margins at the 40 px body floor (components.md §7.6; assets.md §10.5).

## 6. The club name and the ASRCC line

Two correct forms (brand.md Names): "ACM Student Chapter at Riverside City College" for "forms, constitution, ASRCC packets"; "ACM @ RCC" for "social, slides, this repo". On slides the form is **ACM @ RCC**. The GitHub org display name "ACM@RCC" and repo slug `rcc-acm` are handles, not the name on an artifact (brand.md Names; bright-lines.md §1.3 Domains and handles).

Placement: "One placement per artifact, at that artifact's front door"; for a slide deck, "Title slide and final slide" (bright-lines.md §1.4 Where the name goes). Set as real selectable text at body role and normal body size, color no lighter than `--acm-on-surface-variant` (`#5c5958` light), measured at 4.5:1 or better (bright-lines.md §1.4 How it is set; accessibility.md §1.2). A slide deck is a standalone publication surface, so the internal-doc exemption does not apply (bright-lines.md §1.4 Where it is not required).

ASRCC: the line is conditional. "'Funded by ASRCC', or the wording Student Activities asks for, on the flyer of any event ASRCC paid for, and said aloud at the event. Required by ASRCC, not by ACM" (bright-lines.md §1.4 line 2; brand.md RCC rules that apply; checklist.md Brand 6). assets.md §10.1 gives the long form: "This event is funded by ASRCC (Associated Students of Riverside City College)." The credit is "a required slot with a `required` flag when the funding source is ASRCC" and otherwise absent (components.md §7.10; §8.2 Facts table has a "Funded by ASRCC?" row). None of the seven files records the funding of the 2026-09-03 meeting. The brief states it is not ASRCC-funded, so no ASRCC line is required on this deck, and adding one would be an invented compliance line (components.md §7.10). If funding is later confirmed, the line goes on the deck and is said aloud.

Nothing else is required by ACM: "Required text when the logo appears: None imposed by ACM" (assets.md §10.1). No RCC logo: "Use of the RCC name and logo on club materials: [TBD: confirm with Student Activities]" (brand.md RCC rules that apply).

## 7. Motion and reduced motion

The assigned files set the shape (bright-lines.md §1.3 Motion, Reduced motion; documents.md §6.3; accessibility.md §1.9 step 6; checklist.md Accessibility 4). The numbers live in foundations.md §5 and tokens.css, quoted here from those files.

- Two tracks: "Spatial covers position, size, rotation, and corner radius. It may overshoot. Effects covers opacity, color, and state layers. It never overshoots" (foundations.md §5.1).
- Slide transitions are page-level transitions, the slow tier: effects 220 ms, spatial 480 ms (foundations.md §5.2 table: "slow | 220ms | 480ms | Dialog and sheet enter, page-level transitions"). Tokens: `--acm-dur-slow-effects: 220ms`, `--acm-dur-slow-spatial: 480ms` (tokens.css Motion).
- "Enter is slower than exit. An exit uses the tier below its enter" (foundations.md §5.2): a slide leaving uses the default tier, 140 ms effects, 320 ms spatial.
- Easing: `--acm-ease-standard: cubic-bezier(0.32, 0.72, 0, 1)` for "Effects, always" and spatial moves that must land exactly; `--acm-ease-spatial: cubic-bezier(0.34, 1.56, 0.64, 1)` for spatial only; `--acm-ease-exit: cubic-bezier(0.4, 0, 1, 1)` for "Anything leaving" (foundations.md §5.3; tokens.css). "Never apply it [ease-spatial] to opacity or color: a color that overshoots renders as a flash" (foundations.md §5.3).
- Not the website's 0.3 / 0.6 / 1.2 s (bright-lines.md §1.3; foundations.md §5.2).
- Reduced motion: "Zero the spatial durations, leave effects intact. Every state change survives, every movement stops" (foundations.md §5.4; bright-lines.md §1.3 Reduced motion). The shipped block (tokens.css):

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --acm-dur-fast-spatial: 0ms;
    --acm-dur-default-spatial: 0ms;
    --acm-dur-slow-spatial: 0ms;
  }
  html { scroll-behavior: auto; }
  .acm-card:hover { transform: none; }
}
```

- Under reduced motion the slide still changes (state change survives); only the movement stops. Verify with DevTools "Emulate prefers-reduced-motion: reduce": "Every transition and animation the motion section defines must stop. Check that nothing becomes unusable because a transition was doing load-bearing work" (accessibility.md §1.9 step 6; checklist.md Accessibility 4).
- No content behind a hover; the hero is static: "States: none" (components.md §7.1, §7.9). Documentation pages "need almost none" (documents.md §6.3).

## 8. Accessibility rules that apply

- **Contrast floors** (accessibility.md §1.2): 4.5:1 for body text and any text under 24 px regular or 18.66 px bold; 3:1 for large text and for non-text that carries meaning (icons, focus rings, borders, chart marks, a selected state); no minimum for purely decorative graphics, but hold the Rail and decorative icons to 3:1 anyway so they "survive a projector in a bright lab" (accessibility.md §2.1, §2.4). Measure every pair, light theme first, with DevTools or the TPGi analyser; "Dark theme is a second full pass, not an inversion you can assume works" (accessibility.md §1.2, §1.9 step 2; checklist.md Accessibility 1). Design-time shortcut only: 40 L\* points is about 3:1, 50 about 4.5:1, and "the 50-point version does not hold in the worst case" (accessibility.md §1.1).
- **The club name line is body text at 4.5:1** whatever its size (accessibility.md §1.2). Labels on tinted containers are measured against the container, not the page (accessibility.md §1.2, §1.3).
- **Focus visibility** (accessibility.md §1.3; tokens.css): 

```css
:focus-visible {
  outline: 3px solid transparent;
  outline-offset: 2px;
  box-shadow: 0 0 0 2px var(--acm-focus-gap), 0 0 0 5px var(--acm-focus-ring);
  border-radius: inherit;
}
```

  The ring is `primary` (6.13:1 on the light surface, 4.99:1 on the deepest container); a control on a `primary` fill takes the `on-surface` outline instead. The one legitimate removal is `:focus:not(:focus-visible) { outline: none }` paired with a real `:focus-visible` ring. Never remove focus from the skip link or anything with `tabindex="0"`. A box-shadow ring is clipped by `overflow: hidden`, so the ring goes on the clipping element (components.md §7.1). Visible under forced-colors (the transparent outline is what gets a system color).
- **Keyboard** (accessibility.md §1.6, §1.9 step 3): Tab once shows the skip link, Enter lands focus in `<main>`; every stop visible and in DOM order; Enter and Space activate every control; Escape closes anything that opens; tab past the end reaches browser chrome. Everything clickable is `<button>` or `<a href>`. Disclosures use `<button aria-expanded aria-controls>` with focus returning to the trigger.
- **Targets** (accessibility.md §1.4): 44 x 44 for phone taps, 24 x 24 minimum for dense desktop controls with 24 px clearance; pad the target, do not grow the icon; icon-only buttons need `aria-label` or visually hidden text.
- **Structure** (accessibility.md §1.5): one `h1` (the meeting title), no skipped levels, `<ul>` for lists of things, `<time datetime>` on every date and time, tables with `scope` and `<caption>`, landmarks (`.acm-skip`, `<header><nav aria-label="Main">`, `<main id="main" tabindex="-1">`, `<footer>`), distinct `aria-label` on each nav. Skip link hidden with `left: -9999px`, never `display: none` (accessibility.md §1.6).
- **`aria-hidden` on decorative things**: the Rail as inline SVG gets `aria-hidden="true" focusable="false"`; the pseudo-element version needs nothing (accessibility.md §1.7, §2.4). Decorative icons and hero glyphs are `aria-hidden="true"` (accessibility.md §2.1; components.md §7.9). Icons are `currentColor` and never the only label without an `aria-label` (accessibility.md §2.1).
- **Text as real text**: the club name and any ASRCC line are "real text ... Not an image, not a background, not `title` attribute text" (accessibility.md §1.5; bright-lines.md §1.4). A QR code's URL is printed as text beside it (accessibility.md §1.7). A diagram's information exists in text or a table nearby (accessibility.md §1.7).
- **Alt text**: replaces the image; never `alt="logo"`; never names an individual; never describes race, gender, body, or disability; one sentence; `alt=""` when a caption already says it; a slide screenshot's alt carries the slide's text (accessibility.md §1.7). Every image has explicit `width` and `height` (checklist.md Accessibility 6).
- **Color alone**: never; links underlined, pillars named, statuses worded, no instruction by shape or position ("the round button", "the box on the right") (accessibility.md §1.8, §1.9 step 9; §2.4; checklist.md Accessibility 3).
- **Reflow and zoom** (accessibility.md §1.9 step 5): page body never scrolls horizontally at 320 CSS px; nothing clipped at 200% zoom on 1280 px.
- **Forced colors** (accessibility.md §1.3, §1.9 step 6; tokens.css): cards, callouts, and secondary buttons take a `1px solid CanvasText` border; the Rail becomes `CanvasText`; text readable, ring visible, nothing lost.
- **Code**: every syntax color at 4.5:1 against `--acm-code-surface` in both themes; TODO markers are words, not colors; a language tag on every fence (accessibility.md §1.2, §1.8; components.md §7.11).
- **Procedure**: run accessibility.md §1.9 steps 1 through 7 and 9 before the deck is shown or linked; zero critical and serious in axe is "a floor, not a pass".

## 9. Things the files leave [TBD] that touch slides

Listed so nobody invents them.

1. `[TBD: A-210 projector native resolution.]` (assets.md §10.5). The slide type minimums are a judgment call "to be tested on the projector and recorded here" (assets.md §10.5).
2. Chapter logo: `[TBD]`. "There is no chapter logo file in `assets/` yet"; "Until then, no artifact carries a logo" (brand.md Files in assets/; bright-lines.md §1.5; assets.md §10.1; checklist.md open item 2). The ACM matrix page `identitystandards.acm.org/matrix3.html` was unreachable from tooling on 2026-09-01 (bright-lines.md §1.5).
3. Favicon: `[TBD]`. "It follows the chapter logo decision, not this device" (accessibility.md §2.4). The deck's `<link rel="icon">`, if any, has no sanctioned mark.
4. Colors: `[TBD: the decision]`; typography: `[TBD: the decision]`. Every hex and face is provisional as of 2026-09-01 (brand.md Colors, Typography; checklist.md open item 1: "Until then every value in this system is provisional").
5. Use of the RCC name and logo on club materials: `[TBD: confirm with Student Activities]` (brand.md RCC rules that apply).
6. The QR codes' target link: `[TBD: confirm which URL it encodes]` (brand.md Files in assets/; bright-lines.md §1.5; assets.md §10.6). Until resolved, `alt="QR code; the link is printed beside it"` (accessibility.md §1.7).
7. Which pillar each meeting type maps to for `data-pillar` (lab day, ICPC, career, mini-talk, hackathon, showcase): open, "this system does not decide it" (checklist.md open item 5; accessibility.md §2.4). No slide may assign a Break to a meeting type.
8. Adopting the Rail as the system's device needs a decision-log entry (accessibility.md §2.4 Where it comes from; checklist.md open item 4: blocks "Any build").
9. The Rail field hairlines and the Break's gap edges, "checked on the projector and at 2x device pixel ratio" (checklist.md open item 12; accessibility.md §2.3, §2.4). Untested.
10. Container tint chroma (0.012) and dark elevation alphas on the A-210 projector: "a lecture-hall projector flattens low-chroma tints" (foundations.md §2.4 as cited by assets.md §10.5; checklist.md open item 11). The warm-paper tint of `--acm-surface-container-*` may flatten to nothing on the wall.
11. Icon stroke on the projector: if 1.5 px thins out, "the sanctioned change is one system-wide step to 2px, recorded in foundations, never a per-icon adjustment" (accessibility.md §2.1).
12. Lucide license: "understood to be ISC. Unverified in this document" (accessibility.md §2.1; checklist.md open item 7). Vendored SVGs with the upstream LICENSE and a brand.md attribution row before the dependency is committed.
13. The live website URL: the website source names `rccacm.com`, "links.md still marks the live URL `[TBD]`" (checklist.md open item 15; bright-lines.md §1.3 Domains and handles).
14. The shared drive link for masters: `[TBD: link in links.md]` (assets.md §10.8).
15. Export templates: `[TBD: the templates do not exist yet; the sizes below are their spec.]` (assets.md §10.2; accessibility.md §2.3 Template contract). No slide template SVG exists.
16. ACM's identity standards are version 1.0 from 2007; check each semester start for a newer guide (bright-lines.md §1.7; checklist.md open item 19).
17. The RCC media release form, whether one exists and supersedes the club slip (accessibility.md §2.2; checklist.md open item 18). Relevant only if the deck carries photos of people.
18. Whether the two AI Hackathon PNGs are retired is a decision-log entry, not a delete (bright-lines.md §1.5; checklist.md open item 3). They are not used either way.