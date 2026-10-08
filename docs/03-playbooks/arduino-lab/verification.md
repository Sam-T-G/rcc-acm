# Verification: what passes before a lab ships

A green check is required, but it isn't enough. Every item here has caught a real problem.

## 1. Code compiles on both board types

Every sketch a slide shows, edits, or links to gets compiled for the Elegoo UNO R3 and the UNO R4 WiFi:

```bash
arduino-cli lib install Servo          # arduino-cli doesn't bundle Servo; the Arduino IDE does
arduino-cli compile -b arduino:avr:uno <sketch-folder>
arduino-cli compile -b arduino:renesas_uno:unor4wifi <sketch-folder>
```

- **What to test:** the real starting point (the built-in example) plus each edit, as its own sketch.
- **Write it down:** "Tested on the UNO and UNO R4 WiFi, <date>" goes in the step's notes.
- **Built-in examples:** check them against the installed copy. For example, Sweep is at `~/Library/Arduino15/libraries/Servo/examples/Sweep/` on a Mac.

## 2. The deck check passes

```bash
node deck-kit/check.mjs semesters/<term>/meetings/<date>-deck.html --shots <dir>
```

It checks type floors, margins, overlap, variety, the auto-beat behavior, and the presenter tools. Fix every failure before going further.

## 3. Every step slide reviewed by eye

Open the screenshot for each step at its last beat and check:

- the diagram shows every hole, pin, and menu item the text names;
- the newest part is the orange one;
- no label sits on a wire or runs off the picture;
- the text fits without crowding the progress line.

The check doesn't measure text inside SVG pictures, so this pass is the only thing that catches overlapping labels.

## 4. A real-key walk

Present the deck (S for the presenter view) and press through every slide with the keyboard or the phone remote. Check that:

- each step's "you should see" line fills in on its own;
- check-ins wait for a press;
- timers start with T.

## 5. A dry run on a real kit

Someone who didn't write the lab builds it from the slides alone, with nothing else open. Every place they hesitate or ask a question is a step to rewrite against the [instruction spec](instruction-spec.md).

## 6. Hardware prep confirmed

- [ ] Batteries tested.
- [ ] Order arrived and kits are complete.
- [ ] Cables counted.
- [ ] The guide's [CHECK] items resolved.
