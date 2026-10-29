# Drawing the breadboard

Every breadboard picture in a lab deck is drawn with `board()` in [deck-kit/lab/labkit.py](../../../deck-kit/lab/README.md). This page says what the real board looks like, what a drawing of it must keep true, and what it may simplify.

## Why this page exists

The 2026-10-15 lab first shipped a zoomed breadboard (`bbz`) that spaced holes 76 px apart across and 36 px down. It looked neat, but the spacing didn't match the real board. Stretching one axis made the board look tall and narrow. The four rails looked like four more rows of holes, so the middle channel seemed to cut across the rails instead of running beside them. And nothing showed which holes are joined, which is the one thing a beginner needs from the picture. Sam caught it in review on 2026-10-14, the day before the lab, and every board picture was redrawn with `board()`.

## The real board

The club's kits use an 830-hole board.

- **One grid.** Holes are 0.1 inch apart, across and down alike.
- **Numbered rows.** There are 63. Each one is two strips of 5 joined holes: a to e, and f to j.
- **The middle channel** runs the long way, between e and f. It's wide enough (0.3 inch) for a chip to straddle it, and it joins nothing.
- **Four rails,** two along each long edge, also run the long way, beside the channel. Each rail is one long joined set, set apart from rows a and j. Its holes come in groups of 5.
- **Printed lines:** red for +, blue for -. On the club's Elegoo boards both edges print red above blue, so with the printing upright the far pair is + outside, - inside, and the near pair is + inside, - outside. Steps still name a rail by its line ("the top - rail (blue line)"), never "the outer rail", because other makers differ.
- **Split rails.** Some long boards break each rail in the middle. [CHECK whether the club's boards do.] If they do, keep the build on the module's half.
- **The power module** plugs into the row-1 end and feeds all four rails. Its pins come in the same order on both sides, so that is the only end where its + pins land on the red lines.
- **Which way the rows run.** Held so its printing reads upright, the Elegoo board has line a at the far edge and counts its rows 60 down to 1 from left to right, so row 1 and the module sit at the right end (Elegoo's product photo; manual p.193). Elegoo's own wiring diagrams often show the board turned the other way, with the module on the left and the printing upside down.
- **Printed labels.** Letters run down the ends and numbers along the edges. Many boards print every fifth number.

## Rules for every board picture

1. **Never stretch one axis.** One pitch across and down. If the board won't fit, show fewer rows, never squashed ones.
2. **The long axis runs across the slide,** in the view the students are told to take. The 2026-10-15 lab says "module on your right, letters upright": line a at the top, row 1 at the right next to the module, rows counting up to the left. Never show a slice so narrow that the board reads tall, and never mix two views (the first `board()` put the module on the left with line a on top, a view that matches no way you can hold the real board).
3. **Draw the joins.** Each 5-hole strip and each rail sits on a light bar, so the picture shows what's connected, not only where the holes are.
4. **Rails look like rails:** one long bar, its red or blue line, and a + or - at the end. Never use color alone; the + or - sign carries the same meaning ([foundations.md §2.7](../../04-brand/design-system/foundations.md), diagram colors).
5. **The newest part is orange, and the strips it touches are tinted.** The tint shows what the "you should see" line says, like "The left leg now joins the - rail".
6. **One view for the whole lab.** The same window every step, with the module at the left end, so parts pile up and nothing jumps. Parts from earlier rounds stay drawn, in ink, because they're still on the board.
7. **Labels stay off the parts.** The row-number ruler sits above the board. A wire to the UNO leaves the board between holes and ends at the pin's name ("pin 2", "pin ~5", "GND").
8. **Every hole a step names is in the picture,** at its real place, with the part's leg on it.

## What the drawing simplifies, and why that's safe

- **Rail holes line up with the numbered rows.** On a real board the groups of 5 sit a little offset. Steps say "any hole in the rail", so it never matters where.
- **Parts are simple shapes from above:** the transistor's flat side, the diode's stripe, the button's square. Their legs land on the holes they use.
- **The ruler labels only 1, 10, and 20.** The steps count from those, and the gaps hold the wire tags.

## Before a board picture ships

- [ ] Hold it next to a photo of the real board. The rails and the channel run the same way, the strips hold 5 holes, and the holes are evenly spaced.
- [ ] Every hole named in the step's text has the part's leg drawn on it.
- [ ] The tinted strips match the "you should see" line.
- [ ] No label sits on a wire, a part, or another label. The deck check doesn't read text inside pictures, so look at the screenshot.

## Using `board()`

`board(parts, hi=(), on=False)` draws rows 1 to 23, counted leftward from the module at the right end.

- **`parts`:** what's on the board, by name (`labkit.BD_ORDER` lists them). The module is always drawn.
- **`hi`:** the newest parts, drawn in orange with their strips tinted.
- **`on`:** the module is switched on, so its light is lit. The fan spins only while the test jumper closes the transistor.
- **Adding a part:** give it an entry in `_bd_parts` with the holes it uses, as (row number, line) pairs, and a drawing placed with `bdx()` and `bdy()`. Never place a part by pixel. The tint and the description come from the hole list, so they always match the drawing.
- **Older pictures:** `bb()`, `bbz()`, `button_uno_steps()`, and `fan_uno_steps()` stretch an axis or skip the holes. Use them only to rebuild an old deck exactly.
