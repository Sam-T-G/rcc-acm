# 1. Purpose and the bright lines

## 1.1 What this is for and what outranks it

This document is how an ACM @ RCC artifact is built: event pages, meeting pages, lab day pages, the showcase page, a club site, the exported social and print assets, and the markdown docs the club actually runs on. It covers both renderings of a doc, on GitHub with no stylesheet and as a standalone HTML build.

When two things disagree, the higher line wins.

1. ACM's Visual Identity Standards (`identitystandards.acm.org`, guide version 1.0, 2007, read from the PDF on 2026-09-01; the site blocks automated fetches, so open it in a browser) and the ACM chapter policies already cited in [brand.md](../brand.md): chapters may use the ACM chapter logo, a club-designed logo must carry the words "ACM Chapter" legibly, and the chapter never presents itself as speaking for ACM.
2. `docs/04-brand/brand.md`, the club's applied reading of those. It marks colors and typography `[TBD]` and names the website as the reference until decided.
3. This design language.
4. **The reference surfaces**: the club website source (`github.com/ACM-RCC/ACMWebsite`, read 2026-09-01: `src/app/globals.css`, `tailwind.config.ts`, `src/app/layout.tsx`, `src/app/opengraph-image.tsx`) and the sibling GDG on Campus @ RCC design system, whose method is the precedent for this one. Observation is not permission. "The website does it" is never the reason a docs artifact does it.

Every claim taken from a reference surface is pinned to 2026-09-01. The website is a live codebase, so the reading gets a fresh pass each fall.

## 1.2 The line: the chapter's own, not the parent's chrome

Method is how a decision gets made: scale, rhythm, elevation logic, motion curves, density, how a document argues on a page. Chrome is identity: the ACM Diamond and its gradient, ACM Blue, ACM's document templates and stock photography, and the sibling chapter's Google-licensed marks and faces. Method is public engineering practice the club is free to learn from. Chrome makes the chapter look like ACM headquarters or like the GDG chapter, and both are outcomes this system exists to prevent. The club shares officers and a room with GDG on Campus @ RCC; the two identities must be tellable apart at a glance.

## 1.3 Take this, not that

| Area | Take (method) | Do not take (chrome) |
|---|---|---|
| Type roles | A semantic scale with size, leading, tracking, and weight bound to a role name, and a brand-face-to-text-face optical split so the system can reface without touching a component. | The website's numbered `--step-N` scale as the docs' vocabulary (a numbered scale is a build artifact; roles survive a reface). The names "Material Design", "Material 3", "M3" for our system. |
| Typefaces | Inter and JetBrains Mono, both OFL, both in the Google Fonts catalog, both already loaded by the website. §1.6 records why. | Myriad Pro (Adobe-licensed, ACM's own face for ACM communications; the standards allow Arial or Helvetica for digital use, and the chapter's material is not ACM's). Product Sans. Google Sans, which is the sibling chapter's program face and blurs two clubs. |
| Font delivery | Link the Google Fonts CSS2 API, or self-host from the `google/fonts` OFL directories; both faces have one. | Hotlinking any font or media from the website's own host, or from ACM's. |
| Optical type | `font-optical-sizing: auto` over Inter's 14 to 32 `opsz` axis. Tracking that flips sign at the display-to-text boundary. The typography section owns the numbers. | Pinned `font-variation-settings` axes. The website's `-webkit-font-smoothing: antialiased` on `body` (macOS-only thinning). |
| Spacing | A 4px base with multiplier naming, and padding before gap before margin so spacing lives on the parent. | Tailwind utility classes as the docs' spacing vocabulary. The website's `--r-*` radius tokens. |
| Layout | The 4 / 8 / 12 responsive column ladder, page gutter and section rhythm as single tokens, prose measure capped independently of the layout grid. | The website's scroll-driven full-bleed sections and pinned hero as a docs pattern. Any Next.js layout component as a docs shell. |
| Color | Seed and derive rather than hand-pick. The role grammar (`surface` / `on-surface` / `primary` / `on-primary` / `container` / `outline`). Tone deltas as a reasoning aid, measurement as the gate. | ACM Blue (PANTONE Process Blue C, `#0182ac`) as a UI color, anywhere. The Material baseline theme as a package. |
| Our hues | The website's `#ff4d00`, `#4d9fff`, and `#22c55e` as hue anchors, and orange and green as the two sanctioned raw fills. | The Google four in any arrangement; the AI Hackathon banner and icon in `assets/` are the standing example (§1.5). ACM's secondary seven as a set: the standards say they are accents for ACM's communications, and seven accents on one page reads as a rainbow. |
| Accent | One lead hue against a warm-tinted neutral ramp, spent sparingly. | ACM Blue. The sibling chapter's green. A blue action color of any kind on a chapter page. |
| Gradients | Nothing. The docs system ships no gradient. If one is ever needed, the construction rule: opaque leading edge starting about a third in, diffuse tail ending before 100%, one named token override. | The website's `.text-gradient-orange` (`#ff4d00` to `#ff8800`) in docs, slides, or print: gradient text has no single background pair to measure, so it fails contrast by definition, and a banded headline on the A-210 projector reads as a defect. The ACM Diamond's gradient, which the standards say never to alter or reproduce. |
| Depth | Surface-tint ladders and 1px hairlines derived from the ink at low alpha, ahead of stacked shadows. Tone first, one reserved interaction level. | The website's `.glass-panel` (a blur over a 3% white fill) as a docs surface. A dp shadow ladder as the depth model. |
| Shape | A roundness-indexed corner scale capping at 24px and the optical nesting rule (inner radius equals outer radius minus the padding between them). | The website's 32px and 48px radii in docs. The ACM Diamond's rotated-square silhouette as decoration. |
| Motion | The two-track split: spatial may overshoot, effects never do. Three tiers. Enter slower than exit. The website's two easing curves, so the docs and the site feel like one club. | The website's 0.3 / 0.6 / 1.2 second durations (scroll choreography for a marketing page). The magnetic cursor, the scramble text, the velocity text. A pulsing "thinking" treatment. A four-color loader. |
| Reduced motion | The `prefers-reduced-motion` block: zero the spatial durations, leave effects alone. | The omission. |
| Icons | Stroke icons on a 24 grid, one base glyph plus a consistent modifier for a variant, one locked weight everywhere. §5.5 of foundations names the set. | Material Symbols or Google Symbols. The ACM Diamond as an icon, bullet, or favicon glyph ("Do not use the ACM diamond symbol within headlines or text" is the standards' own wording). The `{}` / `<>` glyphs from community pages. |
| Imagery | One locked aspect ratio across a browse grid, native ratios in article bodies, explicit width and height, lazy below the fold, alt text that names the interaction. The lab's overhead wiring photos are the club's native imagery. | ACM's stock "community" and "innovation" photography from the standards deck. Stock people at laptops. The website's hero video as a docs asset; it lives in the website repo. |
| Diagrams | A three-weight stroke ladder with each weight given a fixed job, open chevron arrowheads with `markerUnits="strokeWidth"`, stencils named by role. Three hues plus neutral, never four. | Vendor logos (Raspberry Pi, Arduino) as diagram labels; write the part name. Google Cloud product icons. |
| Charts | Cap categorical hues at three, get further series from lightness steps inside a hue, neutral grey for out of scope, legend carries the numbers with a total row, one reserved meaning for a dashed outline. | The Google four as a categorical set. ACM's secondary seven as a categorical set. |
| Docs | Sentence case everywhere. Heading grammar that encodes section type. A closed callout set with a written scarcity rule. The list-versus-table rule. Horizontal-rule-only tables. A complete sentence before every list and table. A last-updated stamp. | ACM's own document templates (proceedings covers, letterhead, newsletter covers) from the standards deck. The DevSite chrome. |
| Copy | Verb-first CTAs that name the action. One sentence of what plus one of how. Formats that publish their own length and capacity. | Copy borrowing ACM's institutional authority: first-person-as-ACM, ACM's membership numbers, "ACM says". The website's manifesto register on a doc page. |
| Names | Our own names for our own things. ACM, ICPC, Cal Hacks, and MLH are program and event names used under their own rules, with their own marks, never restyled into ours. | "ACM" alone as the club's name. The chapter is a chapter; brand.md has the two correct forms. |
| Merch | The Rail alone on club-made merch, with the club name per brand.md. | The ACM logo on anything the chapter makes without checking the chapter policies first. The ACM logo and the Rail on the same object. |
| Domains and handles | `rcc-acm` (this repo), "ACM @ RCC" (short name), `rcc.acm` on Instagram, the `ACM-RCC` GitHub org with display name "ACM@RCC", `rccacm.com` per the website source. | Anything that implies the chapter is ACM: "ACM Riverside", an `acm.org` lookalike. Any Google mark in a handle. |

## 1.4 Required lines on public artifacts

There is no independence sentence. That is a Google program rule for the sibling chapter, and ACM imposes nothing like it. Say so plainly so nobody invents one. What ACM's chapter policy requires is that the chapter never presents itself as speaking for ACM, and three things satisfy it.

### The three lines

1. **The club name, written as brand.md writes it.** "ACM Student Chapter at Riverside City College" on forms, the constitution, and ASRCC packets. "ACM @ RCC" on social, slides, and this repo. Never "ACM" alone as the name of the club.
2. **"Funded by ASRCC"**, or the wording Student Activities asks for, on the flyer of any event ASRCC paid for, and said aloud at the event. Required by ASRCC, not by ACM.
3. **ACM Blue appears nowhere except inside the unaltered ACM logo.** This is the line that keeps a chapter artifact from reading as an ACM artifact, and it is checkable by looking.

### Where the name goes

One placement per artifact, at that artifact's front door.

| Surface | Placement |
|---|---|
| Web page (event, meeting, lab day, showcase, club site) | Header lockup or the H1's ledger line, plus the footer. |
| Markdown doc on GitHub | The H1 or the job line under it. `README.md` already does this. |
| Standalone HTML build of a doc | Same as the markdown, plus the footer. |
| Slide deck | Title slide and final slide. |
| Poster, flyer, table sign, signage | Top or bottom of the piece, legible at the distance the piece is read from. |
| Social profile bio | The full or short name and the meeting time. The avatar carries whatever mark the club has on every post the account makes, so the bio is the durable placement. |
| Social post image | The short name in the image, per [assets.md](assets.md). The ASRCC line goes in the caption and, where the event is funded, in the image too. |
| Link-preview image (`og:image`) | The short name is on the card; the website's own card already does this. |
| GitHub repo social preview | The short name, or nothing but the Rail and the repo name. |
| Recorded session | Video description, and on the bumper card. |
| `templates/announcement.md` | The "one line on the club" slot already carries it. |
| Spoken, at an event | Host names the club at 0:00 and says the ASRCC line if ASRCC paid. |

### How it is set

Real selectable text, never inside an image alone, a collapsed `<details>`, a tooltip, or a hover state. Body role type at normal body size. `--acm-on-surface-variant` is the color floor and it must clear 4.5:1 against its background; measure it, do not estimate it.

### Where it is not required

Internal working docs with no logo and no standalone publication: meeting notes, run sheets, retros, the semester folders. The repo is public, so these are readable, but the repo's front door is `README.md` and that carries the name.

## 1.5 The logo

### Files

There is no chapter logo file. [brand.md](../brand.md) says so: "Chapter logo: `[TBD]`. There is no chapter logo file in `assets/` yet." Two things exist in `assets/` that are not logos: the two QR codes (`rcc-acm-qr-code.png`, `rcc-acm-qr-dark.png`, 500 x 500, target link `[TBD]` in brand.md) and the two AI Hackathon graphics discussed below.

ACM publishes a chapter logo matrix at `identitystandards.acm.org/matrix3.html`. It was unreachable from tooling on 2026-09-01. `[TBD: open it in a browser, pull the chapter lockup in the formats it offers, record its rules in brand.md, and commit the files under 1 MB to assets/.]` Until then, no artifact carries an ACM mark at all; the club name does the work.

### What ACM's standards say

Read from the standards PDF on 2026-09-01. They bind the ACM logo wherever the chapter uses it.

- **Minimum size.** The ACM logo "must be no smaller than .5 inch in height."
- **Clear space.** Half the height of the ACM Diamond on all sides. The diamond is never closer than one diamond width to other elements. Business cards may use half that clear space.
- **Colors.** The logo is reproduced in ACM Blue (PANTONE Process Blue C), black, or white. "Do not reproduce the ACM logo using the secondary color palette."
- **Improper use, verbatim list.** Do not substitute other fonts or typography styles for the ACM word mark. Do not outline the logo or draw a key line around it. Do not place the logo over complex imagery. Do not change the size relationship between the diamond symbol and the word mark. Do not use drop shadows or other graphic embellishments. Do not alter the gradients within the diamond. Do not alter the alignment of the word mark with the diamond. Do not reproduce the logo on an angle. Do not attach type or graphic elements to the logo. Do not use the ACM diamond symbol within headlines or text. Do not reproduce the logo using unauthorized colors. Do not reproduce the logo on a complex pattern. "No component of the ACM logo should be redrawn or altered in any way. Only use authorized digital art released by ACM."

The standards say nothing about student chapters. The chapter-specific rules are on the chapter policies page brand.md cites.

### Two ways a chapter logo can exist

1. **ACM's chapter lockup**, from the matrix page. Use it unaltered under every rule above. ACM Blue lives inside it and nowhere else on the page.
2. **A club-designed logo.** The chapter policy requires the words "ACM Chapter" to be legible on it. It must not reproduce or quote the ACM Diamond (only authorized art may carry it), it takes orange or ink rather than ACM Blue, and adopting it is a decision-log entry. The Rail is not a logo and does not become one (§2.4 of accessibility.md).

### The worked example of what not to do

`assets/acm-ai-hackathon-banner.png` (1170 x 156) and `assets/acm-ai-hackathon-icon.png` (1024 x 1024) assemble Google's blue, red, yellow, and green in a watercolor treatment around the words "ACM AI Hackathon". Three problems, any one of which would be enough: they read as Google, they use none of the chapter's colors, and the sibling GDG chapter lives under a rule that no four-color composition may exist anywhere near its marks, and the two clubs share officers and a room. Rule from here on: no chapter artifact uses that quartet. Whether the two files are retired is a decision for the decision log, and the Spring 2027 hackathon materials get rebuilt under this system. Do not delete them in the PR that adds this document.

### Placement

Flat surface color only. Not over photography, a gradient, or a pattern; the standards forbid all three for the ACM logo and the club's own marks follow the same rule. For ASRCC co-branding, required at any event ASRCC funds, keep the two marks visually separate at their own optical weights; a composite is a new mark.

## 1.6 Where the chapter's position differs from a plain reading

Three places where a strict reading of the sources and the chapter's choice differ. Resolve them here and do not relitigate per artifact.

**Orange as the lead.** ACM's secondary palette includes ACM Orange (PANTONE 138C, `#fc9200`) and says secondary colors are accents for ACM's communications, never for the logo. The standards do not address what a chapter's own identity may lead with, because they do not address chapters. The chapter leads with orange anyway, and with the website's `#ff4d00` rather than ACM's exact orange, on purpose: it is already the club's accent, it stays inside the family of colors ACM itself pairs with its logo, and it is not the one color that would make a chapter page read as ACM. Judgment call, recorded here and pending a brand.md entry.

**Inter instead of Myriad Pro.** The standards name Myriad Pro for ACM communications and allow Arial or Helvetica for digital applications. Myriad Pro is an Adobe-licensed face the chapter does not hold, and chapter documents are not ACM communications. Inter is OFL, is what the website already loads, and carries an `opsz` axis the type system depends on. Judgment call, recorded here and pending a brand.md entry.

**The website as reference.** brand.md says the website's colors are the reference until decided. This system reads them, measures them, derives from them, and does not change them. The website's own dark ground (`#050505`) is deeper than the docs' dark surface; that divergence is written down in foundations §2 and is an open item, not a conflict.

Everything else in the sources stands as written.

## 1.7 When it is genuinely unclear

Take the conservative path for this artifact, then resolve it: check [brand.md](../brand.md), then the ACM standards and the chapter policies (both linked in [links.md](../links.md)), then ask ACM through the chapters contact in links.md; the standards deck lists `mktg@acm.org` for typeface questions. Record the outcome in brand.md with a date, and log it in the [decision log](../../01-governance/decision-log.md) if a rule changed. The standards deck is version 1.0 from 2007; check at each semester start whether ACM has issued a newer one.

Last updated: 2026-09-01.
