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
| `steps(round_name, items, section=None)` | One step slide per item. Each item is `(headline, instruction, see, see_detail, picture, notes)`. Rotates grounds, adds "step k of n", and fills in the "see" line after 1.2 s. An empty `see_detail` leaves the line out. |
| `check(label, h2, items, notes, ground=None)` | A check-in. Each item is `(what you saw, why)`. 4 at most. |
| `do_slide(label, eyebrow, h2, steps, secs, picture, ...)` | Numbered steps, an inline timer, and a picture. Use it for the parts finder and the challenge round. |
| `split_beats(label, eyebrow, h2, beats, picture, auto=None, ...)` | A concept slide. `auto=2` fills it in on its own. |
| `code(label, h2, src, notes)` | A full code slide. 10 lines at most. |
| `notes(*paragraphs, bridge=None)` | Speaker notes, with the bridge line last |
| `lab_css()` | Every style the pictures and lab slides need. Put it in the deck's `<style>`. |
| `lab_css_base()`, `lab_css_pictures()` | The same CSS split in two: list and Do-slide styles with the static picture classes, and only the picture animations. A deck with no animated pictures inlines `lab_css_base()` alone. |
| [partials.py](partials.py) | Whole slides for recurring shapes (pick, sendoff, rules, work_clock, round_map, win, qr). Documented in [../README.md](../README.md#partials). |

## Pictures

All are 760 × 560 stage px, with labels at 32 px.

| Function | Draws |
|---|---|
| `board(parts, hi=(), on=False)` | **The breadboard for every lab step.** True to scale and as the board sits on the table: printing upright, line a at the far edge, rows 1 to 23 counted leftward from the module at the right end, one pitch across and down, each 5-hole strip and each rail drawn as its joined set, rails with their red and blue lines, the row-number ruler above the board. `parts` come from `BD_ORDER` (`battery`, `button`, `btn_a`, `btn_j`, `transistor`, `emit_gnd`, `base_res`, `diode`, `motor`, `test_jump`, `to_pin5`, `gnd_link`; the module is always drawn). `hi` turns parts orange and tints the strips they touch. `on` lights the module; the fan spins only with the test jumper in. Rules: [breadboard-drawing.md](../../docs/03-playbooks/arduino-lab/breadboard-drawing.md). |
| `bb(parts, hi=(), lit=False, on=False)` (older; use `board()`) | A breadboard drawn hole by hole: rows 1 to 22 along the top, a to j down the side, and the rails. `parts` come from `module`, `jumpers`, `battery`, `resistor` (+ rail to a10), `led` (c10, c11), `ground` (a11 to the - rail), `button` (e15, e17, f15, f17), `btn_in` (a11 to a15), `btn_out` (j17 to the bottom - rail). `hi` turns parts orange. `lit` and `on` light the LED and the module light. |
| `parts_kit()` | The 12 parts of the 2026-10-08 lab, drawn and named |
| `parts_grid(cells, label)` | Up to 12 parts in a 3 × 4 grid. `cells` are `(icon, caption)`; icons are the `parts_kit()` set plus `transistor` and `diode` |
| `bbz(parts, hi=(), on=False)` (older, stretches one axis; use `board()`) | Rows 9 to 14 of the breadboard, zoomed, hole by hole. `parts`: `transistor` (c10, c11, c12, flat side facing you), `emit_gnd` (a10 to the top - rail), `base_res` (e11 to f11 across the gap), `diode` (b12 to the top + rail, stripe at the rail), `motor` (a12 and the top + rail), `test_jump` (j11 to the bottom + rail). `on` spins the fan. |
| `fan_uno_steps(k)` (older; use `board()` with `to_pin5` and `gnd_link`) | The UNO and the fan switch. `k` = 1 j11 to pin ~5, 2 also the top - rail to the free GND in the power row, 3 both wires orange (the check before power) |
| `ide_toolbar(mode)` | The IDE 2 toolbar: `'verify'` (check mark, with the size report) or `'upload'` (round arrow, with TX, RX, and L blinking) |
| `upload_path()` | Concept, 4 beats: write a sketch, Verify to numbers, Upload down the cable, the board runs it |
| `transistor_switch(diode=True)` | Concept, 4 beats: the pin can't power the fan, a transistor switch, the module's power, the diode. `diode=False` stops at 3 beats. |
| `arm_timeline()` | Concept, 4 beats: `write(90)` then the fan, against one degree at a time then the fan |
| `servo_sweep90()`, `press_sequence(fan_on=True)` | A servo sweeping 0 to 90; press, the arm climbs to 90, then the fan |
| `servo_steps(k)` | UNO and servo. `k` = 1 jumpers in the plug, 2 brown to GND, 3 red to 5V, 4 orange to pin 9. |
| `button_uno_steps(k)` | A button on the UNO. `k` = 1 button, 2 corner to pin 2, 3 opposite corner to GND. It draws no holes; use `board()`. |
| `laptop_uno(plugged)` | Laptop and UNO, with the USB cable plugged in or pulled out |
| `ide_menu(items)` | An IDE menu path, the last item in orange |
| `snippet_hl(name, label, lines, hl=())` | A code panel, at most 38 characters a line. `hl` highlights lines. |
| `motor_blade()`, `motor_rails_dir(reverse)`, `servo_arm()` | Motor, fan, and servo steps |
| `loop_basic()`, `breadboard()`, `ground()`, `uno(pins)`, `angles()`, `servo_need()`, `button_pin()`, `button_loop()`, `led_rails_lit()`, `power()` | Concept pictures. `uno(pins, names=True)` marks the pins you pass, default `((9, 'servo'), (2, 'button'))`; `names=False` leaves the part names to the beats |

**Adding a picture:**

- Write a function that returns `svg(name, aria_label, body)`.
- Keep labels at 32 px and inside the 760 × 560 box. The check doesn't measure SVG text, so look at the screenshot.
- SVG text is JetBrains Mono at 32 px, about 19.2 px a character, so a 760-wide picture fits 37 characters from x = 32. `snippet()` allows 38; keep code lines to 37.
- Put code inside a picture in `<g data-code="">`. Never use `class="code"` inside an SVG: deck.js wraps `.code` as a block, and that breaks the picture.
- Add the new parts to `bb()` by hole, never by eye, so the picture always matches the text.

## Problems the kit already handles

- deck.js splits text into word spans for animation, so a CSS grid row needs its text wrapped in one `<span>`. `do_slide` does this.
- A clock needs a `.clock__hint`; deck.js writes "T to start" and "T to pause" into it.
- Slide text can't contain `{ }` or `< >` outside code. Say "closing bracket" in an instruction.
