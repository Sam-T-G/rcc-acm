# deck-kit/lab: building Arduino lab decks

`labkit.py` turns a lab written to the [Arduino lab spec](../../docs/03-playbooks/arduino-lab/README.md) into deck-kit slides. It writes the step slides, check-ins, and Do slides, and draws the pictures: a hole-by-hole breadboard, the UNO with a servo or button, IDE menus, code panels, and the parts table. It's plain Python 3 with no dependencies.

## Start a new lab deck

1. Write the rounds on [templates/arduino-lab-round.md](../../templates/arduino-lab-round.md) first.
2. Copy `example_lab.py` to `scratch/<date>-deck/gen.py`. Point `OUT` at `semesters/<term>/meetings/<date>-deck.html` and change the stylesheet and script paths to `../../../deck-kit/`.
3. Keep `sys.path.insert(0, '<repo>/deck-kit/lab')` and import from `labkit`.
4. Build with `python3 gen.py`, then run `node deck-kit/check.mjs <deck> --shots <dir>` and work through [verification.md](../../docs/03-playbooks/arduino-lab/verification.md).

The example builds `deck-kit/lab/example-lab.html`, one full round, and passes the check.

## Slide builders

| Function | Makes |
|---|---|
| `steps(round_name, items, section=None)` | One step slide per item. Each item is `(headline, instruction, see, see_detail, picture, notes)`. Rotates grounds, adds "step k of n", and fills in the "see" line after 1.2 s. |
| `check(label, h2, items, notes, ground=None)` | A check-in. Each item is `(what you saw, why)`. 4 at most. |
| `do_slide(label, eyebrow, h2, steps, secs, picture, ...)` | Numbered steps, an inline timer, and a picture. Use it for the parts finder and the challenge round. |
| `split_beats(label, eyebrow, h2, beats, picture, auto=None, ...)` | A concept slide. `auto=2` fills it in on its own. |
| `code(label, h2, src, notes)` | A full code slide. 10 lines at most. |
| `notes(*paragraphs, bridge=None)` | Speaker notes, with the bridge line last |
| `lab_css()` | Every style the pictures and lab slides need. Put it in the deck's `<style>`. |

## Pictures

All are 760 × 560 stage px, with labels at 32 px.

| Function | Draws |
|---|---|
| `bb(parts, hi=(), lit=False, on=False)` | A breadboard drawn hole by hole: rows 1 to 22 along the top, a to j down the side, and the rails. `parts` come from `module`, `jumpers`, `battery`, `resistor` (+ rail to a10), `led` (c10, c11), `ground` (a11 to the - rail), `button` (e15, e17, f15, f17), `btn_in` (a11 to a15), `btn_out` (j17 to the bottom - rail). `hi` turns parts orange. `lit` and `on` light the LED and the module light. |
| `parts_kit()` | The 12 parts of the 2026-10-08 lab, drawn and named |
| `servo_steps(k)` | UNO and servo. `k` = 1 jumpers in the plug, 2 brown to GND, 3 red to 5V, 4 orange to pin 9. |
| `button_uno_steps(k)` | A button on the UNO. `k` = 1 button, 2 corner to pin 2, 3 opposite corner to GND. |
| `laptop_uno(plugged)` | Laptop and UNO, with the USB cable plugged in or pulled out |
| `ide_menu(items)` | An IDE menu path, the last item in orange |
| `snippet_hl(name, label, lines, hl=())` | A code panel, at most 38 characters a line. `hl` highlights lines. |
| `motor_blade()`, `motor_rails_dir(reverse)`, `servo_arm()` | Motor, fan, and servo steps |
| `loop_basic()`, `breadboard()`, `ground()`, `uno()`, `angles()`, `servo_need()`, `button_pin()`, `button_loop()`, `led_rails_lit()`, `power()` | Concept pictures |

**Adding a picture:**

- Write a function that returns `svg(name, aria_label, body)`.
- Keep labels at 32 px and inside the 760 × 560 box. The check doesn't measure SVG text, so look at the screenshot.
- Put code inside a picture in `<g data-code="">`. Never use `class="code"` inside an SVG: deck.js wraps `.code` as a block, and that breaks the picture.
- Add the new parts to `bb()` by hole, never by eye, so the picture always matches the text.

## Gotchas this kit already handles

- deck.js splits text into word spans for animation, so a CSS grid row needs its text wrapped in one `<span>`. `do_slide` does this.
- A clock needs a `.clock__hint`; deck.js writes "T to start" and "T to pause" into it.
- Slide text can't contain `{ }` or `< >` outside code. Say "closing bracket" in an instruction.
