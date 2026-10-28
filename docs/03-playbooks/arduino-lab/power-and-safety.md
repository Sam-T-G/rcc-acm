# Power and safety

Say where the power comes from in every lab, in the officer guide and on the slide where it first matters. Beginners damage boards in two ways: a short, and power wired in the wrong place.

## The two power systems

| System | Path | Powers | Limit |
|---|---|---|---|
| Breadboard rails | 9V battery (or 9V adapter) → power module jack → module → + and - rails | LEDs, buttons in a loop, small motors | 6.5 to 9 V in; 5 V out per side; 700 mA max (Elegoo specs) |
| Arduino | Laptop USB → UNO → its 5V and GND pins | The board, a servo (red wire to 5V), button inputs | What the laptop's USB port gives. One micro servo is fine; more needs the rails |

The two systems never need to touch. **The one exception** is a part that's powered from the rails but takes a signal from the board (a servo on the rails, a motor driver, a transistor switch for a fan). Then add one jumper from a UNO GND pin to the - rail. That shared ground is what lets the part read the signal.

## The never list

These go on the slides where they apply, and in every officer guide.

1. **Never wire + straight to - with nothing in between.** That's a short. Every loop has a part in it.
2. **Never put the power module on backwards.** Its + pins go on the red lines and its - pins on the blue lines (Elegoo warning: backwards reverses the power).
3. **Never connect the UNO's 5V pin to the module's + rail.** Two supplies would be fighting each other.
4. **Never plug a battery or adapter straight into the breadboard.** It always goes through the module.
5. **Never feed the module more than 9 V.**
6. **Never drive a motor straight from a board pin.** A pin is safe at 20 mA, with 40 mA as the absolute limit (Arduino docs). A motor needs more, and it sends a voltage spike back when it stops.
7. **Never change wires with power on.** Switch the module off or unplug USB first. Make this the first step of each round.

## Known traps

| Trap | What happens | Fix built into the lab |
|---|---|---|
| Some boards ship with Blink loaded, some don't (Elegoo tutorial, lesson 2: "generally") | The L light may already blink, so blinking alone proves nothing | Change the delay before the first upload. A fast blink is unmistakably the student's upload. |
| Both module jumpers on OFF | Nothing turns on, not even the module's light | Step: "Pull each cap off and push it back on over the pins labelled 5V." |
| Split rails on some 830-hole boards | Half of each rail is dead | Look for a gap in the red and blue lines. Keep the circuit on the module's half. |
| Button legs on the same internal pair | The button acts like a plain wire, so it's always on | Always use opposite corners |
| INPUT_PULLUP missing | The input reads random values | The step says to add `pinMode(pin, INPUT_PULLUP);` |
| Servo on USB power resets the board | USB can't supply the servo's surge | Move the servo's red wire to the module's + rail and add a shared ground |
| IDE never opened online | No Arduino Uno in the board menu, no Servo examples | Members open IDE 2 once on Wi-Fi before the lab (its first start installs `arduino:avr` and the built-in libraries) |
| Built-in examples look read-only | They aren't: IDE 2 copies an opened example to a temporary folder, so it can be edited and uploaded | Nothing to fix. Saving asks for a new name. |
| Servo buzzes at 0 or 180 | Some servos can't reach the very ends | Use 10 and 170 |
| No port on some Windows laptops | The board's USB driver isn't installed | Elegoo tutorial lesson 0: install the driver from Device Manager. Read the small chip by the USB port to know which driver (ATmega16U2 or CH340) |
| USB-C-only laptops | The kit cable won't fit | Club USB-B to USB-C cables. The UNO R4 WiFi needs a USB-C cable. |
| LED backwards | It stays dark but isn't broken | Long leg to +. "Dark LED? Flip it around." |
| Diode across a motor put in backwards | Nothing happens until the transistor switches on; then the rails short through the diode and the transistor, which can get hot enough to burn | Stripe toward +, in the step text and the picture. Officers check every stripe before the switch-on step, and that step says to switch off and look if the fan doesn't spin. Never touch the transistor to check it. |
| Transistor base resistor on an UNO R4 WiFi | Its pins are rated for 8 mA (R4 WiFi datasheet); 220 Ω draws about 17 mA | 220 Ω on the Elegoo UNO R3 (under its 20 mA), 1 kΩ on an R4 |
| Servo sits at 90 until the code writes an angle | `attach()` starts it at 90 (Servo 1.3.0, DEFAULT_PULSE_WIDTH 1500) | Add `myservo.write(0);` right after `attach` when a lab needs the arm to start at 0 |
| A board wire into the wrong hole before the module is switched on | A jumper from the + rail to a pin back-powers the UNO through that pin, and an upload that drives the pin LOW then damages it. A ground jumper in the + rail lifts the UNO's GND to 5 V. | After wiring a rail-powered part to the board, a check step: trace the board wires, switch the module on with USB still out, and expect nothing to happen (no fan, no UNO lights) |
| Opening the Serial Monitor | It restarts the UNO, like an upload, so the sketch starts over | Say so on any slide that opens it |

## Sources

- Elegoo, *The Most Complete Starter Kit Tutorial for UNO*, V1.0.19.01.23: lessons 2, 3, 5, 9, and 29.
- Arduino documentation: pin current limits.
- The 2026-10-08 and 2026-10-15 lab guides in `semesters/2026-fall/meetings/`.
- PN2222A datasheet (Fairchild); Arduino UNO R4 WiFi datasheet (ABX00087), GPIO current.
