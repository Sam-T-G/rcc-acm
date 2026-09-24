# Building an ACM deck: rules for agents

Read [README.md](README.md) for markup. These are the calls you make without asking.

## Photos: fetch them freely

Whenever a slide names something a person could photograph (a board, a sensor, a tool, a part, a place, a product), give it a photo. Do not wait to be asked.

1. `node deck-kit/fetch-image.mjs search "<words>"` lists open-licensed candidates (CC0, public domain, CC BY, CC BY-SA only).
2. `node deck-kit/fetch-image.mjs get <id> <deck-folder>/<deck-name>-images <name> --alt "<what it shows>"` saves a 1600 px JPEG with no metadata, writes `CREDITS.md`, and prints the `<figure>` to paste.
3. **Open the file and look at it** before it goes on a slide. Alt text says only what you can see. If it shows the wrong model or board, pick another.
4. Keep the linked credit line on the slide. The check fails a photo without one.

The club's own photos come in through `node deck-kit/ingest-photos.mjs <folder> <images-folder>`, never pasted raw (it strips GPS). Each needs `data-faces="none"` or `"consented"`; if you cannot tell, ask Sam.

Club video: `swift deck-kit/encode-video.swift <clip> <images-folder> <name>`, then the printed `<video>` (README, Video). Same `data-faces` rule.

Never fetch: people or faces, stock people at laptops, AI images of people, the ACM Diamond or any ACM mark (none until the chapter lockup exists), Google product imagery, anything NC or ND. Never put text over a photo. Vendor logos printed on hardware in a photo are fine; a vendor logo as a label is not.

## Variety: no two slides in a row alike

- Mix kinds, grounds (`paper`, `warm`, `tint`, `orange`), and layouts (`center`, `giant`, `bleed-right`, `bleed-left`, `framed`). The check fails three slides in a row with the same kind, ground, and layout.
- Keep `orange` for the loud moments, about one slide in four, and at most one `giant` statement per section.
- Branding is the name `ACM @ RCC` as text, the Rail (cover only), and orange. There is no logo to add.

## Always

- Invent no facts: no dates, numbers, names, or claims Sam did not give. Unknowns stay `[TBD]` or come off the slide.
- Copy is casual and short, as a student says it. No colons in headlines, no em dash inside a sentence, none of: seamless, comprehensive, robust, leverage, delve, showcase, elevate, unlock.
- Run `node deck-kit/check.mjs <deck> --shots <dir>` and look at the screenshots before publishing.
