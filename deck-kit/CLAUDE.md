# Building an ACM deck: rules for agents

Read [README.md](README.md) for markup. Make these choices without asking Sam.

## Photos: fetch them freely

Whenever a slide names something a person could photograph (a board, a sensor, a tool, a part, a place, a product), give it a photo. Do not wait to be asked.

1. `node deck-kit/fetch-image.mjs search "<words>"` lists open-licensed candidates (CC0, public domain, CC BY, CC BY-SA only).
2. `node deck-kit/fetch-image.mjs get <id> <deck-folder>/<deck-name>-images <name> --alt "<what it shows>"` saves a 1600 px JPEG with no metadata, writes `CREDITS.md`, and prints the `<figure>` to paste.
3. **Open the file and look at it** before it goes on a slide. Alt text says only what you can see. If it shows the wrong model or board, pick another.
4. Keep the linked credit line on the slide. The check fails a photo without one.

The club's own photos come in through `node deck-kit/ingest-photos.mjs <folder> <images-folder>`, never pasted raw (it strips GPS). Each needs `data-faces="none"` or `"consented"`; if you cannot tell, ask Sam.

Club video: `swift deck-kit/encode-video.swift <clip> <images-folder> <name>`, then the printed `<video>` (README, Video). Same `data-faces` rule.

Never fetch: people or faces, stock people at laptops, AI images of people, the ACM Diamond or any ACM mark (none until the chapter lockup exists), Google product imagery, anything NC or ND. Never put text over a photo. Vendor logos printed on hardware in a photo are fine; a vendor logo as a label is not.

## A visual on every slide

Every slide gets something to look at besides words, whenever it can. Pick in this order:

1. A real photo of the thing the slide is about, fetched from the internet with the steps above.
2. A picture of the idea: a diagram, a true-to-object drawing from `lab/labkit.py`, a chart, a screenshot of the real page or tool, or a QR code.

The picture shows what the slide names. Never use one as decoration. These slides can go without a picture because they already fill the screen with big type or color: the cover, a `giant` or `orange` statement, a hero or marquee slide, and a work clock. Any other slide that ships with only words says why in its notes.

## Variety: no two slides in a row alike

- Mix kinds, grounds (`paper`, `warm`, `tint`, `orange`), and layouts (`center`, `giant`, `bleed-right`, `bleed-left`, `framed`). The check fails three slides in a row with the same kind, ground, and layout.
- Use the `orange` ground on about one slide in four, for the lines you want the room to notice, and at most one `giant` statement per section.
- Branding is the name `ACM @ RCC` as text, the Rail (cover only), and orange. There is no logo to add.

## Partials and templates first

Before hand-writing a slide, check [lab/partials.py](lab/partials.py) (pick, sendoff, rules, work_clock, round_map, win, qr) and [templates/](templates/). Don't bend `contrast` into a track picker or `signup` into a page handoff; use `pick` and `sendoff`. New spacing uses the `--st-*` steps, never a free number.

## The career disk

Stations are real roles only: every card names a current posting and a sourced reason, or leaves the reason off. Majors weights are judgment; say so in the deck header. Look at the disk in screenshots (overview, a few stations, the finale) before publishing.

## Arduino lab decks

Follow [docs/03-playbooks/arduino-lab/](../docs/03-playbooks/arduino-lab/README.md), [instruction-spec.md](../docs/03-playbooks/arduino-lab/instruction-spec.md) first, and build with [lab/labkit.py](lab/README.md). Every step slide names the part and says where each end goes by exact hole or pin label. Never ship a vague step. Compile every sketch for `arduino:avr:uno` and `arduino:renesas_uno:unor4wifi`. After the lab, add what you learned to the spec (the README's Rules learned table).

## Always

- Invent no facts: no dates, numbers, names, or claims Sam did not give. Unknowns stay `[TBD]` or come off the slide.
- Copy is casual and short, as a student says it. No colons in headlines, no em dash inside a sentence, none of: seamless, comprehensive, robust, leverage, delve, showcase, elevate, unlock.
- Follow ~/.claude/skills/prose-voice/SKILL.md for all copy: no literary moves (no object or idea doing a human thing, no 'not only X but Y', no 'X, not Y' pivots), and name the specific thing and the reason.
- Run `node deck-kit/check.mjs <deck> --shots <dir>` and look at the screenshots before publishing.
