# Inventory and audit

Before a lab is written for good, check every part it uses against what the club owns right now. A lab that needs a part we don't have, or one more than we have, fails in the room.

The club's current stock lives in the semester folder, because it changes: `semesters/<term>/lab-inventory.md`. This page is the process.

## The audit, step by step

1. **List the parts per step.** Go through every step slide and write down each part it takes, with a count. Include cables, batteries, and anything that goes on a laptop.
2. **Total the parts per table.** A part used in two rounds counts once if it carries over (the button), or twice if both rounds need it at once.
3. **Compare against one kit.** Use the per-kit contents below and fill in a needed / in each kit / spare table.
4. **Find the limit.** The part with the fewest units across all kits and spares sets how many full stations you can run. In 2026-10-08 it was the power module and the fan motor: one per kit, so 6 full stations.
5. **Plan the overflow.** Work out which rounds can run without the limiting part, using the club extras (UNO R4 WiFi boards, spare servos and breadboards). Those become code-only stations.
6. **List the gaps.** Anything missing (cables), anything unknown (battery charge, whether an order arrived), and anything to look at on a real kit (split rails, motor wires). Mark each one **[CHECK]** in the guide and give it an owner.
7. **Write the prep checklist** from the gaps: test batteries, push arms onto servos, bring cables, post the IDE reminder.
8. **Record it** in the officer guide's audit section, and update `lab-inventory.md` if anything changed.

**Worked example:** the audit section of the [2026-10-08 lab guide](../../../semesters/2026-fall/meetings/2026-10-08-lab-guide.md).

## What one ELEGOO UNO R3 Project Most Complete Starter Kit holds

This is the kit the club bought: model EL-KIT-001, Amazon ASIN B01CZTLHGE, "ELEGOO UNO R3 Project Most Complete Starter Kit, Compatible with Arduino". Taken from that Amazon listing's Included Components (checked 2026-10-07), the Newegg listing, and Elegoo's tutorial. Elegoo sells other kits with similar names (Super Starter, Basic, Complete) that differ: some have no power module. Re-check against a real box when a lab depends on an exact count.

| Group | Contents |
|---|---|
| Board and wiring | 1 UNO R3 board, 1 USB cable (A to B), 1 830-hole breadboard, 65 jumper wires (male to male), 20 female-to-male wires, 1 prototype expansion board |
| Power | 1 power supply module, 1 9V battery with DC connector, 1 9V 1A adapter |
| Lights | 25 LEDs (5 each of white, yellow, blue, green, red), 1 RGB LED |
| Resistors | 30 × 220 Ω, and 10 each of 10 Ω, 100 Ω, 330 Ω, 1 kΩ, 2 kΩ, 5.1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ |
| Capacitors | 5 × 22 pF ceramic, 5 × 104 ceramic, 2 × 10 µF electrolytic, 2 × 100 µF electrolytic |
| Inputs | 5 small buttons, 2 potentiometers, 1 tilt switch, 1 joystick, 1 keypad, 1 rotary encoder, 1 IR receiver and remote |
| Motion | 1 servo (SG90), 1 small DC motor (Amazon lists it as "3V Servo Motor"; the tutorial says "Fan blade and 3-6v motor"), 1 stepper motor, 1 ULN2003 driver board, 1 L293D, 1 5V relay |
| Parts | 5 × PN2222 and 5 × S8050 transistors, 5 × 1N4007 diodes, 1 74HC595 |
| Sensors and modules | Photoresistors (2), thermistor, sound sensor, PIR motion sensor (HC-SR501), ultrasonic sensor, DHT11, water level sensor, GY-521, RC522 RFID, real-time clock |
| Displays and sound | LCD1602, 1-digit and 4-digit 7-segment displays, MAX7219 matrix module, active and passive buzzers |

**Sources:**

- [Amazon listing, ASIN B01CZTLHGE](https://www.amazon.com/dp/B01CZTLHGE)
- [Newegg listing](https://www.newegg.com/elegoo-el-kit-001-accessories/p/293-001C-00001)
- [Elegoo tutorial PDF, V1.0.19.01.23](https://m.media-amazon.com/images/I/C1wMkX1+N9L.pdf). Lesson parts lists: lesson 5 (two push switches), lesson 9 (SG90 and 3 male-to-male wires), lesson 29 (fan blade, 3 to 6 V motor, power supply module, 9V1A adapter).
