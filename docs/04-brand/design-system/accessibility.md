# Accessibility and visual voice

Every contrast ratio below was computed with the WCAG 2.x sRGB relative-luminance formula from the shipped hexes; the full 66-pair audit is in [foundations.md](foundations.md) §2.5 and the derivation script is reproducible. The Rail device was checked for collision against the ACM Diamond, the Google G, the Gemini spark, the four-dot Assistant mark, and the GDG on Campus lockups, and collides with none of them.

The CSS here is the explanation. The shipping copy lives in [tokens.css](tokens.css).

## Part 1: Accessibility

The goal is that anyone on the team can check a page in ten minutes and get a yes or no, without design judgment. Every rule below is either a number you can measure or a step you can run.

### 1.1 Contrast: the measured facts about the website's colors

The four colors the website ships were measured on 2026-09-01 against the system's own surfaces and ink. They are computed values, not quoted from anyone, and any of the tools in 1.9 returns the same number.

| Color | Hex | CIE L* | On light surface | On dark surface | Light ink on it | White on it |
|---|---|---|---|---|---|---|
| Orange (the accent) | `#ff4d00` | 58.6 | 3.16:1 | 5.46:1 | 4.92:1 | 3.33:1 |
| Orange (gradient end) | `#ff8800` | 68.7 | 2.27:1 | 7.59:1 | 6.84:1 | 2.39:1 |
| Blue (provisional secondary) | `#4d9fff` | 64.6 | 2.58:1 | 6.68:1 | 6.02:1 | 2.72:1 |
| Green (live) | `#22c55e` | 70.2 | 2.16:1 | 7.97:1 | 7.18:1 | 2.28:1 |

Five rules follow directly from that table, and they are not negotiable:

1. **No website color is a body-text color on the light surface.** Best of the four is orange at 3.16:1. Brand-colored text or a brand-colored link on a light surface uses the derived `primary` role, which measures 6.13:1 on the surface and 4.99:1 on the deepest container.
2. **Green and the gradient orange never carry text on the light surface and never sit there as a meaningful shape.** At 2.16:1 and 2.27:1 they fail even the 3:1 non-text floor. On light they are fills that take ink, or they are absent. The derived `live` role is a different color and does clear 3:1 as a bare mark, at 6.10:1.
3. **Filled brand buttons on the raw fills take ink labels, not white ones.** White on `#ff4d00` is 3.33:1 and fails body text. Ink on it is 4.92:1 and passes; ink on green is 7.18:1. The button the system actually ships is white on the derived `primary`, at 6.45:1. The raw fills are for large areas, not controls.
4. **Error is never told apart from primary by hue alone.** The website ships no red, so the system's error red is derived, and orange and red are 14 degrees apart in OKLCh hue. Every error state carries a word or an icon, and error never sits beside primary in one component.
5. **All four website colors clear body contrast on the dark theme** (5.46:1 to 7.97:1 against the dark surface). Dark mode is the permissive case. Light mode is where things break, so check light first.

Design-time shortcut, so nobody has to open a tool for every decision: a 40-point gap in CIE L\* gives about 3:1 and a 50-point gap about 4.5:1. The color section is built on tonal roles, so pairing a tone-40 role against a tone-90 role is safe by construction. Treat the shortcut as design-time only and measure before publishing; the 50-point version does not hold in the worst case.

### 1.2 What has to be measured, and what does not

- **4.5:1** for body text, and for any text under 24px regular or 18.66px bold.
- **3:1** for large text at or above 24px regular / 18.66px bold, and for non-text: icons that carry meaning, focus rings, form-field borders, chart marks, the state that distinguishes a selected badge from an unselected one.
- **No minimum** for purely decorative graphics, disabled controls, logotypes, and text inside a photograph.

The traps specific to this club's page set:

- The club name line and the "Funded by ASRCC" line are **body text** and must measure 4.5:1. Do not set either in a light grey at 11px in the footer. One is what keeps the chapter from reading as ACM and the other is a funding condition; both get the same contrast floor as a paragraph.
- Station cards, badges, and stat tiles from the components section usually put a label on a tinted container. Measure the label against the container, not against the page.
- Text over event photography has an unmeasurable background. Never set text directly on a photo. Put it on a solid or near-solid scrim panel and measure against the scrim, or place it below the image entirely. The scrim must be opaque enough that the measurement holds at the lightest pixel in the crop.
- Code blocks: syntax highlighting is color-only by definition. Every token color in the code-block theme must clear 4.5:1 against the code surface. Comments in particular tend to fail, and the lab's starter files are mostly comments.
- Dark theme is a second full pass, not an inversion you can assume works.

### 1.3 Focus indicators

Never `outline: none` without a replacement in the same rule. The one legitimate pattern is `:focus:not(:focus-visible) { outline: none }` paired with a `:focus-visible` rule that draws a real ring.

What tokens.css ships:

```css
:focus-visible {
  outline: 3px solid transparent;
  outline-offset: 2px;
  box-shadow: 0 0 0 2px var(--acm-focus-gap), 0 0 0 5px var(--acm-focus-ring);
  border-radius: inherit;
}
```

The ring is `primary`. Measured against the surface it is 6.13:1 in light and 10.69:1 in dark; against the deepest container it is 4.99:1 and 7.26:1. All clear the 3:1 that WCAG 2.2 SC 1.4.11 requires, and the 2px gap ring shows the surface behind the control so the ring needs one measurement per ground rather than one per component. The transparent `outline` is what forced-colors mode substitutes a system color into, because `box-shadow` is dropped there.

The alternative is an `on-surface` outline (15.55:1 light, 14.79:1 dark), which never collides with a brand-colored fill sitting underneath it. The system ships the primary ring because the ring is the club's color and the gap keeps it legible on every container. The one case the primary ring cannot handle is a control sitting on a `primary` fill; that control takes the `on-surface` outline instead.

Rules around it:

- If a control sits inside a tinted container, measure against the container.
- **No interactive control sits directly on a photograph.** The photo makes the ring's contrast unmeasurable. Give the control a solid fill first.
- Never remove focus from the skip link, from custom-styled checkboxes and radios, or from anything with `tabindex="0"`.
- SC 2.4.11 Focus Not Obscured is AA in WCAG 2.2: a focused control must not be fully hidden behind a sticky header or footer. If the nav is sticky, add `scroll-margin-top` equal to the nav height on every focusable element, or drop the stickiness on small screens.
- The ring is visible on the dark theme, on the light theme, and under Windows High Contrast Mode. Test the last one with Chrome DevTools rendering panel, "Emulate CSS forced-colors".

### 1.4 Target sizes

WCAG 2.2 SC 2.5.8 (AA) requires a minimum target of **24 by 24 CSS px**, with an exception if the target has enough spacing that a 24px circle centered on it does not intersect another target's circle. Inline links inside a sentence are exempt.

Club floor, which is stricter than AA on purpose because these pages get used on phones at Club Rush and at a lab table:

- **44 by 44 CSS px** for anything a person taps on a phone: nav items, the Discord link, the RSVP button, agenda-row links, footer social icons.
- **24 by 24** absolute minimum for dense desktop-only controls, and only with 24px of clear space.
- Pad the target, do not grow the icon. A 20px icon inside a 44px hit area is correct.
- Icon-only buttons need an accessible name: `aria-label="Open menu"` or visually hidden text. An icon-only button with no name is invisible to a screen reader.

### 1.5 Semantic structure, headings, landmarks

**One `h1` per page**, and it is the page's actual title. On an event page that is the event name, not the club name. On a lab day page it is the day, not "Microcontroller lab".

**Never skip a heading level.** `h2` to `h4` is a defect. Screen-reader users navigate long meeting and lab pages by heading, and the heading tree is the table of contents. It also has to hold in the markdown docs, where GitHub builds the file's outline from the same tree.

Heading level is structure, not size. If an `h3` needs to look big, the type section has a role for that. Do not pick the level by how it looks.

**Landmarks on every HTML page:**

```html
<a class="acm-skip" href="#main">Skip to main content</a>
<header>
  <nav aria-label="Main"> ... </nav>
</header>
<main id="main" tabindex="-1"> ... </main>
<footer> ... </footer>
```

- `tabindex="-1"` on `<main>` is required or the skip link will not move focus in Safari.
- If there are two `<nav>` elements on a page, each needs a distinct `aria-label` ("Main", "Stations", "Footer").
- Use `<ul>` for lists of things. The agenda is a list. The station grid is a list. Screen readers announce "list, 4 items", which is real information.
- Tables get `<th scope="col">` or `scope="row"`, and a `<caption>`. Never use a table for layout.
- `<time datetime="2026-12-10T12:50">` for every date and time on event pages.
- The club name and the ASRCC line are real text in the footer. Not an image, not a background, not `title` attribute text.

### 1.6 Keyboard

- Tab order equals DOM order. Never use a positive `tabindex`. Never reorder with CSS `order` or `grid-area` in a way that separates visual order from DOM order for interactive content.
- Everything clickable is a `<button>` or an `<a href>`. A `<div onclick>` is not keyboard reachable and cannot be fixed with CSS.
- Whole-card links: put one `<a>` around the card title and stretch it with `::after { position: absolute; inset: 0 }`. Do not nest other links or buttons inside a clickable card; that creates an unreachable control.
- Disclosure widgets (a collapsible agenda, a FAQ, a station's common-bugs list): `<button aria-expanded="true|false" aria-controls="id">`. Escape closes. Focus returns to the trigger.
- No keyboard traps. If a dialog is ever added, focus moves into it, is trapped inside while open, and returns to the opener on close.
- Skip link:

```css
.acm-skip {
  position: absolute;
  left: -9999px;
}
.acm-skip:focus {
  left: var(--acm-space-4);
  top: var(--acm-space-4);
  z-index: 100;
  /* solid surface fill, on-surface text, focus ring per 1.3 */
}
```

Do not use `display: none` or `visibility: hidden` to hide the skip link. Both remove it from the tab order, which defeats the point.

### 1.7 Alt text policy

The rule that decides every case: **alt text replaces the image for someone who cannot see it.** It is not a caption, not a filename, and not SEO.

| Case | Alt |
| --- | --- |
| The ACM chapter logo (once one exists), linked to the home page | `alt="ACM Student Chapter at Riverside City College"`. The alt names the destination, because the accessible name of a link is what a screen reader announces. Never `alt="logo"`. |
| The same logo sitting next to the club name already in text | `alt=""`. Do not make a screen reader hear the name twice. |
| The Rail (Part 2) | `aria-hidden="true" focusable="false"` on the inline SVG, or `alt=""` on an image. It is decorative and the pillar name is always in text beside it. |
| The QR codes in `assets/` (`rcc-acm-qr-code.png`, `rcc-acm-qr-dark.png`) | The URL must appear as real text on the page. The alt says where it goes, which needs brand.md's `[TBD: confirm which URL it encodes]` resolved first; until then `alt="QR code; the link is printed beside it"`. A QR code with no text URL is unusable by half the audience. |
| A station wiring photo (overhead, hardware only, no people) | Names the station and what is wired: `alt="Overhead photo of station B wired for the T2 cyclone: four LEDs on GP10 to GP13, one button on GP14"`. It doubles as the wiring check. Hands in frame are fine; faces are not, and then the photo falls under event photography below. |
| A card thumbnail that is pure decoration | `alt=""` |
| A diagram (a state machine, a pin map, the semester map) | Short `alt` naming what it shows, plus the same content in text or a table nearby. A diagram whose information exists nowhere else in text is a defect. Mermaid diagrams in markdown need the same treatment. |
| A slide screenshot with text on it | The alt carries the slide's text. If it is more than about 150 characters, put it in the page body and use `alt=""`. |
| Event photography | See 2.2. |

**Alt text for event photography, which is where accessibility and the privacy policy meet.**

The [privacy policy](../../01-governance/privacy-and-public-repo-policy.md) says members who are not officers are never named, and that anything beyond an officer's name and role needs its own consent. That constrains alt text directly:

- **Alt text never names an individual.** Not the speaker, not the members in frame. Write roles and counts: `alt="Two students at a station board in BLCIS A-210, one holding the laminated card"`.
- **Alt text does not describe race, gender, body, or disability** unless it is the point of the image, which for this club it never is.
- Describe what is happening, not what is present. "A team pressing the run button on the showcase board while the projector shows the serial report" beats "a group of people in a room".
- Aim for one sentence. If the photo needs a paragraph, it needs a caption too, and the caption is real text under the image.
- A caption and an alt should not be identical. If the caption already says it, `alt=""` and let the caption do the work.

### 1.8 The markdown docs, rendered on GitHub

GitHub strips `style` attributes and most inline HTML, so none of the CSS above reaches the repo view. What survives is structure, and structure is where the accessibility lives anyway.

- One `#` per file, at the top. Never skip a level. `markdownlint` rule **MD001** (heading-increment) catches this.
- Every image has alt text. `markdownlint` rule **MD045** (no-alt-text).
- No bare URLs as link text. "See the privacy policy" with a real relative path, never "see here". Bare URLs pasted from rcc.edu are tolerated by this repo's lint config, and a bare URL is never the link text of a sentence.
- Tables get a real header row. GitHub renders the first row as `<th>` only if the delimiter row is present.
- Use GitHub's alert syntax (`> [!NOTE]`, `> [!WARNING]`, `> [!IMPORTANT]`) rather than bold-and-emoji. Alerts render with a text label, so the meaning survives without color.
- **Never encode status in color or emoji alone.** A green check next to a station is invisible in a screen reader announcement that reads "white heavy check mark". Write the word: `Status: confirmed`.
- Code fences always carry a language tag. Highlighting is color-only, so never write a code sample whose meaning depends on the highlight. This matters most in the lab's starter files, where the TODO markers must be words, not colors.

The same file published as standalone HTML gets the full treatment in 1.5. The markdown-to-HTML build must emit a single `h1`, `<main>`, and a skip link. If the build is a static-site generator, that belongs in the layout template, once.

### 1.9 Pre-publish verification procedure

Run this before any page goes public, and before the showcase page on 2026-12-10 in particular. About fifteen minutes for a page you have already checked once, forty-five for a new template.

**Step 1. Automated, in the browser (5 min).**

- **axe DevTools** (Deque, free browser extension). Run "Scan all of my page". Zero critical and zero serious issues is the bar. axe catches roughly a third of WCAG issues, so this is a floor, not a pass.
- **Lighthouse** accessibility category, built into Chrome DevTools. Same caveat: a 100 score is not a passing grade, it is the absence of the automatable failures.
- Optionally **WAVE** (WebAIM extension) as a second opinion; it renders errors in place, which is easier to act on.

**Step 2. Contrast, on the specific pairs (5 min).**

- Chrome DevTools color picker shows the ratio inline when you click any `color` swatch in the Styles pane. Use it on: body text, every button label, the club name and ASRCC lines in the footer, badge labels, code-block comments, the focus ring, form-field borders.
- For a pair you cannot inspect (text over a scrim, a printed flyer), use the **TPGi Colour Contrast Analyser** desktop app with its eyedropper, or the **WebAIM Contrast Checker** at webaim.org/resources/contrastchecker/ with the hex values.
- Repeat the whole step with the dark theme active. DevTools rendering panel, "Emulate prefers-color-scheme: dark".

**Step 3. Keyboard, hands off the mouse (3 min).**

- Load the page, press Tab once. The skip link must appear. Press Enter. Focus must land in `<main>`.
- Tab through the entire page. Every stop must be visible, in a sensible order, and never hidden behind the sticky nav.
- Activate every control with Enter and Space. Every collapsible opens and closes. Escape closes anything that opens.
- Tab past the last element. Focus should reach the browser chrome, not loop back into a trap.

**Step 4. Structure (2 min).**

- Chrome DevTools, Elements panel, Accessibility pane: check the computed name of every image, button, and link. Anything named "image", "button", or a filename is a defect.
- Firefox Accessibility Inspector has a "Check for issues" dropdown with contrast and text-label passes that catch different things than axe does.
- Validate the markup: **W3C Nu HTML Checker** at validator.w3.org/nu/. Duplicate IDs and unclosed tags break assistive tech in ways nothing else will report.

**Step 5. Reflow and zoom (2 min).**

- Set the viewport to **320 CSS px wide**. The page must be usable with vertical scrolling only, no horizontal scroll (WCAG 1.4.10 Reflow). Tables and code blocks are allowed to scroll horizontally inside their own container; the page body is not.
- Browser zoom to **200%** at 1280px. Nothing clipped, nothing overlapping (1.4.4).

**Step 6. Motion and preferences (1 min).**

- DevTools rendering panel, "Emulate prefers-reduced-motion: reduce". Every transition and animation the motion section defines must stop. Check that nothing becomes unusable because a transition was doing load-bearing work.
- "Emulate CSS forced-colors: active". Text readable, focus ring visible, no content lost.

**Step 7. Screen reader, once per template rather than once per page (10 min).**

- **VoiceOver** on macOS (Cmd-F5, free, already installed). Use rotor (`VO-U`) to list headings, then links, then landmarks. The heading list should read like a table of contents. The link list should make sense with no surrounding context.
- **NVDA** on Windows (free, nvaccess.org) if anyone on the team has a Windows machine. It behaves differently enough from VoiceOver to be worth one pass on the site's main template.

**Step 8. CI, so this does not depend on anyone remembering (setup once).**

- `markdownlint-cli2` already runs over every `.md` in CI and in `scripts/check.sh`, with MD001 and MD045 on by default. This protects the repo docs, which is most of what the club actually ships.
- `pa11y-ci` or `@axe-core/cli` over the built HTML in the same Action, once a build exists. Fail the PR on serious and critical.

**Step 9. Two things a tool cannot check.** Read the page and confirm: no information is carried by color alone (WCAG 1.4.1), and no instruction refers to a control by shape or position alone ("the round button", "the box on the right").

---

## Part 2: Visual voice

### 2.1 Iconography

**Set: Lucide.** Drawn on a 24 grid as strokes. The GDG system's files disagree with each other about the set (its foundations and components name Lucide, its accessibility file names Phosphor); this copy says Lucide everywhere and lists Phosphor as the alternate on the same terms, with Heroicons behind it.

**Stroke: 1.5px, one weight, everywhere.** Two sizes: 24px inside a large control and in prose, 20px inside medium and small controls. Icons on these pages get projected onto the A-210 wall and read on a phone at a lab table. If 1.5px thins out on the projector, the sanctioned change is one system-wide step to 2px, recorded in foundations, never a per-icon adjustment. One weight is also the only rule a rotating officer team can follow correctly.

**Why not Material Symbols.** It is openly licensed and technically available, so this is not a legal call. It is that Material Symbols silhouettes are one of the strongest signals of Google authorship in existence, and this club already has two Google-looking files in `assets/` it needs to move away from. Stroke icons on a 24 grid read as not-Material at a glance, and they agree with the diagram stroke ladder, so one drawing logic covers icons and diagrams.

**Why not the ACM Diamond.** The standards say not to use it within headlines or text, and an icon slot is text.

**Licensing position, stated plainly:**

- Lucide's license is understood to be ISC. **Unverified in this document.** Read the LICENSE file in the release you vendor and record the result in `brand.md` before committing the dependency.
- Vendor the SVGs the club actually uses into `assets/icons/`. Do not hotlink a CDN and do not ship a webfont of the whole set.
- Commit the upstream `LICENSE` file alongside them at `assets/icons/LICENSE`.
- Add a one-line attribution row to `docs/04-brand/brand.md` naming the set, the version, and the license.
- Icons are never modified beyond color and size. If a needed icon does not exist in the set, use a word instead of drawing one.

**Usage rules:**

- An icon never appears alone as the only label for an action unless it has an `aria-label` and a tooltip.
- Icons are `currentColor`, always. They inherit the text color and therefore inherit dark mode and forced-colors for free.
- Meaningful icons need 3:1 against their background. Decorative ones do not, but hold them to 3:1 anyway so they survive a projector and a grayscale print.
- One icon per row maximum. Icons on both the left and the right of an agenda row is noise.
- Decorative icons are `aria-hidden="true"`; an icon that is the only content of a control carries an accessible name.

### 2.2 Imagery and photography

The club photographs students at meetings, at lab days, and at the ICPC regional site it hosts. The [privacy policy](../../01-governance/privacy-and-public-repo-policy.md) already forbids photos of people without written consent in the repo, and routes photos of people to the shared drive. This section says how consent is captured and what happens to the rest, so the policy is operable rather than aspirational.

**Default shot list, which makes most of the consent problem disappear.** For public pages, shoot so that nobody is identifiable:

- The overhead wiring photo of each station, which the lab's facilitator guide already requires. Hardware only. It is the club's native image and the one no other club has.
- The room from the back, over shoulders, toward the projector showing the serial report.
- Hands on a station board, hands on a breadboard, hands holding a laminated card.
- The whiteboard, the slide, the agenda on the wall, the check-in table, the station box with its lid off.
- Wide room shots where faces are small and turned away.

These need no consent, go in `assets/` if under 1 MB, and carry the pages perfectly well. Identifiable portraits are the exception, not the default.

**The ICPC regional site is a special case.** The contest has its own organizers, and the club is a host, not the owner of the room. Confirm with the contest directors listed in [links.md](../links.md) what may be photographed and published before shooting anything there. `[TBD: record what they say in the ICPC playbook.]`

**How consent is captured.** Three layers, all of which produce something the club can point to later:

1. **Door signage.** A printed card at the entrance of BLCIS A-210 on any day photography is happening: what is being photographed, where it may be published (club web pages, the public GitHub repo, Instagram, ASRCC reports), and where to sit or stand to stay out of frame. Signage is notice, not consent. It does not authorize publishing an identifiable face.
2. **The opt-in slip, which is the actual consent.** A half-page paper slip at check-in, or a separate unticked checkbox on the RSVP form. It must state, in the person's own reading: the club's name, that photos may appear on public web pages and in a public GitHub repository that is permanently archived and indexable, that consent may be withdrawn at any time by messaging an officer, and it must capture a printed name, a signature or a form submission, and a date. It is a separate action from RSVPing. A pre-checked box is not consent, and neither is a Discord post.
3. **The badge sticker, which is how the photographer knows in the moment.** Anyone who signs the slip gets a colored dot on their name badge. **The photographer's rule: if a face is identifiable and there is no dot, that frame does not leave the drive.** Nobody has to remember names or cross-reference a list mid-event.

**Where the paperwork lives.** The signed slips and the form responses go to the club's shared drive, never to the repo, because they carry names and signatures and the policy forbids both. What goes in the repo is what the policy already prescribes for officer names: a line in the semester's `handoff.md` under account and consent records, recording the date and the count. Reference published photos by filename, never by subject name.

**Before publication, check that the college does not already have a media release form.** RCC Student Activities very likely has one, and using the college's existing instrument is better than the club inventing one. Treat this as `[TBD: confirm with Student Activities whether an RCC media release form exists and supersedes the club slip]`. Do not ship the slip until someone asks.

**Minors.** RCC has dual-enrollment high school students. A person under 18 cannot give this consent themselves. Default rule: **if a subject may be under 18, no identifiable photo is published, period**, unless a guardian release has been obtained through the college's process. Do not attempt to assess age visually and do not build a workaround.

**What happens to photos without consent:**

- They live in a `restricted/` subfolder of the event's drive folder, with sharing set to club officers only.
- They are used internally: a retro deck shown live, an ASRCC report presented in a meeting. They are never uploaded to the repo, never on a public page, never on Instagram, never in a slide deck that gets a public link.
- They are deleted at the end of the following semester unless someone has a stated reason to keep them. Retention is a liability, not an asset.

**Before any photo is published:**

- Strip EXIF, including GPS. `exiftool -all= photo.jpg` is one command and it is not optional; phone photos carry location.
- Confirm no faces without dots, no screens with visible personal data, no whiteboards with a phone number on them, no badges with legible full names.
- Confirm under 1 MB if it is going in the repo, per the policy.
- Write alt text per 1.7: no names, no demographic description.

**If a photo is published without consent, or consent is withdrawn:** unpublish the page immediately, then follow the removal procedure already written in the privacy policy. Deleting the file in a new commit is not removal; it requires `git filter-repo`, a force push with branch protection temporarily lifted, a GitHub Support cache purge, everyone re-cloning, and a decision-log row that does not describe the data. That procedure is expensive, and its cost is exactly the argument for the badge-dot rule.

**Never used, on any surface:**

- Stock photography of generic people at laptops. It reads as a template and it is a lie about who is in the room.
- AI-generated images of people. A chapter that teaches evidence and engineering does not fabricate its own audience.
- ACM's stock "community" and "innovation" photography from the standards deck. It is ACM's, and it would make the page read as ACM's.
- Any Google product screenshot, Pixel photography treatment, or Google marketing imagery. That is the imitation line the two hackathon files already crossed.

### 2.3 Illustration, with no illustrator on the team

The club has no illustrator and will not have one next semester either. So the answer is not "keep it simple", it is **no freehand illustration exists in this system.** Three sanctioned image types, all of which are made by editing text.

**1. Type as the image.** The default hero for every event page, meeting page, and social card: the title set at the type section's display role on a flat surface role, with the Rail (2.4) at the inline-start edge, and the date and room in the label role. No picture at all. This is the highest-quality output the club can reliably produce, because it is just the type system doing its job.

**2. Diagrams, not drawings.** Mermaid, in fenced code blocks. GitHub renders it natively in markdown, and the standalone HTML build can render it too. Use it for the semester map, a station's state machine, the pin map, the showcase run of show, the officer handoff chain. It is text, so it diffs in a PR, and it survives an officer transition. Every diagram gets alt text and a text equivalent per 1.7.

**3. The Rail field.** A low-contrast background made from the device (2.4): vertical hairlines in `--acm-outline-variant` at the grid's column positions, exactly one of them carrying the page's Break. It is a `repeating-linear-gradient` plus one Rail, nobody draws anything, and it is used only behind a hero or on the showcase page. Judgment call: look at it on the A-210 projector before the showcase, because a lecture-hall projector may flatten the hairlines to nothing.

**Template contract.** Ship one SVG template per export size in `assets/templates/`, one per row of the size table in [assets.md](assets.md), which owns every dimension and safe zone. Each template contains text nodes with placeholder strings, the Rail, and nothing else. An officer opens it in a text editor, changes the strings, and exports. No drawing tool, no design decisions, no way to break the grid. This is the same discipline that makes the club's markdown docs survivable: the author picks meaning, the system picks measurements.

**Not used:** clip art, 3D blob renders, gradient meshes, watercolor splashes, hand-drawn doodle borders, isometric illustration packs, and anything with the soft rounded optimistic character of Google's AI illustration style. Watercolor is named on purpose: it is what the two hackathon files use.

### 2.4 The signature device: the Rail

This is the piece that makes the pages the club's own rather than a de-branded template. It is one geometric construction, it costs nothing to produce, and it does actual work in the information architecture instead of just sitting in a corner.

**Where it comes from.** The website's own share card (`src/app/opengraph-image.tsx`, read 2026-09-01) is a 1200 x 630 card with a 24px `#ff4d00` left border on a near-black ground, the club name in white, and the four pillars beneath. That left border is the Rail. The system adopts it rather than inventing something new, and adopting it as the system's device is a judgment call that needs a decision-log entry.

**The form.** A solid vertical bar in `--acm-primary`, flush to the inline-start edge of a block, full block height. One width per medium. Fill only, no stroke. Never a gradient, never rounded, never rotated.

| Medium | Rail width |
| --- | --- |
| Screen components: hero, script block, the left edge of a Warning or Check callout | `--acm-space-2` (8px) |
| Share card, 1200 x 630 | 24px (2% of the width, matching the website's card) |
| Print | 0.25 in |

**The Break, one variable.** A gap in the Rail whose vertical position encodes the pillar of the page. The gap height is `--acm-space-3` (12px) on screen. Set once on the page's root element; `--acm-rail-break` carries the percentage.

| Pillar | `data-pillar` | `--acm-rail-break` |
| --- | --- | --- |
| Build | `build` | `20%` |
| Compete | `compete` | `40%` |
| Learn | `learn` | `60%` |
| Connect | `connect` | `80%` |
| Club pages, footer, anything without a pillar | omit | unset; the bar runs solid |

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

Verify the gap edges in a browser at 1x and at 2x device pixel ratio before shipping; a 12px gap on a percentage position can land on a half pixel.

Someone who has read three meeting pages will recognize which pillar a page belongs to before reading the heading. Nothing else in the system does that, and it costs one line of CSS per page. Which pillar each meeting type maps to is an open item in [checklist.md](checklist.md), not a decision this file makes.

**Why this is derived from nothing ACM or Google owns.**

- It is not a diamond, a rotated square, or a gradient, so it cannot be mistaken for the ACM Diamond, and it never quotes that geometry.
- It is not a spark or star of any point count, not a robot head, not a dot, not a chevron, not a bracket, and not the GDG chapter's stepped stroke.
- It is **monochrome by construction** and uses `currentColor`. It has no color meaning at all, so it can never read as the blue/red/yellow/green sequence, which is the mistake the hackathon files already made.
- It uses no gradient. The website's orange gradient stays on the website.
- It is derived from the club's own share card, which the club already publishes.

**Why it is worth having.**

- **One variable does real work.** `--acm-rail-break` turns one drawing into a semester's worth of page-specific structure, which is the one transferable idea from event design systems: parameterize a single construction instead of drawing new assets.
- **It survives the whole range.** A 4px bar on a 20px chip to a 0.25 in bar on a poster, because the width is set per medium and nothing else changes.
- **It survives every theme.** `currentColor` means light, dark, forced-colors, and a grayscale print all work without a second asset. Primary on the surface measures 6.13:1 in light and 10.69:1 in dark.
- **A student can build it.** It is one pseudo-element and one gradient. Nobody has to open a drawing tool, which is the constraint that actually determines whether a design system survives an officer transition.
- **It is semantically honest.** A chapter whose pillars are four verbs gets a mark that is a track with one stop on it.

**Rules of use, and these matter more than the geometry:**

- **The Rail is never the club's logo and never becomes the favicon on its own.** It is a page device. The chapter logo and the favicon are `[TBD]` in brand.md. Where the Rail and an ACM mark both appear, they are separated by at least the height of the mark, and they never sit in a shared box, a shared color field, or any arrangement that could read as one combined mark.
- **Once per screen.** One Rail on the hero or the page's first block. Callouts carry their own short Rail as their left edge, and that is the only repetition allowed. Never both on the same block.
- **It never carries meaning alone.** The pillar name is always in text next to it. Shape alone cannot convey information (WCAG 1.4.1), and a break at 20% versus 40% is invisible to a lot of people.
- **It is decorative in the accessibility tree.** `aria-hidden="true" focusable="false"` on any inline SVG instance; the CSS pseudo-element is invisible to assistive tech already.
- **Contrast:** decorative, so no minimum applies, but hold it to 3:1 against its surface anyway. It should survive a projector in a bright lab and a photocopied flyer.
- **Favicon:** `[TBD]`. It follows the chapter logo decision, not this device.
- **Merchandise:** the Rail alone on a shirt or sticker is fine, because it is the club's own mark. The ACM logo on merchandise follows ACM's chapter policies. Do not put them on the same object.

Last updated: 2026-09-01.
