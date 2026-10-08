# Playbook: Arduino lab

## Purpose

A weekly hands-on Arduino lab where everyone builds something real, step by step, in a meeting slot. The files here are a living spec. Each week's lab is built from them, and anything each lab teaches gets written back here, so the next lab is at least as clear.

## When

Any meeting week with a hardware build. Start 1 week out:

- the hardware audit needs the real kits;
- the dry run needs a real board;
- members need a few days' notice to install the Arduino IDE.

## Owner

The workshop lead for that week. The Chair signs off on the date. Anyone who changes a rule here opens a PR and, if it changes a template, adds a [decision log](../../01-governance/decision-log.md) row.

## The library

| File | What it decides |
|---|---|
| [instruction-spec.md](instruction-spec.md) | How to write a step: anatomy, sentence patterns, naming rules, banned vague phrasing |
| [round-structure.md](round-structure.md) | How a lab is paced: concept, then steps, then check-in; timing and slide types |
| [parts-glossary.md](parts-glossary.md) | One plain name per part, how to recognize it, and what's in each kit |
| [power-and-safety.md](power-and-safety.md) | Where power comes from, the never list, and known hardware traps |
| [inventory-and-audit.md](inventory-and-audit.md) | How to check a lab against the parts the club actually owns |
| [verification.md](verification.md) | What has to pass before a lab deck is published |
| [deck-kit/lab/](../../../deck-kit/lab/README.md) | The code that builds lab slides and breadboard diagrams |
| [templates/arduino-lab-round.md](../../../templates/arduino-lab-round.md) | Fill-in sheet for one round |
| [templates/arduino-lab-guide.md](../../../templates/arduino-lab-guide.md) | Skeleton for the officer's guide that goes in the semester folder |

## T-minus checklist

### 1 week out

- [ ] One outcome: "By the end, every table will have ___." One sentence.
- [ ] Draft each round on [templates/arduino-lab-round.md](../../../templates/arduino-lab-round.md), with every step written to [instruction-spec.md](instruction-spec.md).
- [ ] Run the [inventory audit](inventory-and-audit.md). Work out the station count and list the gaps.
- [ ] Post the prerequisites: laptop, Arduino IDE 2 **opened once on Wi-Fi** (its first start downloads the board package and built-in libraries), and any other library to install.

### 3 days out

- [ ] Build the deck with [deck-kit/lab/](../../../deck-kit/lab/README.md). Write the officer guide from [templates/arduino-lab-guide.md](../../../templates/arduino-lab-guide.md) into `semesters/<term>/meetings/`.
- [ ] Compile every sketch, run `check.mjs`, and review every step slide's screenshot ([verification.md](verification.md)).
- [ ] Dry-run the whole lab on a real kit from the slides alone.

### Day before

- [ ] Test every battery. Prep each table's parts (arms on servos, and so on). Bring cables.
- [ ] Publish the deck, walk it with real keys, and connect the phone remote.

## Day-of run sheet

Follow the officer guide for that week. Officers walk the room during every step. The presenter moves on when most tables show the "you should see" result, not when the slowest table finishes. Stuck tables get an officer, not a wait.

## After

- [ ] Write down what tables got stuck on, at which step, and why. Note any step that needed explaining out loud.
- [ ] Fix the spec here (a sentence pattern, a naming rule, a new trap), and add a line to "Rules learned" below with a link to that week's guide.
- [ ] Update `semesters/<term>/lab-inventory.md` with anything broken, lost, or used up.

## Rules learned

Each rule links to the lab that taught it.

| Rule | Why | From |
|---|---|---|
| One step per slide, with a "you should see" line | Four compressed steps on one slide were too vague to follow | [2026-10-08 guide](../../../semesters/2026-fall/meetings/2026-10-08-lab-guide.md) |
| Steps say "Take X. Plug one end into [hole] and the other into [hole]." | Verbs like "connect" and "wire it" left people guessing | 2026-10-08 |
| Change Blink's delay before the first upload | Some boards ship with Blink running and some don't, so a blinking L light proves nothing. Fast blinking always means the student's upload. | 2026-10-08, Elegoo tutorial lesson 2 |
| No driver chip in a first lab; use a servo | The L293D took a whole slide of pinouts before anything moved. A servo has its driver inside. | 2026-10-08 |
| Students open built-in examples and edit them | Typing whole sketches from a projector is slow and error-prone | 2026-10-08 |
| Say which way the power module goes on, every time | Backwards reverses the power (Elegoo warning) | 2026-10-08, Elegoo lesson 29 |
| Every round ends with a check-in that asks why | Reflection after each build, not one lecture at the end | 2026-10-08 |
| Show what Arduino hides (`main()` calls `setup()` then `loop()`) | Keeps the lab honest to plain C++ | 2026-10-08 |
