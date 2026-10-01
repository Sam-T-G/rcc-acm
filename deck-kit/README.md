# Deck kit

How the club makes slide decks. The slides are plain HTML with one or two attributes each; the kit supplies the stage, the Rail on the cover, the motion, the timers, room mode, speaker notes, and a check that walks the deck with real key presses.

Ported on 2026-09-24 from the GDG chapter's kit (`rcc-gdg/deck-kit`) onto this repo's design system. The rules it implements are [assets.md §10.5](../docs/04-brand/design-system/assets.md) (the slide spec) and [accessibility.md §2.4](../docs/04-brand/design-system/accessibility.md) (the Rail). Where the kit and those files disagree, the files win and the kit has a bug. Where the kit goes past them on purpose, [the decision log](../docs/01-governance/decision-log.md) has the row.

| File | What it is |
|---|---|
| [example.html](example.html) | A finished deck with one slide of every kind. Copy from it; its copy is about the kit, so it makes no claim about the club |
| [deck.css](deck.css) | The stylesheet. Tokens copied from `tokens.css` (the check fails if they drift), the stage, and the thirteen kinds |
| [deck.js](deck.js) | The engine. No build step, no dependencies beyond GSAP, which is optional |
| [check.mjs](check.mjs) | Checks a deck against the slide rules and walks it in five modes. Headless Chrome, no npm install |
| [bundle.mjs](bundle.mjs) | Makes one self-contained HTML file from a deck |
| [fetch-image.mjs](fetch-image.mjs) | Finds and saves an openly licensed photo with its credit. The same file is in the GDG kit |
| [ingest-photos.mjs](ingest-photos.mjs) | Brings the club's own photos in: 1600 px, every bit of metadata (GPS included) stripped, collage markup printed |
| [encode-video.swift](encode-video.swift) | Makes a slide clip: upright H.264 MP4 at a fixed size and bitrate, no audio, no metadata, plus a poster. `swift deck-kit/encode-video.swift <in.mov> <dir> <name>` |
| [disk.js](disk.js) | The career disk: a plug-in slide kind in Three.js. Loads as a module before `deck.js` and registers `window.DeckKinds.disk` |
| [CLAUDE.md](CLAUDE.md) | The calls an agent building a deck makes without asking: photos, variety, copy |

## Make a deck

Put it in the meeting folder, named for the date: `semesters/2026-fall/meetings/2026-09-24-deck.html`. Start from the last deck or from `example.html`, fix the relative paths to `deck-kit/`, and replace the slides. Leave an HTML comment starting `fill:` anywhere a decision is still open; the check refuses a deck that has one.

Every slide is a `<section class="slide">` with a `data-kind`. The first slide of each section also carries `data-section="Name"`; the name shows in the progress line along the bottom, and a slide without one belongs to the section before it. The ledger line along the top comes from `data-ledger` on `<main class="deck">`. Speaker notes go in `<aside class="notes">` and show with `N`. Add `data-room` to the slides that stay up in room mode (`5`). Add `data-beat` to any element to reveal it on a press.

## The thirteen kinds

| `data-kind` | Markup the kit reads |
|---|---|
| `cover` | An empty `.cover__rail`, `.cover__name` reading `ACM @ RCC`, `.eyebrow`, the deck's only `h1`, and a `.sub` whose last clause alone is `<strong>`. Optional `data-starts="13:30"` shows a countdown in the last half hour |
| `statement` | Optional `.eyebrow`, an `h2` of fourteen words or fewer, optional `.sub`. One `.hl` span may carry the lead hue |
| `contrast` | `h2`, then `.contrast` holding two `div`s (`.is-weak`, `.is-strong`), each a `.label` and a `p` |
| `beats` | `h2`, then `ol.beats` with up to four `li data-beat`, each with an optional `.detail` |
| `board` | `h2`, then `ol.board`, one `li` per dated thing: a `<time>` and a `<span>` |
| `code` | `h2`, then `pre.code`, twelve lines at most. `.k` and `.c` spans mark keywords and comments |
| `figure` | `p.figure` holding `.figure__num` with `data-from` and `data-to`, and `.figure__unit`. Source the number in the notes |
| `clock` | `data-timer` in seconds on the slide; a `.clock` block, or let the kit build one |
| `photo` | `.photo__text` (`.eyebrow`, `h2`, `.sub`) beside `figure.photo` holding an `img` with `width`, `height`, and `alt`, and a `figcaption.credit` with a link to the source. `data-layout`: `bleed-right` (default), `bleed-left`, or `framed` |
| `grid` | `h2`, then `ul.grid` with two to four `li`, each an optional `img`, a `b`, and a `.credit` for its photo |
| `signup` | `.signup__main` (`.eyebrow`, `h2`, `.sub`) and an `a.qr` whose `.label` prints the URL. Generate the QR as inline SVG and decode it once before trusting it |
| `collage` | `.eyebrow`, `h2`, `ul.collage` with up to six `li > img` of the club's own photos, each with `data-faces="none"` or `"consented"`, and one `.credit` line |
| `ask` | `.ask__main` (`.eyebrow`, `h2`, `.ask__meta`, optionally one `.callout callout--check`), an optional `a.qr` with its URL as text, and `.ask__foot` with `.ask__name` reading `ACM @ RCC` and an `.ask__stamp` |

## What the kit decides for you

- **The Rail once, on the cover, solid.** It draws down the cover's edge on the opening and retracts to its foot when the deck leaves the cover. No other slide has one; a Check or Warning callout's short Rail is the only repeat.
- **The progress line is not the Rail.** It is the "On this page" rail laid flat (components.md §7.8): section names in the ledger face, the current one at weight 500 in primary, over a 3 px neutral hairline.
- **Light theme only.** A-210 is a daylight wall. There is no dark toggle.
- **Floors.** Titles 72, body 40, ledger 32, at 1920 x 1080 inside 96 px margins. The check measures every text node.
- **Slide-scale motion.** Words rise through masks at 700 ms per beat and 1100 ms per section change, on `--acm-dur-beat`, `--acm-dur-move`, and `--acm-ease-arrive`, which the kit adds to the system's tokens (decision log, 2026-09-24). Reduced motion makes every transition a cut.

## Pictures and variety

Any slide that names a thing a person could photograph gets a photo. `fetch-image.mjs` searches Wikimedia Commons and Openverse for CC0, public domain, CC BY, and CC BY-SA only, saves a 1600 px JPEG with its metadata stripped, keeps a `CREDITS.md` beside the photos, and prints the markup with the credit link:

```sh
node deck-kit/fetch-image.mjs search "arduino uno r4"
node deck-kit/fetch-image.mjs get "commons:Arduino UNO R4 WiFi.jpg" semesters/2026-fall/meetings/2026-09-24-deck-images arduino-uno-r4 --alt "An Arduino UNO R4 WiFi board seen from above."
```

**Split layout.** A `clock` or `beats` slide with `data-layout="split"` puts `.split__head` (`.eyebrow`, `h2`) across the top, `.split__main` (the clock with its `.sub`, or the `ol.beats`) on the left, and `figure.viz` holding an inline SVG with `viewBox="0 0 760 560"` on the right; one SVG unit is one stage pixel, so write labels at 32. On a beats slide, `data-stage="k"` shows an SVG part from beat k and `data-until="k"` shows it only before beat k. Loops are the deck's own CSS keyframes, scoped to `.is-presenting .slide.is-current`; the attributes are the still pose, which is what reduced motion, the stack, and print show. The 2026-10-01 deck has six examples.

Every slide takes a `data-ground`: `paper` (default), `warm`, `tint` (the primary container), or `orange` (the raw `#ff4d00` fill with ink text). Statements take `data-layout="center"` or `"giant"`. The check measures every text pair against its ground at 4.5:1, fails text over a photo, and fails three slides in a row with the same kind, ground, and layout.

Presenting, the ground lives on the stage and crossfades from slide to slide on the effects track, so it survives reduced motion; the check samples it mid-fade.

## Video

A `<video>` goes anywhere an `<img>` does: a photo slide, a grid tile, a collage tile. The markup is shared with the GDG kit: `src` on the element, `poster`, `width`, `height`, `muted`, `loop`, `playsinline`, `preload="auto"`, an `aria-label`, and never an `autoplay` attribute. `data-play="auto"` plays while its slide is current; `data-play="press"` waits for the next forward press, like one more beat. `V` plays or pauses the current slide's video. Leaving a slide pauses its video (a press video also rewinds). Under reduced motion or on a phone, an auto video stays on its poster. Encode clips with `encode-video.swift`; its defaults keep a 25-second phone clip under 1 MB, so the bundler inlines it and it plays with no network. The check fails a clip over 1 MB and tests real playback in every mode. For a collage that mixes shapes, `ul.collage.is-row` with `style="--ar: w/h"` on each `li` lays them out as one row with almost no crop.

## The career disk

`data-kind="disk"` with `data-ground="space"` is a 3D scene: a disk of majors, CS (theory) at one pole and ME (physical) at the other, CompE and EE down one side, data science and the autonomy arc down the other. Every role is an `li` in `ol.stations` with `data-majors="CS:0.6,DS:0.4"` (weights, any of CS, DS, CompE, EE, ME) and `data-tier` (`classic` inner ring, `growing` middle, `new` outer); the engine places it at the weighted angle of its majors. Beat 0 is the overview, each press flies to the next station in list order and shows its card, and the last beat pulls back for the finale. Drag to look around; click a beacon to fly to it. Entering from the slide before it, that slide shatters and the camera breaks through into the scene; reduced motion makes it a cut.

The page needs an import map for Three.js and the module before `deck.js`:

```html
<script type="importmap">{ "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.186.1/build/three.module.js", "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.186.1/examples/jsm/" } }</script>
<script type="module" src="../../../deck-kit/disk.js"></script>
```

Every word is DOM (the HUD and the station cards), so the type floors and contrast checks cover it. With no WebGL or no CDN, the stations step through as plain cards, one per press. Other plug-in kinds follow the same contract: `window.DeckKinds[kind] = (slide, api) => ({ beats, set, go, enter, leave, busy, finish, sleep, resize })`.

## Presenter view, phone remote, run sheet

Ported 2026-10-01 from the GDG chapter's kit, where the rules are [its presentation.md §13.13](https://github.com/Sam-T-G/rcc-gdg). The deck window is always the source of truth: the presenter view, its two preview frames (`?view=mirror`), and the phone only send key presses and draw what the deck reports.

- **`S`, presenter view.** A second window: the current slide, a preview of what one more press shows (the next beat, the next station on the career disk, or the next slide), the notes, the bridge line, a timer since it opened (click to reset), the time of day, and the slide's clock. A clicker works with either window focused. It needs the projector to **extend** the laptop; on a mirrored display the room sees it, so use the phone instead.
- **`M`, phone remote.** Shows a QR code (in the presenter view if it is open, otherwise on the stage). The phone gets the notes, the bridge line, what's next, and big Back and Next buttons, and keeps its screen awake. Presses travel through ntfy.sh over plain HTTPS (no account), so it works on cellular. The topic is a long random name and only slide numbers and key names cross it. ntfy.sh allows 250 messages a day per network address, about one per press. The phone loads the **published** deck, so the deck needs `data-live-url="https://sam-t-g.github.io/rcc-acm/decks/<slug>/"` on `main.deck`, and the live copy must be the same version as the one on the projector.
- **`?view=runsheet`.** Every slide in one printable table: title, kind, presses, clock, bridge line, the slide it leads into, and the notes. Bring it as the backup.
- **Bridge lines.** End a slide's notes with `<p class="bridge">One sentence into the next slide.</p>`. The presenter lights it on the slide's last press. The check reports the count.
- **The career disk** builds no 3D scene on the phone or the run sheet, and the presenter's two previews draw it at half resolution a few times a second and cut between stations, so the projector keeps the GPU.

`check.mjs` tests the presenter view, the run sheet, and the phone page's no-code message with real key presses. It cannot test the phone itself, which needs the relay and a second device. Before a meeting that will use the phone: press `M` on the live deck, scan, tap Next twice, and watch the deck move.

## Running it

Open the file in Chrome. Arrows, Space, or a clicker move; `T` and `R` run the clock; `5` is room mode; `V` plays or pauses a video; `N` shows notes; `S` opens the presenter view; `M` shows the phone remote's QR code; `F` is fullscreen; `?` lists the keys. On a phone, or with `?stack` on the URL, the deck is a scrolling stack. Printing to PDF gives one 1920 x 1080 page per slide with every beat showing.

**Offline:** GSAP and the fonts come from CDNs. Without a network the deck still runs, with CSS-only motion and the fallback face; walk it once offline before relying on that.

## Checking it

```sh
node deck-kit/check.mjs semesters/2026-fall/meetings/2026-09-24-deck.html --shots /tmp/deck-shots
```

It needs Node 22 and Google Chrome. It fails on a fill marker or template token, token drift, a structure or slide-rule violation, type under a floor, anything outside the margins or in the progress band, and console errors. Then it walks the deck with real key presses with motion on, with reduced motion, with GSAP blocked, with no script, and at phone width, and checks that the Rail is full height on the cover after the opening and again after a walk back, that leaving the cover is a move and not a jump, that six fast presses land six steps on, and that `T` starts the clock.

## Publishing it

```sh
scripts/publish-deck.sh semesters/2026-fall/meetings/2026-09-24-deck.html 2026-09-24 --push
```

This runs the check, bundles the deck into `site/decks/<slug>/index.html` (gitignored), and replaces only `decks/<slug>/` on the `gh-pages` branch. GitHub Pages serves it at `https://sam-t-g.github.io/rcc-acm/decks/<slug>/`. The page is public the moment it is pushed: read [privacy-and-public-repo-policy.md](../docs/01-governance/privacy-and-public-repo-policy.md) first. Without `--push` it only builds.

---

**Last updated: 2026-09-24.**
