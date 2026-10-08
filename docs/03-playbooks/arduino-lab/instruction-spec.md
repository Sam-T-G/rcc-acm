# Instruction spec: how to write a lab step

Every hands-on step in an Arduino lab follows this spec. A person who has never touched a breadboard should be able to do the step from the slide alone, without asking anyone.

If a step can't be written this way, it's two steps.

## Anatomy of a step

One step is one slide and one physical action. Built with `steps()` in [deck-kit/lab/labkit.py](../../../deck-kit/lab/labkit.py).

| Part | What it says | Limit |
|---|---|---|
| Eyebrow | `<Round name> · step k of n` | Generated |
| Headline | The action, naming the part and where it goes: "Brown to GND", "Add the resistor" | 6 words, one line, no colon |
| Instruction | 1. **Take** the part, by a name that matches what people see (bag label, color, shape). 2. **Where each end or leg goes**, by exact hole, rail, or pin label. 3. Optional: how to seat it or which way round. | About 35 words, 3 lines |
| You should see | A result they can check with their eyes. Fills in on its own after 1.2 s. | 8 words |
| Detail under it | What the result means, or the fix for the most common miss | 10 words |
| Diagram | Everything built so far, with the newest part in orange. Every hole in the text appears in the picture. | |
| Speaker notes | Why it works, the usual mistakes, sourced facts, and a bridge line into the next step | |

## Sentence patterns to copy

Use these as written and swap in the part and the holes. They come from the 2026-10-08 lab, which was modeled on the Elegoo and Arduino tutorials' wiring descriptions.

| Action | Pattern |
|---|---|
| A jumper wire | "Take a jumper wire. Plug one end into hole a11 and the other end into any hole in the top - rail (blue line)." |
| A part with two legs | "Take one red LED. Plug its long leg into hole c10 and its short leg into hole c11." |
| A part that bends | "Take one resistor labelled 220. Bend both legs down. Plug one leg into any hole in the top + rail (red line) and the other leg into hole a10." |
| A part across the gap | "Take one button. Set it over the middle gap with its four legs over holes e15, e17, f15, and f17. Press it down until it sits flat." |
| A wire on a part's plug | "Take the free end of the jumper on the brown wire. Plug it into a pin labelled GND on the UNO's short row of power pins." |
| A board pin | "Plug it into the pin labelled ~9 in the long row of digital pins." |
| Taking something out | "Pull the jumper out of hole a11." |
| Swapping | "Put the wire that was in + into -, and the wire that was in - into +." |
| Power off | "Press the module's power switch so its light goes off." / "Pull the USB cable out of the UNO." |
| A menu in the IDE | "Click File. Point to Examples, then 01.Basics, and click Blink." |
| Editing code | "Find the two lines that say delay(1000); and change both to delay(200);." |
| Adding code | "Click at the end of the line myservo.attach(9); press Enter, and type pinMode(2, INPUT_PULLUP);" |
| Uploading | "Click the round arrow button at the top left to upload." |

## Naming rules

- **Holes:** a letter and a number, like a10. Explain this once per lab on the breadboard slide: the letters a to j run down the side, the numbers along the top. Say "row 10" only when any of a10 to e10 will do.
- **Rails:** "the top + rail (red line)" and "any hole in the - rail (blue line)". Say "any hole" whenever the position doesn't matter. Boards differ in which line is on the outside, so the notes tell people to follow the lines, not the picture's order.
- **Board pins:** use the label printed on the board, exactly: `~9`, `5V`, `GND`, `2`. Say which row: "the long row of digital pins" or "the short row of power pins". With more than one GND, say which one ("the GND next to pin 13").
- **Parts:** one plain name per part for the whole lab, the name in the [parts glossary](parts-glossary.md). The first time a part appears, add how to find it: "from the bag labelled 220", "the white plastic arm", "the round plug".
- **Wire colors:** name a part's own wires by color (servo brown, red, orange). Never ask for a jumper of a particular color, because kits vary.
- **Software:** the exact menu words in order. The verbs are Click, Point to, Type, Find, and Change.

## Banned: vague instructions and what to write instead

| Vague | Write instead |
|---|---|
| "Connect the LED" | "Take one red LED. Plug its long leg into hole c10 and its short leg into hole c11." |
| "Wire it to ground" | "Plug the other end into any hole in the top - rail (blue line)." |
| "Hook up the servo" | Three steps: brown to GND, red to 5V, orange to ~9, each with "Take the free end of the jumper on the ___ wire." |
| "Set up the board" | Two steps: pick the board, then pick the port. Each one names the exact menu path. |
| "Upload it" (the first time in a lab) | "Click the round arrow button at the top left to upload." Later uploads can say "upload". |
| "Put the resistor in series" | Name the holes. No circuit jargon in instructions. |
| "Make sure it's grounded" | Name the wire and both of its ends. |
| "Add the button logic" | Show the exact code on the right, and say which lines to delete and where to type. |

**Words that need a plain-word swap or a one-line explanation:**

| Jargon | Plain word or explanation |
|---|---|
| series, parallel | name the holes instead |
| anode, cathode | long leg is +, short leg is - |
| GPIO | pin |
| header | the row of pins |
| VCC | 5V |
| pull-up | "INPUT_PULLUP keeps the pin HIGH until you press" |
| PWM | "pulses fast enough to look in-between" |
| sketch | say once that Arduino calls a program a sketch |

## Order rules inside a round

- **Breadboard rounds:** switch the power off first. Then place parts, then wires. Then "Trace it, then switch on", then look.
- **Arduino rounds:** the first step is "Unplug USB". Upload is the last step.
- **One action per step.** If the instruction needs "and then" for a different part, split it. A wire's two ends count as one action.
- **Never leave the room on a half-built circuit** across a concept or check-in slide. Finish the round, then talk.

## Voice

These come from the deck-kit rules, plus the lessons in the [README](README.md):

- Casual and plain, the way a student explains it to a friend. No idioms, no lecture voice.
- No em dashes inside sentences. No colons in headlines.
- None of: seamless, comprehensive, robust, leverage, delve, showcase, elevate, unlock.

## Before a step ships

- [ ] Do the step from the slide alone, on a real kit, with nothing else on screen.
- [ ] Every hole, pin, and menu name in the text matches the diagram and the real board.
- [ ] Any code it shows or edits compiles for the UNO and the UNO R4 WiFi ([verification.md](verification.md)).
- [ ] "You should see" is something you actually saw.
