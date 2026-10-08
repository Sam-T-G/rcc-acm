# Parts glossary

One plain name per part. Use the name in the first column on slides, in guides, and out loud, for the whole lab. The second column is how a beginner finds it on the table.

Add a row the first time a lab uses a new part. Never rename a part between labs.

## Parts in use

| Name to use | How to recognize it | What it does, in plain words | Comes in |
|---|---|---|---|
| breadboard | White board covered in holes, with red and blue lines along both long edges | Where circuits get built. Each short row of 5 holes (a to e, or f to j) is connected inside; each long rail is connected along its length. | Elegoo kit (830 holes), plus spares |
| power module | Small board with a round jack, a switch, a light, and two small caps | Clips onto one end of the breadboard. Turns 6.5 to 9 V into 5 V (or 3.3 V) on the rails, up to 700 mA. | Elegoo kit |
| jumper caps (on the power module) | The two small caps, one on each side of the module | Each picks 5V, 3.3V, or OFF for its side. Both OFF means nothing turns on. | Elegoo kit, on the module |
| 9V battery | A 9 V battery on a cable ending in a round plug | Powers the module through its jack | Elegoo kit |
| 9V adapter | Black wall plug with a cable and the same round plug | Same job as the battery, from an outlet | Elegoo kit |
| UNO board | Blue board with a silver USB port and two long rows of pins | The Arduino: a small computer that runs one program over and over. Elegoo's copy of the Arduino UNO R3. | Elegoo kit |
| UNO R4 WiFi | White-labelled Arduino board with a USB-C port | Runs the same code. Needs a USB-C cable. | Club extras |
| USB cable | Cable with one square end and one flat end | Power and code from the laptop to the UNO | Elegoo kit (USB-A to USB-B); club USB-B to USB-C cables for USB-C laptops |
| jumper wire | Short wire with a metal pin on both ends | Connects two holes, or a hole and a pin | Elegoo kit (65, male to male), plus jumper kits |
| red LED | Small red dome with two legs, one longer | A light that only works one way around. The long leg is +. | Elegoo kit (5 red) |
| 220 Ω resistor | Tiny tan or blue part with colored stripes, grouped by value with a 220 label. Unlabelled: red, red, brown, gold (4-band) or red, red, black, black, brown (5-band) | Slows the electricity so an LED doesn't burn out | Elegoo kit |
| button | Small black square with a round top and four legs | A gap you close by pressing. The legs are connected in two pairs; opposite corners always go through the button. | Elegoo kit (5) |
| fan blade + motor | Small round motor with two wires, and a plastic three-blade fan | Spins when electricity flows through it. Swap the wires and it spins the other way. | Elegoo kit |
| servo | Small blue box with a shaft on top and a three-wire plug: brown, red, orange | A motor that turns to an angle from 0 to 180 degrees and holds it. Brown is ground, red is 5 V power, orange is the signal. | Elegoo kit (SG90), plus SG90 and MG90S packs |
| servo arm | Plastic piece from the bag that comes with the servo | Pushes onto the servo's shaft so you can see it turn | Servo packs |

## In the kits, not used in a lab yet

Use these names when a lab first uses them, and move each one up to the table above.

- **L293D chip:** drives a motor both ways. Needs its own wiring slide.
- **PN2222 and S8050 transistors:** a pin-controlled switch for a motor.
- **1N4007 diodes:** let current through one way only.
- **relay:** a switch the board can click on and off.
- **stepper motor and ULN2003 driver board.**
- **sensors:** ultrasonic, PIR motion, DHT11 temperature and humidity, photoresistor, thermistor, sound, water level, tilt switch.
- **inputs:** joystick, keypad, rotary encoder, IR receiver with remote, RFID reader.
- **displays:** LCD1602, 7-segment (one digit and four digit), MAX7219 LED matrix.
- **buzzers:** active and passive.
- **other parts:** potentiometers, RGB LED, 74HC595 shift register, GY-521 motion module, real-time clock module.

The full kit list and its sources are in [inventory-and-audit.md](inventory-and-audit.md).
