# Foundations

Color, typography, space, grid, shape, elevation, and motion. Every value here resolves to a custom property in [tokens.css](tokens.css). Nothing else in the system names a raw color or size.

This system is provisional: [brand.md](../brand.md) still marks colors and typography `[TBD]` and names the website as the reference until a decision is logged. Everything below is built on that reference, measured, and labelled. The decision that makes it binding goes in the [decision log](../../01-governance/decision-log.md).

## 2. Foundations: color

## 2.1 What is sourced and what is derived

Sourced, from the club website's stylesheet (`src/app/globals.css` in `ACM-RCC/ACMWebsite`, read 2026-09-01). Measured this session against the system's own surfaces (light `#fdf8f7`, dark `#181514`, light ink `#221f1e`):

| Colour | Hex | CIE L\* | OKLCh hue | On light surface | On dark surface | Light ink on it | White on it |
|---|---|---|---|---|---|---|---|
| Racing orange (`--racing-orange`) | `#ff4d00` | 58.6 | 37.0 | 3.16:1 | 5.46:1 | 4.92:1 | 3.33:1 |
| Orange, gradient end (`--accent-to`) | `#ff8800` | 68.7 | 56.5 | 2.27:1 | 7.59:1 | 6.84:1 | 2.39:1 |
| Electric blue (`--accent-2`, marked "provisional" in the source) | `#4d9fff` | 64.6 | 254.1 | 2.58:1 | 6.68:1 | 6.02:1 | 2.72:1 |
| Green (`--success`, `--live`) | `#22c55e` | 70.2 | 149.6 | 2.16:1 | 7.97:1 | 7.18:1 | 2.28:1 |

Read that as one sentence: **the website's palette is a dark-mode palette.** The site runs white text on `#050505`, and every accent was tuned for that ground. None of the four clears 4.5:1 as text on a light page, and only the orange clears the 3:1 graphic floor there. That is why the light theme runs on derived tones and the raw hexes are reserved for two named fills and for hue anchors.

The site ships no red. The error ramp below holds a reference red hue (OKLCh 23.0, taken from `#e5484d` only to fix a hue) and is derived like everything else. Label: derived, not sourced.

Everything else in this system is derived by the club: a tone step on one of those hues, or a near-neutral tinted toward the lead hue. No derived color is more saturated than the source color it comes from.

ACM's own standards matter here too. ACM's primary palette is ACM Blue (PANTONE Process Blue C, `#0182ac`), black, and white; its secondary palette includes an ACM Orange (PANTONE 138C, `#fc9200`) sanctioned as an accent and forbidden on the logo. See [bright-lines.md](bright-lines.md) §1.3 for what that permits and forbids.

## 2.2 The two sanctioned fills

Two of the website's four hold 4.5:1 with our ink (`#221f1e`) and ship as raw fill tokens:

- `--acm-fill-orange: #ff4d00` (ink on it 4.92:1)
- `--acm-fill-green: #22c55e` (ink on it 7.18:1)

Blue clears the ratio (6.02:1) and is excluded on purpose. The website's own source calls it provisional, and a blue fill on a chapter page invites the one confusion this system exists to prevent: reading as ACM headquarters, whose color is blue. The gradient-end orange is excluded because it is a gradient stop and the system ships no gradient. Red ships no fill because there is no sourced red.

White on either fill fails body text (3.33:1 on orange, 2.28:1 on green). Filled brand buttons on the raw fills take ink labels.

## 2.3 Which color leads

**Orange leads.** `#ff4d00` is the primary hue. Three reasons, in order of weight: it is already the website's accent, so the docs and the site read as one club; it sits inside ACM's own sanctioned secondary palette (ACM Orange, PANTONE 138C), so it is a color ACM already lets its communications carry as an accent; and it is not ACM Blue, so a chapter page never reads as the parent organization. Blue as the lead would cost the club its clearest point of separation and would collide with the ACM logo the moment one lands on the page.

The positive case: this is a club about building, competing, and shipping on a Thursday afternoon, and the website already chose a color that reads as heat and speed. Nothing here overrides that.

This is a judgment call, not something ACM or the website ranks. The mechanics work with any hue as lead: swap the hue feeding `--acm-primary` and re-run the audit.

**One job each.**

| Colour | Role | Job | Never |
|---|---|---|---|
| Orange | `primary` | Links, buttons, active state, focus ring, the Rail. The color the club is recognized by. | n/a |
| Blue | `secondary` | Cross-references out to another doc or repo: the lab repo, the website, ACM's pages. That is the whole job. | Adjacent to primary in the same component. |
| Green | `live` | The live-now, confirmed, and passing marker, and the Check callout. | Decoration, headings, accents. |
| Red | `error` | Errors, destructive actions, and failure paths in a diagram. Semantic. | Near primary in one component. Orange and red are 14 degrees apart in OKLCh hue and are confusable, so an error is always labeled by a word or an icon, never by hue alone. |

**Three checks that keep it the chapter's**, all verifiable by looking at a page:

1. ACM Blue appears nowhere except inside the unaltered ACM logo.
2. No single component uses more than two hues.
3. Orange covers at least 70% of the non-neutral area on any surface. A page that is a spread of four colors at similar weight has failed regardless of hex, and a page that assembles Google's blue, red, yellow, and green has failed twice (§1.3).

The meeting types (regular, lab day, showcase) and the four pillars (Build, Compete, Learn, Connect) get no hue. [accessibility.md](accessibility.md) §2.4 gives the pillars a form instead (the Rail's Break), and meeting types are told apart by their words.

## 2.4 How the ramps were derived

Reproducible, so a future officer can regenerate rather than guess. Tone is CIE L\*. Hue and chroma come from OKLCh, which holds hue steady across lightness better than LCh(ab), particularly for blue. Each ramp holds its source hue, solves for the OKLab lightness landing on the target CIE L\*, and takes the largest in-gamut chroma under an envelope that peaks at mid tones and tapers to zero at both ends (0.42 of source chroma at T10, 0.62 at T20, 0.80 at T30, 1.00 from T40 to T60, 0.62 at T80, 0.38 at T90, 0.28 at T94, 0.20 at T96). Without the taper the deep tones clip to gamut-edge primaries and the light tones go neon. The method is the same one the sibling GDG chapter's system uses, so the two clubs' palettes are generated the same way from different anchors.

Tone deltas are a reasoning aid: 40 points is about 3:1, 50 points is about 4.5:1. Every pair in §2.5 was measured, not estimated.

**The neutral ramp.** Neutrals are tinted toward the lead hue at 37.0. Ink and page surfaces run at OKLCh chroma `0.005`, which reads as grey. **Container fills and outlines run at `0.012`**, which is where the tint becomes a decision a reader can see: a card reads as faintly warm paper against a near-white ground. That is the club's cheapest and most durable signature, and it is the one place the docs and the website (whose neutrals are pure grey) deliberately differ.

The container chroma of 0.012 is a judgment call tuned against generated output. Look at it on the A-210 projector before the showcase; a lecture-hall projector flattens low-chroma tints.

## 2.5 Contrast audit

Recomputed this session from the shipped hexes with the WCAG 2.x formula. 4.5:1 is the floor for body text; 3.0:1 for large text (24px, or 18.66px bold) and for non-text elements that carry meaning.

**Light.** 33 pairs, all pass.

| Foreground | Background | Values | Ratio | Min |
|---|---|---|---|---|
| `on-surface` | `surface` | `#221f1e` on `#fdf8f7` | 15.55 | 4.5 |
| `on-surface-variant` | `surface` | `#5c5958` on `#fdf8f7` | 6.59 | 4.5 |
| `on-surface` | `surface-container-highest` | `#221f1e` on `#ebe0dd` | 12.66 | 4.5 |
| `on-surface-variant` | `surface-container-highest` | `#5c5958` on `#ebe0dd` | 5.37 | 4.5 |
| `on-surface` | `surface-container-lowest` | `#221f1e` on `#ffffff` | 16.37 | 4.5 |
| `on-surface-variant` | `surface-container-lowest` | `#5c5958` on `#ffffff` | 6.94 | 4.5 |
| `primary` | `surface` | `#ae3200` on `#fdf8f7` | 6.13 | 4.5 |
| `primary` | `surface-container-highest` | `#ae3200` on `#ebe0dd` | 4.99 | 4.5 |
| `primary` | `surface-container-lowest` | `#ae3200` on `#ffffff` | 6.45 | 4.5 |
| `on-primary` | `primary` | `#ffffff` on `#ae3200` | 6.45 | 4.5 |
| `on-primary-container` | `primary-container` | `#661900` on `#ffdbd0` | 9.56 | 4.5 |
| `secondary` | `surface` | `#005eb4` on `#fdf8f7` | 6.12 | 4.5 |
| `secondary` | `surface-container-highest` | `#005eb4` on `#ebe0dd` | 4.98 | 4.5 |
| `on-secondary` | `secondary` | `#ffffff` on `#005eb4` | 6.44 | 4.5 |
| `on-secondary-container` | `secondary-container` | `#003469` on `#d9eaff` | 10.12 | 4.5 |
| `live` | `surface` | `#006e2e` on `#fdf8f7` | 6.10 | 4.5 |
| `live` | `surface-container-highest` | `#006e2e` on `#ebe0dd` | **4.97** | 4.5 |
| `on-live` | `live` | `#ffffff` on `#006e2e` | 6.42 | 4.5 |
| `on-live-container` | `live-container` | `#003e17` on `#c9f2d0` | 10.05 | 4.5 |
| `error` | `surface` | `#ba162a` on `#fdf8f7` | 6.16 | 4.5 |
| `error` | `surface-container-highest` | `#ba162a` on `#ebe0dd` | 5.02 | 4.5 |
| `on-error` | `error` | `#ffffff` on `#ba162a` | 6.49 | 4.5 |
| `on-error-container` | `error-container` | `#6c0d16` on `#ffe9e7` | 10.58 | 4.5 |
| `code-on-surface` | `code-surface` | `#33302f` on `#fcf1ee` | 11.81 | 4.5 |
| `inverse-on-surface` | `inverse-surface` | `#f7f3f1` on `#33302f` | 11.87 | 4.5 |
| `inverse-primary` | `inverse-surface` | `#ffb59f` on `#33302f` | 7.70 | 4.5 |
| `outline` | `surface` | `#7e7572` on `#fdf8f7` | 4.27 | 3.0 |
| `outline` | `surface-container-highest` | `#7e7572` on `#ebe0dd` | 3.47 | 3.0 |
| `outline` | `surface-container-lowest` | `#7e7572` on `#ffffff` | 4.49 | 3.0 |
| `focus-ring` | `surface` | `#ae3200` on `#fdf8f7` | 6.13 | 3.0 |
| `focus-ring` | `surface-container` | `#ae3200` on `#f6ece9` | 5.56 | 3.0 |
| `focus-ring` | `surface-container-highest` | `#ae3200` on `#ebe0dd` | 4.99 | 3.0 |
| `focus-ring` | `surface-container-lowest` | `#ae3200` on `#ffffff` | 6.45 | 3.0 |

**Dark.** 33 pairs, all pass.

| Foreground | Background | Values | Ratio | Min |
|---|---|---|---|---|
| `on-surface` | `surface` | `#ebe7e6` on `#181514` | 14.79 | 4.5 |
| `on-surface-variant` | `surface` | `#bfbbb9` on `#181514` | 9.53 | 4.5 |
| `on-surface` | `surface-container-highest` | `#ebe7e6` on `#3b3331` | 10.04 | 4.5 |
| `on-surface-variant` | `surface-container-highest` | `#bfbbb9` on `#3b3331` | 6.47 | 4.5 |
| `on-surface` | `surface-container-lowest` | `#ebe7e6` on `#100e0d` | 15.68 | 4.5 |
| `on-surface-variant` | `surface-container-lowest` | `#bfbbb9` on `#100e0d` | 10.11 | 4.5 |
| `primary` | `surface` | `#ffb59f` on `#181514` | 10.69 | 4.5 |
| `primary` | `surface-container-highest` | `#ffb59f` on `#3b3331` | 7.26 | 4.5 |
| `primary` | `surface-container-lowest` | `#ffb59f` on `#100e0d` | 11.33 | 4.5 |
| `on-primary` | `primary` | `#5e1700` on `#ffb59f` | 7.73 | 4.5 |
| `on-primary-container` | `primary-container` | `#ffdbd0` on `#852400` | 7.24 | 4.5 |
| `secondary` | `surface` | `#9fcaff` on `#181514` | 10.70 | 4.5 |
| `secondary` | `surface-container-highest` | `#9fcaff` on `#3b3331` | 7.26 | 4.5 |
| `on-secondary` | `secondary` | `#003061` on `#9fcaff` | 7.75 | 4.5 |
| `on-secondary-container` | `secondary-container` | `#cfe5ff` on `#004689` | 7.29 | 4.5 |
| `live` | `surface` | `#88d898` on `#181514` | 10.66 | 4.5 |
| `live` | `surface-container-highest` | `#88d898` on `#3b3331` | 7.23 | 4.5 |
| `on-live` | `live` | `#003915` on `#88d898` | 7.72 | 4.5 |
| `on-live-container` | `live-container` | `#beeec6` on `#005321` | 7.19 | 4.5 |
| `error` | `surface` | `#ffb3af` on `#181514` | 10.65 | 4.5 |
| `error` | `surface-container-highest` | `#ffb3af` on `#3b3331` | 7.23 | 4.5 |
| `on-error` | `error` | `#640b14` on `#ffb3af` | 7.70 | 4.5 |
| `on-error-container` | `error-container` | `#ffdad7` on `#8d1320` | 7.24 | 4.5 |
| `code-on-surface` | `code-surface` | `#e0dcdb` on `#251e1c` | 12.04 | 4.5 |
| `inverse-on-surface` | `inverse-surface` | `#33302f` on `#e6e1e0` | 10.10 | 4.5 |
| `inverse-primary` | `inverse-surface` | `#ae3200` on `#e6e1e0` | **4.98** | 4.5 |
| `outline` | `surface` | `#9d9491` on `#181514` | 6.12 | 3.0 |
| `outline` | `surface-container-highest` | `#9d9491` on `#3b3331` | 4.15 | 3.0 |
| `outline` | `surface-container-lowest` | `#9d9491` on `#100e0d` | 6.49 | 3.0 |
| `focus-ring` | `surface` | `#ffb59f` on `#181514` | 10.69 | 3.0 |
| `focus-ring` | `surface-container` | `#ffb59f` on `#251e1c` | 9.65 | 3.0 |
| `focus-ring` | `surface-container-highest` | `#ffb59f` on `#3b3331` | 7.26 | 3.0 |
| `focus-ring` | `surface-container-lowest` | `#ffb59f` on `#100e0d` | 11.33 | 3.0 |

### Numbers to watch

- **The tightest body-text pass in light is `live` on `surface-container-highest` at 4.97:1**, with `secondary` at 4.98 and `primary` at 4.99 right beside it. Nothing sanctions a darker surface than `surface-container-highest` in light mode. If someone adds one, every colored word on it stops passing.
- **The tightest pass in dark is `inverse-primary` on `inverse-surface` at 4.98:1.** The inverse surface is the one light island on a dark page; keep colored text on it to that single role.
- **`outline-variant` is 1.45:1 on the light surface and 1.94:1 on the dark surface.** That is deliberate and below 3:1. It is a divider and a decorative edge. It must never be the only thing defining the boundary of a control or of a status container. Use `outline` for that.
- **Container fills are nearly invisible on their own.** Against the light page ground, `primary-container` measures 1.22:1, `live-container` 1.17:1, `secondary-container` 1.16:1, and `error-container` 1.10:1. **Any container that carries status (a callout, an error field, a live marker) pairs with a 1px `--acm-outline` hairline.** The fill is a tint, and the hairline is the boundary that meets 1.4.11.
- **`--acm-live` may be a bare mark in light.** It measures 6.10:1 against the light surface, so a green dot beside a confirmed room is legal as a graphic. It still carries a word, because a mark that means something cannot mean it by color alone (SC 1.4.1).
- **A link is not distinguishable by color alone.** `primary` against body ink measures 2.54:1 in light and 1.38:1 in dark, both below the 3:1 that SC 1.4.1 needs for color-only distinction. Every in-prose link carries an underline (§3.7).

### The surface ladder

Adjacent steps sit at 1.045:1 to 1.169:1 (light: 1.108, 1.048, 1.056, 1.055; dark: 1.124, 1.045, 1.137, 1.169). They are meant to be barely perceptible: enough to read an edge without drawing a line. `surface` to `surface-container-highest` is 1.23:1 in light and 1.47:1 in dark. Depth is tone difference first, and tone survives dark mode, a classroom projector, and a printer in a way `box-shadow` does not.

## 2.6 Rules

**Do** use `primary` for the action the reader is meant to take. **Do not** use `secondary` to mean "slightly less important action." Blue means "this points somewhere else." A lower-emphasis action is an outlined or text `primary` button.

**Do** use `live` for a state that is true right now: the current phase on the showcase page, a confirmed room, a station whose harness prints PASS. **Do not** use green as a decoration or as a second accent.

**Do** use `error` for failure and destruction, and always with a word or an icon. **Do not** put an error control next to a primary control in one component; the two hues are close enough that a reader in a hurry reads them as one.

**Do** put white cards (`surface-container-lowest`) on the tinted page ground (`surface`). The tint is what lets the card read as lifted without a shadow.

**Do** derive a new color by picking a tone on one of the four hues and measuring it. **Do not** introduce a fifth hue, and never introduce ACM Blue as a UI color. This answers the `brand.md` line "Colors: [TBD]": the club's colors are the ramps here, pending the decision-log entry that makes them binding.

**Caution:** every `*-container` role is a fill and never a text color. `#ffdbd0` as text on `#fdf8f7` is 1.22:1.

## 2.7 Color in the markdown docs

**On GitHub**, the club's CSS does not apply. Color reaches those pages only through committed images and diagrams, so the rule there constrains assets rather than tokens.

**As standalone HTML**, the tokens apply directly.

There is a hard arithmetic limit worth publishing. GitHub's light canvas is `#ffffff` and its dark canvas is `#0d1117` (current as of 2026-09-01; if GitHub changes it, re-run this table). **No single color clears 4.5:1 against both.** An exhaustive sRGB search puts the true ceiling of `min(CR vs #ffffff, CR vs #0d1117)` at **4.350:1**. So:

- **Text inside artwork** cannot be one fixed color. Either ship two files behind a `<picture>` with `prefers-color-scheme` (§8.7 in [components.md](components.md) has the markup), or put the text in the markdown beside the image, which is cheaper and makes it searchable.
- **Strokes, fills, and marks** need 3:1, which one color can hold on both. Use these dual-mode tones, each computed this session as the best tone on its hue:

| Role in a diagram | Hex | On `#ffffff` | On `#0d1117` |
|---|---|---|---|
| Lead / primary mark | `#dd4201` | 4.33:1 | 4.37:1 |
| Cross-reference mark | `#247ad6` | 4.35:1 | 4.35:1 |
| Live / success mark | `#008c3d` | 4.36:1 | 4.34:1 |
| Failure path only | `#dc3f46` | 4.34:1 | 4.36:1 |
| Neutral rule / connector | `#7b7877` | 4.38:1 | 4.32:1 |

Never encode meaning in color alone in a diagram. Pair it with a label, a shape, or a dash pattern, and let a dashed stroke mean one thing across every diagram the club draws. Never use the lead mark and the failure mark on the same diagram without a shape difference; on a wiring diagram they read as two shades of the same wire.

## 2.8 Ligatures in code

Inter carries no logo glyphs and no ligature trap. JetBrains Mono does ship coding ligatures (`->`, `!=`, `>=` and the rest), and they are the reason the system sets `font-variant-ligatures: none` on `code, kbd, samp, pre`. The club's code blocks are teaching material and station cards. A student copies what they see, and a ligature shows a glyph that does not exist on the keyboard. Judgment call, and a cheap one: no code sample here needs ligatures.

## 2.9 Judgment calls in this section

- Orange as the lead. Neither ACM nor the website ranks it; the website uses it and ACM permits it as an accent.
- The container tint chroma of 0.012 and the surface chroma of 0.005, tuned by eye against generated output. Tone targets and every contrast number are computed.
- The dark surface at CIE L\* 7 (`#181514`) rather than the website's `#050505` (L\* 1.4). L\* 7 leaves room for a five-step container ladder above it and survives the A-210 projector. The website is a separate codebase and may keep its deeper ground; converging it on these tokens is an open item in [checklist.md](checklist.md).
- The error hue at OKLCh 23.0. The website ships no red, so the hue is fixed from a reference red and is derived rather than sourced.
- `#0d1117` as GitHub's dark canvas, current as of 2026-09-01.
- The website's electric blue is marked "provisional" in its own source. If the site drops or changes it, the `secondary` ramp is regenerated from the new anchor and this section re-audited.

---

## 3. Foundations: typography

## 3.1 The license answer

The website loads **Inter** and **JetBrains Mono** through `next/font/google` (read from `src/app/layout.tsx`, 2026-09-01). Both are SIL Open Font License faces in the Google Fonts catalog, both are self-hostable, and neither is anyone's brand face. That is the whole license answer, and it is a better position than the sibling GDG chapter has.

| Family | In catalog | License | Web-embeddable | Slot |
|---|---|---|---|---|
| **Inter** | Yes | OFL | **Yes** | brand and text |
| **JetBrains Mono** | Yes | OFL | **Yes** | code |
| Myriad Pro | No (Adobe) | Adobe Fonts subscription | Not without a license the club does not hold | out |
| Arial, Helvetica | System faces | n/a | n/a | fallback only |

**Why not Myriad Pro.** ACM's identity standards name Myriad Pro for ACM's own communications and allow Arial or Helvetica for digital applications and correspondence. The chapter's docs, posts, and flyers are the chapter's communications, not ACM's, and Myriad is a licensed Adobe face the club would have to pay for on every machine that opens a template. Inter is free, variable, and already on the website. Record this in `brand.md` as provisional until the decision is logged; the "Typography: [TBD]" row is answered by this section.

**Roboto is deliberately not recommended.** Roboto plus a blue plus a card grid reads as stock Android, and the club is one blue away from that at all times.

## 3.2 The optical seam, and how it is set

Inter exposes an `opsz` axis with a range of 14 to 32. The low end is the text design; the high end is the display design. Two drawings, one file, one continuous axis. That is the brand-face-versus-text-face split available for free, and it is one of the three things that make a club page recognizable, with the ledger line (§3.4) and the Rail ([accessibility.md](accessibility.md) §2.4).

**Set it with `font-optical-sizing: auto` and nothing else.** The UA then maps `opsz` to the used font size, clamped to the axis range, so a 40px headline gets the display drawing and 17px body gets the text drawing with no hard-coded axis anywhere. Pinning an axis value in `font-variation-settings` would break the fallback stack and create an inheritance trap, because `font-variation-settings` is a single replaced value and any child setting one axis drops the rest.

**`font-variation-settings` is not set anywhere.** Inter has no `GRAD` axis, so there is nothing to retune per theme. Light text on a dark ground blooms and reads heavier; if that shows on a real page, the fix is a weight step (400 to 450 for body on dark), and it has to be looked at rather than assumed. Open item.

## 3.3 Weights

Inter ships `wght` 100 to 900 with true italics in a second file. Three weights are in the system.

| Token | Value | Job |
|---|---|---|
| `--acm-weight-body` | 400 | Running text. Everything that is a sentence. |
| `--acm-weight-strong` | 500 | Every heading, label, and button. |
| `--acm-weight-loud` | 700 | Reserved. One use per page at most, and the emphasized tier. |

Every other weight exists in the font and is out of the system. The difference between 500 and 600 will not survive a handoff between officers. Hierarchy is carried by size, space, face, and color. Every heading is 500 and the reader tells them apart by size and by the seam.

**`font-synthesis: weight`**, not `none`. Weight 500 carries every heading, label, and button; `system-ui`, `-apple-system`, and `Segoe UI` do not all ship a real 500, and with synthesis fully off those headings render at 400 during the swap window and look unstyled rather than broken. Allowing weight synthesis and forbidding style synthesis gives a fallback heading that still reads as a heading and still makes a missing italic fail visibly.

**Emphasized tier.** A parallel set at identical sizes, one weight step heavier: 400 goes to 500, 500 goes to 700. Sizes and leading never change, so switching a card to emphasized cannot reflow a layout. Use it for the current phase on the showcase agenda, the station a student is at, a selected filter, the next lab day in the meeting plan. Two or three per page and it stops signalling anything.

## 3.4 The scale

Fifteen roles. Ordering is strictly monotonic at every viewport width. Fluid roles interpolate between a 360px and a 1440px viewport. Fixed roles never move; the reading size should not change when the window does, and the hierarchy should flatten on a phone rather than shrink proportionally.

| Role | Size | Line height | Tracking | Weight | Face |
|---|---|---|---|---|---|
| `display-lg` | 36 to 57px fluid | 1.05 | -0.02em | 500 | brand |
| `display-sm` | 28 to 40px fluid | 1.12 | -0.015em | 500 | brand |
| `headline-lg` | 24 to 32px fluid | 1.25 | -0.01em | 500 | brand |
| `headline-sm` | 20 to 24px fluid | 1.30 | -0.005em | 500 | brand |
| `title-lg` | 18px | 24px | 0 | 500 | text |
| `title-sm` | 15px | 20px | +0.005em | 500 | text |
| `body-lg` | 17px | 28px | +0.005em | 400 | text |
| `body-md` | 15px | 24px | +0.008em | 400 | text |
| `body-sm` | 13px | 20px | +0.01em | 400 | text |
| `label-lg` | 15px | 20px | +0.01em | 500 | text |
| `label-md` | 13px | 16px | +0.015em | 500 | text |
| `label-sm` | 11px | 16px | +0.06em | 500 | text, uppercase |
| `code-lg` | 15px | 24px | 0 | 400 | code |
| `code-md` | 14px | 24px | 0 | 400 | code |
| `code-sm` | 13px | 20px | +0.02em | 500 | code |

At a 390px viewport the fluid roles compute to 36.6 / 28.3 / 24.2 / 20.1, above `title-lg` at 18. At 1440px they reach 57 / 40 / 32 / 24. Ordering holds at both ends and everywhere between.

Brand and text are the same family here; the seam is carried by `opsz`, not by a second file. Both slots exist as tokens so the system can reface one without touching a component.

**The seam.** The scale is not generated from a modular ratio and does not pretend to be. Steps run about 1.42 at the display end and settle to roughly 1.11 to 1.20 through headline and title, then take one deliberate jump from `title-lg` (18px) down to `body-lg` (17px) where weight and tracking change instead of size. Around 20px the display drawing hands off to the text drawing and the tracking flips sign. Publishing that seam matters more than publishing a ratio; the ledger line below makes it a visible feature rather than an artifact.

Body is anchored at 17px, not 16px. Judgment call: these documents get read on a phone and projected in A-210 on Thursday afternoons, and 17px holds up in both. The website runs a fluid body near 16 to 19px; 17 sits inside that range.

**Line heights.** Display through headline run 1.05 to 1.30, tighter as size grows. Body and label run 1.5 to 1.65. Fixed roles are set in rem so leading lands on a 4px grid and text stacks against components without drift; fluid roles use a unitless ratio and land off-grid between the clamp ends, which is invisible because display type rarely meets a component edge.

**Tracking** is a function of size and flips sign around 20px: negative above, zero at `title-lg`, positive below, up to +0.06em on the uppercase `label-sm`. The website sets every heading at -0.03em, which is right for its 9rem display and wrong for a 20px subheading. Setting tracking to one value everywhere is the single most common reason student work looks flat.

## 3.5 Measure

| Token | Value | Use |
|---|---|---|
| `--acm-measure-prose` | `68ch` | Doc bodies, playbooks, meeting notes. About 620px at `body-lg`. |
| `--acm-measure-narrow` | `46ch` | Captions, callout bodies, sidebars, table cells. |
| `--acm-measure-display` | `20ch` | Headlines. Caps the line by character count so a hero headline wraps to two or three lines at every viewport. |

Keep prose between 45ch and 75ch. Above 75ch the eye loses the line return; below 45ch the rag gets ugly. Measure is capped independently of the layout grid: a section can be 1200px wide and its prose still 68ch. Every heading role gets `--acm-measure-display` whether it arrives as a class or as an `h1` through `h4` element, so a heading looks the same coming from markdown as from hand-written markup.

## 3.6 Details set once

**Tabular figures.** Inter documents `tnum`. Default figures are proportional. Turn on `font-variant-numeric: tabular-nums` for anything in a column or anything that changes: the budget, the kit order, attendance counts, the sixteen-row meeting plan, the phase clock on the showcase page, the serial readings on a station card. `[TBD: confirm the served latin subset carries tnum before relying on it in a build; read the GSUB list of the delivered WOFF2.]`

**No time colon feature.** Inter has no stylistic set for a raised time colon, so "12:50 to 1:50 PM" renders with the default colon. Nothing to verify and nothing to design around.

**Small caps.** Inter ships no true small caps. Do not design anything that depends on them; `label-sm` in uppercase with +0.06em tracking is the ledger voice instead.

**Italics.** True italics ship across the weight range. Use them.

**Do not** use `-webkit-font-smoothing: antialiased` to thin text on dark backgrounds. The website does; the docs do not. It affects macOS only and makes type inconsistent across platforms.

## 3.7 Links

`primary` against body ink is 2.54:1 in light and 1.38:1 in dark, both below the 3:1 that color-alone distinction requires. **Every link inside prose carries an underline**, at `text-underline-offset: 0.15em` and `text-decoration-thickness: from-font`. Standalone navigation links and button-styled links are exempt, because there the surrounding context is not prose and the affordance is the shape.

## 3.8 Fallback stack

The fallback is the system stack, not a second web font: `system-ui, -apple-system, "Segoe UI", sans-serif` for both text slots and `ui-monospace, SFMono-Regular, Menlo, monospace` for code. Inter is the primary and the license is clean, so there is no compliance case for a second catalog family. Arial and Helvetica, which ACM's standards allow for digital use, arrive through `system-ui` on the platforms that ship them.

**Open item:** the fallback face metrics differ from Inter, so text shifts when the webfont lands. `size-adjust` on an `@font-face` fallback fixes it, and the correct value has to be measured against the real fallback on the real platforms. Left as a TODO rather than invented.

## 3.9 Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400..700;1,14..32,400..700&family=JetBrains+Mono:ital,wght@0,400..700;1,400..700&display=swap">
```

Name every axis you intend to set; the URL selects which axes ship, not how far they run. `display=swap` so text renders in the fallback immediately. `[TBD: fetch the URL once and record the byte count and the number of @font-face blocks here, the way the GDG system did for its families; Google Fonts splits each face by unicode-range, so a Latin page downloads two files, not the whole list.]`

Self-hosting is also fine for both families, because their OFL files live in the `google/fonts` repo. The website self-hosts through `next/font`; a docs build may do either.

## 3.10 Open items

- `tnum` in the served latin subset: documented upstream, not read from the delivered file.
- Body weight on dark: 400 is the starting point; look at `body-lg` on `--acm-surface` and decide whether 450 reads better.
- Inline code at `0.9375em`: JetBrains Mono's x-height against Inter has not been compared.
- `size-adjust` on the fallback.
- The loading URL's byte count and block count.

---

## 4. Foundations: space, grid, shape, elevation

## 4.1 Space

**Base unit 4px, preferred step 8px, named by multiplier.** `--acm-space-6` is 6 x 4px = 24px.

Two things make 4px right. The type scale's fixed line heights are all 4px multiples, so a text block and a box beside it stack without half-pixel drift. And 4px is fine enough to handle real sub-8 cases (icon-to-label gaps, chip padding) without anyone inventing a 5px, while 8px is coarse enough that most layout decisions have one obvious answer.

Multiplier naming extends without renaming anything. T-shirt sizes run out the moment you need a step between two of them.

The scale is deliberately incomplete: fourteen steps, not thirty-two. Add a step when a real component needs one.

| Token | Value | Typical job |
|---|---|---|
| `--acm-space-0` | 0 | Reset |
| `--acm-space-0-5` | 2px | Optical nudge only. Never layout. |
| `--acm-space-1` | 4px | Chip inner padding, tight icon gap |
| `--acm-space-2` | 8px | Label to control, table cell padding, the Rail's width |
| `--acm-space-3` | 12px | Row padding in dense lists, the Break's height |
| `--acm-space-4` | 16px | Paragraph flow, narrowest page margin, control padding |
| `--acm-space-5` | 20px | Controls that need to clear an icon |
| `--acm-space-6` | 24px | Card padding, grid gutter, block separation |
| `--acm-space-8` | 32px | Feature card padding, space above h3 |
| `--acm-space-10` | 40px | Large card padding |
| `--acm-space-12` | 48px | Space above h2, desktop page margin |
| `--acm-space-16` | 64px | Inside hero blocks |
| `--acm-space-20` | 80px | Desktop section padding |
| `--acm-space-30` | 120px | Page bands |

**Padding, then gap, then margin.** Spacing lives on the parent container. A card carrying its own outer margin cannot be reused in a grid, a stack, and a sidebar without three overrides. The one sanctioned exception is prose flow between siblings, where `li + li` and `p + p` margins are the correct tool and are applied from a `--acm-flow-*` token so the value stays in one place.

**Positions are logical.** `inline-start` / `inline-end`, `block-start` / `block-end`. Free today, and the whole difference if the club ever publishes in a right-to-left script. It is also what puts the Rail on the correct edge without a second rule.

**Section rhythm has its own tokens.** The space between two sections is not made of component spacing. These three are the only fluid tokens in the system, because nothing aligns across a section gap so intermediate drift is invisible. Everything structural steps at breakpoints and stays on the grid.

**Prose rhythm is 2:1, above to below, at every heading level.** One ratio does all the sectioning work, which is why a well-set doc needs no rules, boxes, or background changes to mark a section boundary. It is the club's only sectioning device.

**Density: two settings.** Default for cards, event pages, and prose. Compact for the meeting plan, the kit table, and the roster. Compact changes *what appears* and not only the row height: at compact, a station card in a grid drops its "why this matters" line and keeps title, tier, and the parts count.

**Density is a user setting and never a viewport consequence.** Binding it to a breakpoint would make content disappear on phones, which is a content-parity failure. `data-density="compact"` is set by a control, not a media query.

## 4.2 Grid

**Three breakpoints: 600px, 1024px, 1440px. Columns 4, 8, 12.**

The breakpoint numbers are a judgment call. Three is the smallest ladder covering phone, small laptop or tablet, and desktop. Pick three; do not add a fourth.

The column counts are not a judgment call. 4 / 8 / 12 share divisors, so a span of 4 is full width at 4 columns, half at 8, and a third at 12. One number, correct at every tier, no breakpoint override. Halves and quarters come free everywhere. **Thirds exist only at 12 columns**, which is worth knowing before designing a three-up card row: it collapses to two-up at 8 and stacks at 4. The lab-day page's four station cards are a quarter each: four-up at 12, two-up at 8, stacked at 4.

| Tier | Columns | Gutter | Page margin |
|---|---|---|---|
| base (under 600px) | 4 | 16px | 16px |
| 600px and up | 8 | 24px | 32px |
| 1024px and up | 12 | 24px | 48px |

The gutter holds at 24px across both larger tiers rather than growing. Card padding is also 24px, so the gap between two cards and the gap inside one card agree and a row reads as one rhythm. The column width absorbs the extra viewport, which is the right answer: wider screens should get wider content, not wider air.

**Containers, chosen by what is inside them.**

| Token | Value | Use |
|---|---|---|
| `--acm-container-prose` | 640px | Body copy. Meeting notes, playbook prose. |
| `--acm-container-doc` | 896px | A document that also carries tables, code, and figures. A station card. |
| `--acm-container-content` | 1200px | Card grids, event pages, the lab-day page, the showcase project wall. |
| `--acm-container-wide` | 1440px | Hero media and full-bleed bands. |

The container's `max-width` measures the **content**, with page margin added on top. This requires `box-sizing: border-box`, which the reset in §5.1 ships. Without it the padding lands outside the max-width and the column band is wrong.

**Control sizing.** The visible control is 40px; the hit area is 48px minimum. Two tokens, and every button, checkbox, and icon link clears the touch minimum without anyone thinking about it.

## 4.3 Shape

Seven steps, indexed by roundness rather than by component size.

| Token | Value | Use |
|---|---|---|
| `--acm-radius-none` | 0 | Full-bleed media, table cells, dividers, the Rail |
| `--acm-radius-xs` | 4px | Inline code, tags, smallest chips |
| `--acm-radius-sm` | 8px | Inputs, code blocks, compact list cards |
| `--acm-radius-md` | 12px | Standard card in a grid |
| `--acm-radius-lg` | 16px | Feature card, framed screenshot, callout |
| `--acm-radius-xl` | 24px | Hero media, large panels, page-level containers |
| `--acm-radius-full` | 9999px | Actions and avatars only |

The website's own scale runs 8 / 16 / 24 / 32 / 48 plus pill. The docs system caps at 24px and the 32 and 48 steps are out of it. Judgment call: the larger steps belong to a marketing page with 9rem display type, and on a document they read as bubbles. The site is a separate codebase and keeps its scale until it converges (open item).

**Full round means you can press it.** Buttons, pills, pressable chips, avatars. Everything else uses the rectangular ladder. That single distinction does more affordance work than any hover state. If a container is fully rounded it reads as a control and someone will click it.

**Radius grows with footprint.** An 8px radius on a 640px panel looks like a rendering artifact; a 24px radius on a 32px chip looks like a bubble.

**The radius numbers are spacing numbers.** 4, 8, 12, 16, 24 all appear in the spacing scale, so corners and gaps agree automatically and there is one fewer scale to remember.

**Nesting math, two subtractions.** Inner radius equals outer radius minus the padding between them: a 24px card with 8px of padding around an inner panel gives that panel 16px. And inner radius equals outer radius minus the border width: an 8px container with a 1px border wants 7px inside. Worked example in tokens.css: a 12px card with 8px of inlay leaves 4px, `--acm-radius-xs`, on the media band.

**Asymmetric corners are first-class.** A card docked to a section boundary rounds only its free corners. Do not round a corner that has nothing on the other side of it. The Rail is never rounded; it is a bar, and a rounded bar is a pill, which means press.

**Radius is a spatial property.** When it animates it runs on the spatial track, never on effects.

## 4.4 Elevation

Five levels. Four are allowed at rest.

| Level | Depth cue | At rest | Use |
|---|---|---|---|
| 0 | Tone only | Yes | Page surface, section bands, a card on a tinted ground |
| 1 | Tone + shadow | Yes | Card separating from a same-tone ground; sticky header once scrolled |
| 2 | Tone + shadow | Yes | Dropdown, popover, filter panel |
| 3 | Tone + shadow | Yes | Dialog, modal sheet |
| 4 | Shadow | **No** | Interaction only: drag, and a genuine lift |

**Depth is tone first.** Separation comes from a step on the surface container ladder. If tone alone will not carry it, add a 1px `--acm-outline-variant` hairline. Shadow has exactly two jobs: protecting an element that sits over busy or patterned content, and signalling interaction. If two boxes need to look different and neither floats over anything, that is a tone or a hairline problem. The website's glass panels (a 3% white fill with a 12px blur) are a marketing treatment and are not in this system.

**The recipe is two layers and the ink is not black.** A tight key shadow for contact plus a wider ambient shadow for distance, tinted with the same ink as the text (`--acm-elevation-ink: 34 31 30`, which is `#221f1e`). Pure black shadows go grey and muddy when they stack.

**`--acm-elevation-0` is a zero-alpha shadow, not `none`.** `none` does not interpolate with a shadow list, so a transition from level 0 snaps instead of animating.

**Card hover goes to level 1, not level 4.** Spending the top of a five-level ladder on the most common hover in the system flattens the whole range, and a shadow with no `transform` reads as a pop rather than a lift.

**Dark is a separate answer, not an inversion.** Step the tone first: on a dark ground a shadow has almost nothing to darken, so move up one surface container role. Pair every floating dark surface with a hairline. When a shadow is genuinely needed (dialogs, dragged items), swap the ink to true black and raise the alpha. The dark alphas (0.44 key, 0.24 ambient) are chosen, not measured. **Verify them on the A-210 projector before the showcase**; a lecture-hall projector flattens anything under about 0.3 to nothing.

## 4.5 Sourced against chosen

Taken as method from the sibling GDG system, which read them from public engineering practice: the 4px base with an 8px preference and line heights on 4px multiples; padding before gap before margin; logical position naming; section rhythm as its own token; 2:1 heading space; the 4 / 8 / 12 column ladder; prose measure capped independently of the grid; a 40px visible control inside a 48px hit area; full-round for actions with rectangular surfaces; reusing one numeric scale for spacing and radius; tone before shadow; the two-layer tinted shadow at 0.30 key and 0.15 ambient; shadow on light and a tone step on dark; inner radius compensated for a border; asymmetric radii for docked panels; two densities where density changes content rather than only padding.

Chosen here and open to argument: the breakpoints 600 / 1024 / 1440; holding the gutter at 24px across both larger tiers; page margins 16 / 32 / 48; the four container widths and 640px for prose; seven radius steps capping at 24px against the website's 48; five elevation levels; every dark-mode alpha; the three `clamp()` rhythm ranges.

---

## 5. Foundations: motion

## 5.1 Two tracks

**Spatial** covers position, size, rotation, and corner radius. It may overshoot.
**Effects** covers opacity, color, and state layers. It never overshoots.

That split is the whole system, and it is what makes the reduced-motion override two lines rather than an audit.

## 5.2 Durations

Three tiers per track. Spatial runs roughly 2.2 times the effects duration at the same tier, which is the ratio at which a movement and the color change riding along with it feel like one event.

| Tier | Effects | Spatial | Use |
|---|---|---|---|
| fast | 90ms | 200ms | State layers, hover, press, focus ring |
| default | 140ms | 320ms | Card lift, disclosure, chip selection, radius morph |
| slow | 220ms | 480ms | Dialog and sheet enter, page-level transitions |

**Enter is slower than exit.** An exit uses the tier below its enter. A dialog enters on slow and leaves on default.

All chosen, not sourced. The website runs 0.3s / 0.6s / 1.2s because it is a scroll-driven marketing page; a document that moves at those speeds feels broken. The docs keep the shorter ladder and the ratio.

## 5.3 Easing

The two working curves are the website's own, so the docs and the site feel like one club under the cursor.

| Token | Curve | Use |
|---|---|---|
| `--acm-ease-standard` | `cubic-bezier(0.32, 0.72, 0, 1)` | Effects, always. Spatial moves that must land exactly. The website's `--ease-automotive`. |
| `--acm-ease-spatial` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Spatial only. Overshoots and settles. The website's `--ease-premium`. |
| `--acm-ease-exit` | `cubic-bezier(0.4, 0, 1, 1)` | Anything leaving. Accelerates out. |

`--acm-ease-spatial` is the only curve with a control point above 1, which is what produces the overshoot. Never apply it to opacity or color: a color that overshoots renders as a flash. The site's overshoot is larger than the GDG system's (1.56 against 1.28); on a 320ms card lift it reads as a small bounce, and that is the intended difference in character between the two clubs' pages.

## 5.4 Reduced motion

Zero the spatial durations, leave effects intact. Every state change survives, every movement stops. The website already ships a `usePrefersReducedMotion` hook; the docs ship the media query in tokens.css.

## 5.5 Icons

**Lucide**, at 24 x 24 with a 1.5px stroke and one locked weight everywhere. Two sizes: 24px inside a `lg` control and in prose, 20px inside `md` and `sm` controls.

Stroke icons on a 24 grid agree with the diagram stroke ladder the club will draw wiring and state-machine diagrams with (`[TBD: not yet written; base weight 1.5px, three weights, one job each]`), which means one drawing logic covers icons, wiring diagrams, and the state-machine sketches on a T2 card.

**Unverified in this document: Lucide's license.** It is understood to be ISC. Read the LICENSE file in the Lucide repository and record the result in `brand.md` before committing the dependency. If it does not check out, Phosphor and Heroicons are the alternates on the same terms.

Conventions: one base glyph plus a consistent modifier for a variant. Never the ACM Diamond as an icon (the standards forbid it inside headlines or text), never a Google or Gemini glyph, never the `{}` and `<>` code-punctuation glyphs that read as a stock CS-club identity. Decorative icons are `aria-hidden="true"`; an icon that is the only content of a control carries an accessible name.

---

Last updated: 2026-09-01.
