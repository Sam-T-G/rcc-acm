# Round structure: how a lab is paced

A lab is a string of rounds. Each round teaches one idea by building one thing:

1. **Concept**
2. **Steps**
3. **Check in**
4. Next round.

People spend most of the time with their hands on parts, not reading slides.

## The rhythm

| Phase | Slides | What happens | Built with |
|---|---|---|---|
| Concept | 0 to 2 | The one idea this round shows, in plain words, with a picture. Fills in on its own (`data-auto`) so it never stalls. | `split_beats(..., auto=2)` |
| Steps | One per action | Instruction, picture, and "you should see". Officers walk the room. | `steps(round_name, [...])` |
| Check in | 1 | 3 or 4 lines of what you saw and why, plus one "try this". The presenter asks each line as a question, takes an answer, then presses. | `check(...)` |
| Challenge (last round only) | 1 | A choice of 4 open extensions with a timer and a hint picture | `do_slide(...)` |

Concept slides are optional. If a round's idea is obvious from building it, skip the concept and let the check-in explain it.

**Start every lab** with a "Find your parts" Do slide: every part drawn and named, 2 minutes, before any wiring. It's also hands-on.

## Timing

- **About 35 seconds per step** for a room of beginners. A 7-step round is about 4 minutes.
- **Hands-on time is at least two thirds of the lab block.** The 2026-10-08 lab had 30 hands-on minutes out of 42.
- **Put a target clock time in the notes** on the first slide of each round ("Aim to be here by 1:58").
- **If a round runs long,** cut the challenge round, never the early rounds. Later rounds depend on them.

## Slide types and the kit features they use

| Type | Kit features | Notes |
|---|---|---|
| Step | `data-kind="beats"`, `data-layout="split"`, `data-step`, `data-auto="1.2"`, `data-room` | One beat: the "you should see" line. One press per step. |
| Do (parts finder, challenge) | `data-kind="clock"`, `data-layout="split"`, `data-do`, `data-timer`, `data-room` | Numbered steps, an inline timer (T), and a picture. Stays up while tables work. |
| Concept | `beats`, `split`, `data-auto` | At most 4 beats |
| Check in | `beats`, eyebrow "Check in" | Manual presses, so the presenter can ask first |
| Hidden detail (C++ under the hood) | `code` | Use sparingly, one per lab |

**Kit rules that apply:**

- No three slides in a row with the same kind, ground, and layout. `steps()` rotates the grounds for you.
- At most 4 beats per slide.
- No `{ }` or `< >` in slide text outside code. Code drawn inside a picture goes in `<g data-code>`.

## Check-in questions

Each one is a line the room can answer from what they just did:

1. **What you saw:** "It lit up" → why: "The loop is complete."
2. **What happens if...:** "Now pull one wire out" → they do it.
3. **Why a part is there:** "Why the resistor?"
4. **The habit they just used,** or one "try this" change ("Change both 1000s to 200").

Notes say: ask first, take one answer, then press.

## Round order for a typical first lab

Use the 2026-10-08 lab as the reference:

- **Find your parts.**
- **Loop:** LED with no code, then a button in the loop.
- **Motor off the rails:** why a pin can't drive it.
- **Board and Blink:** what Arduino runs for you.
- **Servo:** Sweep, then why ground is shared.
- **Button input with if/else.**
- **Challenges:** while, else if, a toggle.

Later labs can drop the no-code rounds and start from code.
