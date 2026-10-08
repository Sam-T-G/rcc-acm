"""labkit: slide builders and pictures for ACM @ RCC Arduino lab decks.

Spec: docs/03-playbooks/arduino-lab/ (instruction-spec.md first). Usage: deck-kit/lab/README.md.
Extracted 2026-10-07 from the 2026-10-08 lab generator. Every picture is an inline SVG,
viewBox 0 0 760 560, one unit = one stage pixel, labels at 32 px. Pure Python 3, no dependencies.
"""
import math
import re

def svg(cls, label, body):
    return (f'<figure class="viz viz--{cls}"><svg viewBox="0 0 760 560" role="img" '
            f'aria-label="{label}">{body}</svg></figure>')


def flow_dots(cls, pts, n=6):
    """n dots spread along a path; the deck <style> walks them with keyframes built from the same pts."""
    return ''.join(f'<circle class="ink {cls}" r="9" style="--n:{i}" transform="translate({pts[0][0]} {pts[0][1]})"/>' for i in range(n))


def rails(minus_x=0):
    return ('<line class="line" x1="0" y1="40" x2="760" y2="40"/><text x="0" y="28">+ rail</text>'
            f'<line class="line soft" x1="0" y1="530" x2="760" y2="530"/><text x="{minus_x}" y="518">- rail is ground</text>')


def lit_led(x=560):
    return f'<path class="acc" d="M{x+8} 228 v-42 a32 32 0 0 1 64 0 v42 z"/>'


def led_body():
    return ('<path class="box" d="M560 230 v-46 a40 40 0 0 1 80 0 v46 z"/><rect class="box" x="548" y="228" width="104" height="18" rx="4"/>'
            '<line class="line" x1="580" y1="246" x2="580" y2="470"/><line class="line" x1="620" y1="246" x2="620" y2="400"/>')


RESISTOR = ('<path class="line" d="M260 150 l12 -22 l24 44 l24 -44 l24 44 l24 -44 l24 44 l12 -22"/>'
            '<text x="332" y="100" text-anchor="middle">220 Ω</text>')


LOOP = [(110, 180), (110, 80), (640, 80), (640, 480), (110, 480), (110, 380)]


def loop_basic():
    batt = ('<rect class="box" x="50" y="180" width="120" height="200" rx="14"/>'
            '<text class="big" x="110" y="250" text-anchor="middle">+</text><text class="big" x="110" y="360" text-anchor="middle">-</text>')
    wires = ('<path class="wire" d="M110 180 V80 H330"/><path class="wire" d="M640 220 V80 H410"/>'
             '<path class="wire" d="M640 340 V480 H110 V380"/>')
    gap = '<g data-until="3"><path class="wire" d="M330 80 H410"/></g>'
    part = '<circle class="box" cx="640" cy="280" r="60"/><text x="600" y="190" text-anchor="end">part</text>'
    s1 = '<g data-stage="1"><g data-until="3">' + flow_dots('lp-e', LOOP) + '</g></g>'
    s2 = ('<g data-stage="2"><g data-until="3"><circle class="acc" cx="640" cy="280" r="48"/>'
          '<text class="t-acc" x="400" y="300" text-anchor="middle">it does work</text></g></g>')
    s3 = ('<g data-stage="3"><path class="line acc-stroke" d="M330 50 v60 M410 50 v60"/>'
          '<text class="t-acc" x="370" y="160" text-anchor="middle">a gap</text>'
          '<text x="400" y="300" text-anchor="middle">nothing flows</text></g>')
    s4 = ('<g data-stage="4"><path class="wire-acc" d="M170 220 H260 V340 H170"/>'
          '<text class="t-acc" x="200" y="400">a short</text>'
          '<text class="t-acc" x="200" y="440">+ straight to -</text></g>')
    return svg('lp', 'A power source with plus and minus ends wired in a loop through a part on the right. Dots of current leave plus, go through the part, which lights, and come back to minus. Then a gap opens in the top wire and nothing flows. Last, a wire straight from plus to minus with nothing in between: a short.',
               batt + wires + gap + part + s1 + s2 + s3 + s4)


LED_RAILS = [(240, 40), (240, 150), (440, 150), (440, 470), (580, 470), (580, 246), (620, 246), (620, 400), (700, 400), (700, 530)]


def led_rails():
    s1 = '<g data-stage="1"><path class="wire" d="M240 40 V150 H260"/>' + RESISTOR + '</g>'
    s2 = ('<g data-stage="2">' + led_body() + '<path class="wire" d="M404 150 H440 V470 H580"/>'
          '<text class="t-acc" x="566" y="430" text-anchor="end">long +</text><text class="t-acc" x="634" y="300">short -</text></g>')
    s3 = ('<g data-stage="3"><g data-until="4"><path class="wire" d="M620 400 H700 V530"/>' + lit_led() + flow_dots('lr-e', LED_RAILS)
          + '<text class="t-acc" x="20" y="330">it lights</text></g></g>')
    s4 = ('<g data-stage="4"><path class="wire" d="M620 400 H700 V440 q0 30 -40 50"/><circle class="ink" cx="700" cy="530" r="8"/>'
          '<text class="t-acc" x="20" y="330">no loop,</text><text class="t-acc" x="20" y="375">no light</text></g>')
    return svg('lr', 'The power module rails, plus on top and minus, which is ground, at the bottom. The plus rail runs through a 220 ohm resistor to the long, plus leg of an LED; the short, minus leg runs down to the minus rail and the LED lights while current flows round. Then the ground wire is pulled out and the LED goes dark.',
               rails() + s1 + s2 + s3 + s4)


def led_rails_lit():
    lit = '<path class="wire" d="M620 400 H700 V530"/>' + lit_led() + flow_dots('lr-e', LED_RAILS)
    return svg('lr', 'The finished LED loop: the plus rail runs through a 220 ohm resistor to the long leg of an LED, and the short leg runs to the minus rail, which is ground. The LED is lit.',
               rails() + '<path class="wire" d="M240 40 V150 H260"/>' + RESISTOR + led_body()
               + '<path class="wire" d="M404 150 H440 V470 H580"/>'
               + '<text class="t-acc" x="566" y="430" text-anchor="end">long +</text><text class="t-acc" x="634" y="300">short -</text>' + lit)


def tact(x, y, s=150, hot=False):
    """A four-leg push button from above, legs at the corners; hot lights the diagonal pair."""
    legs = [(x - 20, y + 20), (x + s + 20, y + 20), (x - 20, y + s - 20), (x + s + 20, y + s - 20)]
    out = f'<rect class="box" x="{x}" y="{y}" width="{s}" height="{s}" rx="12"/><circle class="ph" cx="{x + s/2}" cy="{y + s/2}" r="{s/4}"/>'
    for i, (lx, ly) in enumerate(legs):
        cls = 'acc' if hot and i in (0, 3) else 'ink'
        out += f'<circle class="{cls}" cx="{lx}" cy="{ly}" r="12"/>'
    return out


def button_loop():
    base = (rails() + '<path class="wire" d="M240 40 V150 H260"/>' + RESISTOR + led_body()
            + '<path class="wire" d="M404 150 H440 V470 H580"/><path class="wire" d="M620 400 H700 V410"/><path class="wire" d="M700 500 V530"/>'
            + '<circle class="ink" cx="700" cy="410" r="9"/><circle class="ink" cx="700" cy="500" r="9"/>')
    open_lever = '<line class="line" x1="700" y1="500" x2="748" y2="424"/>'
    closed = ('<line class="line" x1="700" y1="500" x2="700" y2="410"/>' + lit_led() + flow_dots('bl-e', BTN_RAILS))
    s1 = '<g data-stage="1"><text class="t-acc" x="760" y="380" text-anchor="end">a gap</text></g>'
    s2 = ('<g data-stage="2">' + tact(60, 230, 130, hot=True)
          + '<text class="t-acc" x="20" y="420">opposite</text><text class="t-acc" x="20" y="460">corners</text></g>')
    s3 = '<g data-stage="3"><path class="wire-acc" d="M620 400 H700 V410"/><path class="wire-acc" d="M700 500 V530"/></g>'
    s4 = (f'<g data-stage="4"><g class="bt-open">{open_lever}</g><g class="bt-on">{closed}</g></g>')
    pre = f'<g data-until="4">{open_lever}</g>'
    return svg('bt', 'The LED loop again, with a push button in the wire from the short leg to the minus rail. Drawn as a switch, it is a gap. From above, the button has four legs; the two on opposite corners light up. The button sits in the ground wire. Pressed, the gap closes, current flows and the LED lights; let go and it goes dark.',
               base + pre + s1 + s2 + s3 + s4)


BTN_RAILS = [(240, 40), (240, 150), (440, 150), (440, 470), (580, 470), (580, 246), (620, 246), (620, 400), (700, 400), (700, 530)]


def fan(cx, cy, cls, spin='', r=1.0):
    ry, rx, off = 42 * r, 18 * r, 46 * r
    return (f'<g class="{spin}"><circle fill="none" cx="{cx}" cy="{cy}" r="{off + ry}"/>'
            + ''.join(f'<ellipse class="{cls}" cx="{cx}" cy="{cy - off:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" transform="rotate({a} {cx} {cy})"/>' for a in (0, 120, 240))
            + f'<circle class="ink" cx="{cx}" cy="{cy}" r="{12 * r:.0f}"/></g>')


def arc_arrow(cx, cy, r, cw):
    """An arc over the top of a fan with its head showing the turn."""
    x1, x2 = cx - r * 0.7, cx + r * 0.7
    y = cy - r * 0.714
    if cw:
        return (f'<path class="line acc-stroke" d="M{x1:.0f} {y:.0f} A{r} {r} 0 0 1 {x2:.0f} {y:.0f}"/>'
                f'<path class="acc" d="M{x2 + 14:.0f} {y - 22:.0f} l6 34 l-32 -6 z"/>')
    return (f'<path class="line acc-stroke" d="M{x2:.0f} {y:.0f} A{r} {r} 0 0 0 {x1:.0f} {y:.0f}"/>'
            f'<path class="acc" d="M{x1 - 14:.0f} {y - 22:.0f} l-6 34 l32 -6 z"/>')


def motor_rails():
    cx, cy = 380, 280
    motor = (f'<circle class="box" cx="{cx}" cy="{cy}" r="100"/>'
             '<rect class="ink" x="266" y="270" width="18" height="20" rx="3"/><rect class="ink" x="476" y="270" width="18" height="20" rx="3"/>')
    a = '<path class="wire" d="M280 280 H150 V40"/><path class="wire" d="M480 280 H610 V530"/>'
    b = '<path class="wire" d="M280 280 H150 V530"/><path class="wire" d="M480 280 H610 V40"/>'
    b_pulled = '<path class="wire" d="M280 280 H150 V530"/><path class="wire" d="M480 280 H610 V120 q0 -30 40 -40"/><circle class="ink" cx="610" cy="40" r="8"/>'
    still = fan(cx, cy, 'ink')
    body = (rails(180) + motor
            + f'<g data-until="1">{still}</g>'
            + f'<g data-stage="1"><g data-until="2">{a}{fan(cx, cy, "acc", "mr-cw")}{arc_arrow(cx, cy, 150, True)}'
              '<text class="t-acc" x="380" y="470" text-anchor="middle">spins</text></g></g>'
            + f'<g data-stage="2"><g data-until="3">{b}{fan(cx, cy, "acc", "mr-ccw")}{arc_arrow(cx, cy, 150, False)}'
              '<text class="t-acc" x="380" y="470" text-anchor="middle">spins the other way</text></g></g>'
            + f'<g data-stage="3">{b_pulled}{still}<text x="380" y="470" text-anchor="middle">stopped</text></g>'
            + '<g data-stage="4"><text class="t-acc" x="380" y="110" text-anchor="middle">no code, just a loop</text></g>')
    return svg('mr', 'A motor with a fan blade, wired straight across the plus and minus rails. It spins. With its two wires swapped it spins the other way. With one wire pulled out it stops. No code, just a loop.', body)


def motor_rails_spin():
    cx, cy = 380, 280
    body = (rails(180) + f'<circle class="box" cx="{cx}" cy="{cy}" r="100"/>'
            '<rect class="ink" x="266" y="270" width="18" height="20" rx="3"/><rect class="ink" x="476" y="270" width="18" height="20" rx="3"/>'
            '<path class="wire" d="M280 280 H150 V40"/><path class="wire" d="M480 280 H610 V530"/>'
            + fan(cx, cy, 'acc', 'mr-cw') + arc_arrow(cx, cy, 150, True)
            + '<text class="t-acc" x="380" y="470" text-anchor="middle">swap the wires to reverse</text>')
    return svg('mr', 'A motor with a fan blade wired straight across the plus and minus rails, spinning. Swapping its two wires reverses it.', body)


def motor_rails_dir(reverse=False):
    cx, cy = 380, 280
    a = ('<path class="wire" d="M280 280 H150 V530"/><path class="wire" d="M480 280 H610 V40"/>' if reverse
         else '<path class="wire" d="M280 280 H150 V40"/><path class="wire" d="M480 280 H610 V530"/>')
    body = (rails(180) + f'<circle class="box" cx="{cx}" cy="{cy}" r="100"/>'
            '<rect class="ink" x="266" y="270" width="18" height="20" rx="3"/><rect class="ink" x="476" y="270" width="18" height="20" rx="3"/>'
            + a + fan(cx, cy, 'acc', 'mr-ccw' if reverse else 'mr-cw') + arc_arrow(cx, cy, 150, not reverse)
            + f'<text class="t-acc" x="380" y="470" text-anchor="middle">{"the other way" if reverse else "it spins"}</text>')
    return svg('mr', 'A fan motor wired across the plus and minus rails, spinning' + (' the other way after its wires are swapped.' if reverse else '.'), body)


def motor_blade():
    o = ('<rect class="box" x="140" y="210" width="260" height="150" rx="30"/><text x="270" y="300" text-anchor="middle">motor</text>'
         '<rect class="ink" x="400" y="276" width="70" height="18" rx="4"/>'
         + ''.join(f'<ellipse class="acc" cx="540" cy="200" rx="28" ry="80" transform="rotate({a} 540 285)"/>' for a in (0, 120, 240))
         + '<circle class="ink" cx="540" cy="285" r="20"/><path class="line acc-stroke" d="M500 420 h-60 M440 420 l18 -14 M440 420 l18 14"/>'
         '<text class="t-acc" x="520" y="470" text-anchor="middle">push it on</text>')
    return svg('mb', 'The fan blade being pushed onto the motor shaft.', o)


def ground():
    floor = '<line class="line" x1="0" y1="470" x2="360" y2="470"/>'
    uno = ('<rect class="box" x="40" y="170" width="180" height="300" rx="14"/><text x="130" y="420" text-anchor="middle">UNO</text>'
           '<rect class="ink" x="208" y="208" width="24" height="24" rx="3"/><text x="200" y="230" text-anchor="end">pin</text>')
    chip_at = lambda dy: (f'<rect class="chip" x="540" y="{170 - dy}" width="180" height="300" rx="10"/>'
                          f'<text class="chip-t" x="630" y="{420 - dy}" text-anchor="middle">servo</text>')
    s1 = ('<g data-stage="1"><path class="line acc-stroke" d="M280 466 V224 M266 238 l14 -16 l14 16"/>'
          '<text class="t-acc" x="300" y="360">5 V</text></g>')
    s2 = '<g data-stage="2"><line class="wire-acc" x1="0" y1="470" x2="360" y2="470"/><text class="t-acc" x="0" y="530">ground = 0 V</text></g>'
    s3 = '<g data-stage="3"><path class="wire" d="M232 220 H540"/><text x="386" y="196" text-anchor="middle">signal</text></g>'
    lifted = (f'<g data-until="4">{chip_at(80)}<line class="dash" x1="400" y1="390" x2="760" y2="390"/>'
              '<text class="t-acc" x="600" y="450" text-anchor="middle">5 V above what?</text></g>')
    shared = (f'<g data-stage="4">{chip_at(0)}<line class="wire-acc" x1="0" y1="470" x2="760" y2="470"/>'
              '<text class="t-acc" x="760" y="530" text-anchor="end">one shared floor</text></g>')
    return svg('gd', 'Ground drawn as a floor. The UNO stands on it and its pin sits 5 volts above it, measured with an arrow from the floor. The floor is labeled ground, 0 volts. A signal wire runs from the pin to a servo. Without a shared ground the servo floats on its own dashed floor, asking 5 volts above what; with the grounds wired together both stand on one floor.',
               floor + uno + s1 + s2 + s3 + lifted + shared)


def button_pin():
    out = ('<rect class="box" x="0" y="100" width="170" height="380" rx="16"/><text x="85" y="300" text-anchor="middle">UNO</text>'
           '<rect class="ink" x="160" y="188" width="24" height="24" rx="3"/><text x="150" y="211" text-anchor="end">2</text>'
           '<rect class="ink" x="160" y="428" width="24" height="24" rx="3"/><text x="150" y="451" text-anchor="end">GND</text>')
    s1 = '<g data-stage="1"><rect class="ph" x="250" y="300" width="300" height="22" rx="6"/>' + tact(330, 236, 150) + '</g>'
    s2 = '<g data-stage="2"><path class="wire" d="M184 200 H310 V256"/></g>'
    s3 = ('<g data-stage="3"><path class="wire" d="M500 366 V440 H184"/><circle class="acc" cx="500" cy="366" r="12"/><circle class="acc" cx="310" cy="256" r="12"/>'
          '<text class="t-acc" x="230" y="500">ground again</text></g>')
    s4 = ('<g data-stage="4"><text class="bp-up" x="560" y="200">let go</text><text class="bp-up" x="560" y="240">HIGH</text>'
          '<text class="t-acc bp-down" x="560" y="320">pressed</text><text class="t-acc bp-down" x="560" y="360">LOW</text>'
          '<circle class="acc bp-down" cx="405" cy="311" r="37"/></g>')
    return svg('bp', 'A push button across the middle gap of the breadboard. One corner is wired to UNO pin 2, the opposite corner to a GND pin on the UNO. Let go, pin 2 reads HIGH; pressed, it is connected to ground and reads LOW.', out + s1 + s2 + s3 + s4)


def servo_need():
    body = ('<rect class="box" x="0" y="230" width="150" height="100" rx="14"/><text x="75" y="292" text-anchor="middle">pin</text>'
            '<g data-stage="1"><text class="t-acc" x="75" y="380" text-anchor="middle">20 mA</text></g>'
            '<g data-until="4"><circle class="box" cx="640" cy="280" r="90"/>' + fan(640, 280, 'ink') + '<line class="line" x1="150" y1="280" x2="550" y2="280"/>'
            '<g data-stage="2"><text class="t-acc" x="640" y="430" text-anchor="middle">needs more</text>'
            '<path class="line acc-stroke" d="M320 240 l80 80 M400 240 l-80 80"/></g>'
            '<g data-stage="3"><path class="line acc-stroke pm-spike" d="M560 150 l20 -40 l14 30 l20 -60 l14 40"/><text class="t-acc" x="560" y="50">spike back</text></g></g>'
            '<g data-stage="4"><line class="line" x1="150" y1="280" x2="470" y2="280"/><text x="300" y="260" text-anchor="middle">signal</text>'
            '<rect class="box" x="470" y="200" width="270" height="170" rx="16"/><rect class="chip" x="500" y="250" width="120" height="70" rx="8"/>'
            '<text class="chip-t" x="560" y="296" text-anchor="middle">driver</text><text x="680" y="296" text-anchor="middle">M</text>'
            '<text class="t-acc" x="605" y="430" text-anchor="middle">servo</text>'
            '<rect class="box" x="520" y="40" width="170" height="80" rx="12"/><text x="605" y="92" text-anchor="middle">5V</text>'
            '<line class="wire-fat" x1="605" y1="120" x2="605" y2="200"/></g>')
    return svg('pm', 'An Arduino pin that gives about 20 milliamps tries to run a fan motor that needs far more, and the link is crossed out. The motor also sends a spike back when it stops. Then a servo replaces it: the pin only sends a signal, and the servo has its own driver inside, powered from 5V.', body)


def servo_wiring():
    uno = ('<rect class="box" x="0" y="100" width="170" height="380" rx="16"/><text x="85" y="150" text-anchor="middle">UNO</text>'
           '<rect class="ink" x="160" y="188" width="24" height="24" rx="3"/><text x="150" y="211" text-anchor="end">9</text>'
           '<rect class="ink" x="160" y="288" width="24" height="24" rx="3"/><text x="150" y="311" text-anchor="end">5V</text>'
           '<rect class="ink" x="160" y="388" width="24" height="24" rx="3"/><text x="150" y="411" text-anchor="end">GND</text>')
    servo = ('<rect class="box" x="470" y="250" width="250" height="130" rx="12"/><text x="640" y="350" text-anchor="middle">servo</text>'
             '<g class="sv-swing"><line class="wire-fat" x1="540" y1="250" x2="540" y2="160"/></g><circle class="ink" cx="540" cy="250" r="20"/>')
    s1 = ('<g data-stage="1"><path class="dash" d="M440 250 A100 100 0 0 1 640 250"/>'
          '<text class="t-acc" x="440" y="222" text-anchor="middle">0</text><text class="t-acc" x="640" y="222" text-anchor="middle">180</text></g>')
    s2 = '<g data-stage="2"><path class="wire" d="M470 340 H300 V400 H184"/><text x="200" y="386">brown</text></g>'
    s3 = '<g data-stage="3"><path class="wire" d="M470 315 H330 V300 H184"/><text x="200" y="286">red</text></g>'
    s4 = '<g data-stage="4"><path class="wire-acc" d="M470 290 H360 V200 H184"/><text class="t-acc" x="200" y="186">orange</text></g>'
    return svg('sv', 'A servo with an arm on top that turns from 0 to 180 degrees. Its three wires run to the UNO: brown to GND, red to 5V, and orange, the signal, to pin 9.', uno + servo + s1 + s2 + s3 + s4)


def angles():
    cx, cy, r = 380, 440, 250
    def arm(deg, cls='wire-fat', extra=''):
        import math
        a = math.radians(180 - deg)
        return f'<line class="{cls}" x1="{cx}" y1="{cy}" x2="{cx + r * 0.85 * math.cos(a):.0f}" y2="{cy - r * 0.85 * math.sin(a):.0f}" {extra}/>'
    out = (f'<path class="line soft" d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}"/>'
           f'<text x="{cx - r}" y="{cy + 50}" text-anchor="middle">0</text><text x="{cx}" y="{cy - r - 20}" text-anchor="middle">90</text>'
           f'<text x="{cx + r}" y="{cy + 50}" text-anchor="middle">180</text>')
    for k, deg in enumerate((0, 90, 180)):
        out += f'<g data-stage="{k + 1}"><g data-until="{k + 2}">{arm(deg)}</g></g>'
    out += f'<g data-stage="4"><g class="an-sweep">{arm(90, "wire-acc")}</g><text class="t-acc" x="{cx}" y="{cy + 100}" text-anchor="middle">count up, it sweeps</text></g>'
    out += f'<circle class="ink" cx="{cx}" cy="{cy}" r="22"/>'
    return svg('an', 'A half-circle dial from 0 to 180 degrees. The servo arm points to 0, then 90 straight up, then 180. Last, the arm sweeps across as the code counts through every angle.', out)


def snippet(name, label, lines, note=None):
    """Code drawn at the 32 px diagram size, monospace, indents kept; at most 38 characters a line."""
    out = '<rect class="card" x="0" y="0" width="760" height="560" rx="16"/>'
    out += f'<text class="soft" x="32" y="56">{name}</text><g data-code="">'
    y0, dy = (120, 46) if len(lines) <= 8 else (104, 40)
    for k, l in enumerate(lines):
        assert len(l) <= 38, l
        ind = len(l) - len(l.lstrip(' '))
        t = l.strip().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        cls = ' class="t-acc"' if l.strip().startswith('//') else ''
        if t:
            out += f'<text{cls} x="{32 + ind * 19.2:.0f}" y="{y0 + k * dy}">{t}</text>'
    out += '</g>'
    if note:
        out += f'<text class="t-acc" x="32" y="530">{note}</text>'
    return svg('sn', label, out)


def snippet_hl(name, label, lines, hl=(), note=None):
    out = '<rect class="card" x="0" y="0" width="760" height="560" rx="16"/>'
    out += f'<text class="soft" x="32" y="56">{name}</text><g data-code="">'
    y0, dy = (120, 46) if len(lines) <= 8 else (104, 40)
    for k, l in enumerate(lines):
        assert len(l) <= 38, l
        ind = len(l) - len(l.lstrip(' '))
        t = l.strip().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        if not t:
            continue
        y = y0 + k * dy
        if k in hl:
            out += f'<rect class="ph" x="16" y="{y - 32}" width="728" height="{dy}" rx="6"/>'
        cls = ' class="t-acc"' if k in hl else (' class="soft"' if t.startswith('//') else '')
        out += f'<text{cls} x="{32 + ind * 19.2:.0f}" y="{y}">{t}</text>'
    out += '</g>'
    if note:
        out += f'<text class="t-acc" x="32" y="530">{note}</text>'
    return svg('sn', label, out)


def parts_kit():
    def cell(col, row, icon, name):
        x0, y0 = col * 253, row * 140
        return f'<g transform="translate({x0} {y0})">{icon}<text x="126" y="128" text-anchor="middle">{name}</text></g>'
    holes = ''.join(f'<circle class="hole" cx="{46 + c * 16}" cy="{y}" r="3"/>' for c in range(11) for y in (30, 42, 66, 78))
    breadboard = f'<rect class="card" x="26" y="14" width="200" height="80" rx="8"/><line class="dash" x1="34" y1="54" x2="218" y2="54"/>{holes}'
    module = ('<rect class="box" x="50" y="14" width="150" height="80" rx="8"/><rect class="ink" x="60" y="40" width="34" height="30" rx="4"/>'
              '<rect class="box" x="108" y="44" width="26" height="20" rx="3"/><rect class="acc" x="152" y="24" width="20" height="14" rx="2"/><rect class="acc" x="152" y="70" width="20" height="14" rx="2"/>')
    battery = ('<rect class="box" x="70" y="22" width="60" height="78" rx="6"/><rect class="ink" x="80" y="12" width="14" height="10"/><rect class="ink" x="106" y="12" width="14" height="10"/>'
               '<path class="line" d="M130 60 C170 60 160 40 190 40"/><rect class="ink" x="190" y="30" width="34" height="20" rx="4"/>')
    adapter = ('<rect class="box" x="70" y="24" width="64" height="64" rx="8"/><line class="line" x1="88" y1="24" x2="88" y2="8"/><line class="line" x1="116" y1="24" x2="116" y2="8"/>'
               '<path class="line" d="M134 70 C170 70 160 40 190 40"/><rect class="ink" x="190" y="30" width="34" height="20" rx="4"/>')
    uno = ('<rect class="box" x="36" y="16" width="180" height="84" rx="8"/><rect class="box" x="24" y="30" width="36" height="28" rx="3"/>'
           '<rect class="ink" x="90" y="22" width="110" height="10" rx="2"/><rect class="ink" x="110" y="86" width="90" height="8" rx="2"/><rect class="chip" x="110" y="56" width="80" height="18" rx="3"/>')
    usb = ('<rect class="ink" x="30" y="44" width="44" height="22" rx="3"/><path class="line" d="M74 55 C120 20 140 90 180 55"/>'
           '<rect class="ink" x="180" y="40" width="30" height="30" rx="4"/>')
    jumper = '<path class="wire-acc" d="M50 80 C70 10 180 10 200 80"/><rect class="ink" x="44" y="78" width="12" height="20" rx="2"/><rect class="ink" x="194" y="78" width="12" height="20" rx="2"/>'
    led = ('<path class="acc" d="M106 60 v-30 a20 20 0 0 1 40 0 v30 z"/><rect class="box" x="100" y="58" width="52" height="10" rx="3"/>'
           '<line class="line" x1="116" y1="68" x2="116" y2="96"/><line class="line" x1="136" y1="68" x2="136" y2="88"/>')
    resistor = ('<line class="line" x1="40" y1="55" x2="88" y2="55"/><line class="line" x1="164" y1="55" x2="212" y2="55"/>'
                '<rect class="box" x="88" y="40" width="76" height="30" rx="14"/>'
                + ''.join(f'<rect class="ink" x="{x}" y="41" width="6" height="28"/>' for x in (102, 116, 130, 148)))
    button = ('<rect class="box" x="90" y="20" width="72" height="72" rx="8"/><circle class="ph" cx="126" cy="56" r="20"/>'
              + ''.join(f'<rect class="ink" x="{x}" y="{y}" width="14" height="8" rx="2"/>' for x in (76, 162) for y in (30, 74)))
    fanmotor = ('<rect class="box" x="40" y="38" width="80" height="44" rx="10"/><line class="line" x1="120" y1="60" x2="140" y2="60"/>'
                + ''.join(f'<ellipse class="acc" cx="168" cy="34" rx="10" ry="26" transform="rotate({a} 168 60)"/>' for a in (0, 120, 240))
                + '<circle class="ink" cx="168" cy="60" r="7"/>')
    servo = ('<rect class="box" x="70" y="40" width="112" height="56" rx="6"/><rect class="box" x="56" y="54" width="140" height="10" rx="3"/>'
             '<circle class="ink" cx="100" cy="40" r="10"/><line class="wire-fat" x1="100" y1="40" x2="150" y2="14"/>')
    out = (cell(0, 0, breadboard, 'breadboard') + cell(1, 0, module, 'power module') + cell(2, 0, battery, '9V battery')
           + cell(0, 1, uno, 'UNO R3 board') + cell(1, 1, usb, 'USB cable') + cell(2, 1, adapter, '9V adapter')
           + cell(0, 2, jumper, 'jumper wire') + cell(1, 2, led, 'red LED') + cell(2, 2, resistor, 'resistor')
           + cell(0, 3, button, 'button') + cell(1, 3, fanmotor, 'fan + motor') + cell(2, 3, servo, 'servo'))
    return svg('pk', 'Every part for today, drawn and named: breadboard, power module, 9V battery with its barrel plug, UNO R3 board, USB cable, 9V wall adapter, jumper wire, red LED, resistor, push button, fan blade on a motor, and a servo with its arm.', out)


def BX(r):
    return 110 + (r - 1) * 28


BY = {'+t': 96, '-t': 122, 'a': 168, 'b': 194, 'c': 220, 'd': 246, 'e': 272,
      'f': 314, 'g': 340, 'h': 366, 'i': 392, 'j': 418, '-b': 464, '+b': 490}


def bb(parts, hi=(), lit=False, on=False):
    """parts: names from module, jumpers, battery, resistor, led, ground, button, btn_in, btn_out."""
    acc = lambda n: n in hi
    o = '<rect class="card" x="90" y="78" width="630" height="430" rx="10"/><rect class="ph" x="96" y="284" width="618" height="18" rx="4"/>'
    for k in ('+t', '-t', '-b', '+b'):
        o += ''.join(f'<circle class="hole" cx="{BX(r)}" cy="{BY[k]}" r="4"/>' for r in range(1, 23))
    for k in 'abcdefghij':
        o += ''.join(f'<circle class="hole" cx="{BX(r)}" cy="{BY[k]}" r="4"/>' for r in range(1, 23))
    o += ''.join(f'<text x="{BX(r)}" y="62" text-anchor="middle">{r}</text>' for r in (1, 5, 10, 15, 20))
    for k, t in (('+t', '+'), ('-t', '-'), ('a', 'a'), ('e', 'e'), ('f', 'f'), ('j', 'j'), ('-b', '-'), ('+b', '+')):
        o += f'<text x="744" y="{BY[k] + 11}" text-anchor="middle">{t}</text>'
    def wire(d, n):
        return f'<path class="{"wire-acc" if acc(n) else "wire"}" d="{d}"/>'
    def dot(r, k, n):
        return f'<circle class="{"acc" if acc(n) else "ink"}" cx="{BX(r)}" cy="{BY[k]}" r="7"/>'
    if 'module' in parts:
        c = 'acc-stroke' if acc('module') else ''
        o += (f'<rect class="box" x="8" y="80" width="76" height="426" rx="8"/>'
              + (f'<rect class="line acc-stroke" x="4" y="76" width="84" height="434" rx="10"/>' if acc('module') else '')
              + '<rect class="ink" x="18" y="258" width="40" height="60" rx="4"/><rect class="box" x="24" y="380" width="30" height="30" rx="4"/>'
              + f'<circle class="{"acc" if on else "card"}" cx="46" cy="210" r="11"/>')
    if 'jumpers' in parts:
        cl = 'acc' if acc('jumpers') else 'ink'
        o += f'<rect class="{cl}" x="52" y="88" width="26" height="22" rx="3"/><rect class="{cl}" x="52" y="474" width="26" height="22" rx="3"/>'
    if 'battery' in parts:
        cl = 'acc' if acc('battery') else 'ink'
        o += f'<rect class="{cl}" x="10" y="270" width="52" height="36" rx="4"/><text class="{"t-acc" if acc("battery") else ""}" x="40" y="350" text-anchor="middle">9V</text>'
    if 'resistor' in parts:
        x1, y1, x2, y2 = BX(6), BY['+t'], BX(10), BY['a']
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        st = ' style="stroke: var(--acm-primary)"' if acc('resistor') else ''
        o += (f'<line class="line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
              f'<line class="wire-fat"{st} x1="{mx - 14}" y1="{my - 12}" x2="{mx + 14}" y2="{my + 12}"/>' + dot(6, '+t', 'resistor') + dot(10, 'a', 'resistor'))
    if 'led' in parts:
        cx, cy = BX(10) + 14, BY['c'] + 42
        o += (f'<line class="line" x1="{BX(10)}" y1="{BY["c"]}" x2="{cx - 8}" y2="{cy}"/><line class="line" x1="{BX(11)}" y1="{BY["c"]}" x2="{cx + 8}" y2="{cy}"/>'
              f'<circle class="{"acc" if lit else "box"}" cx="{cx}" cy="{cy}" r="18"/>'
              + (f'<circle class="line acc-stroke" cx="{cx}" cy="{cy}" r="24"/>' if acc('led') else '')
              + dot(10, 'c', 'led') + dot(11, 'c', 'led'))
    if 'ground' in parts:
        o += wire(f'M{BX(11)} {BY["a"]} V{BY["-t"]}', 'ground') + dot(11, 'a', 'ground') + dot(11, '-t', 'ground')
    if 'button' in parts:
        x0, x1 = BX(15) - 16, BX(17) + 16
        o += (f'<rect class="box" x="{x0}" y="{BY["e"] - 16}" width="{x1 - x0}" height="{BY["f"] - BY["e"] + 32}" rx="8"/>'
              + (f'<rect class="line acc-stroke" x="{x0 - 6}" y="{BY["e"] - 22}" width="{x1 - x0 + 12}" height="{BY["f"] - BY["e"] + 44}" rx="10"/>' if acc('button') else '')
              + f'<circle class="ph" cx="{BX(16)}" cy="{(BY["e"] + BY["f"]) / 2}" r="16"/>'
              + ''.join(dot(r, k, 'button') for r in (15, 17) for k in 'ef'))
    if 'btn_in' in parts:
        o += wire(f'M{BX(11)} {BY["a"]} Q{BX(13)} {BY["a"] - 44} {BX(15)} {BY["a"]}', 'btn_in') + dot(11, 'a', 'btn_in') + dot(15, 'a', 'btn_in')
    if 'btn_out' in parts:
        o += wire(f'M{BX(17)} {BY["j"]} V{BY["-b"]}', 'btn_out') + dot(17, 'j', 'btn_out') + dot(17, '-b', 'btn_out')
    return svg('bb2', 'A breadboard drawn hole by hole, rows numbered 1 to 22 across the top, rails marked plus and minus, rows a to e above the middle gap and f to j below. ' + ', '.join(parts) + ' placed; the newest part is drawn in orange.', o)


def ide_menu(items, title='Arduino IDE'):
    o = f'<rect class="card" x="0" y="0" width="760" height="560" rx="16"/><text class="soft" x="32" y="56">{title}</text>'
    for k, t in enumerate(items):
        w = 40 + len(t) * 20
        x, y = 32 + k * 70, 100 + k * 100
        last = k == len(items) - 1
        o += (f'<rect class="{"line acc-stroke" if last else "box"}" x="{x}" y="{y}" width="{w}" height="64" rx="10"/>'
              f'<text class="{"t-acc" if last else ""}" x="{x + 20}" y="{y + 43}">{t}</text>')
        if not last:
            o += f'<path class="line" d="M{x + 30} {y + 64} v26 h40"/>'
    return svg('ide', 'In the Arduino IDE menus: ' + ', then '.join(items) + '.', o)


def laptop_uno(plugged=True):
    o = ('<rect class="box" x="20" y="150" width="260" height="170" rx="10"/><rect class="ph" x="40" y="168" width="220" height="134" rx="4"/>'
         '<path class="box" d="M0 320 h300 l-20 30 h-260 z"/><text x="150" y="400" text-anchor="middle">laptop</text>'
         '<rect class="box" x="470" y="170" width="270" height="170" rx="12"/><text x="605" y="270" text-anchor="middle">UNO</text>'
         '<rect class="ink" x="450" y="200" width="40" height="40" rx="4"/>')
    if plugged:
        o += '<path class="wire-acc" d="M300 250 C360 250 380 220 450 220"/><text class="t-acc" x="380" y="320" text-anchor="middle">USB</text>'
    else:
        o += ('<path class="wire" d="M300 250 C330 250 340 240 360 240"/><path class="wire" d="M400 230 C420 225 430 220 450 220"/>'
              '<text class="t-acc" x="380" y="320" text-anchor="middle">unplugged</text>')
    return svg('lu', 'A laptop and the UNO board, ' + ('joined by a USB cable.' if plugged else 'with the USB cable pulled out.'), o)


def servo_arm():
    o = ('<rect class="box" x="200" y="250" width="360" height="170" rx="14"/><rect class="box" x="160" y="290" width="440" height="30" rx="6"/>'
         '<text x="380" y="390" text-anchor="middle">servo</text><circle class="ink" cx="300" cy="250" r="26"/>'
         '<line class="wire-fat" style="stroke: var(--acm-primary)" x1="300" y1="160" x2="300" y2="60"/><circle class="acc" cx="300" cy="110" r="22"/>'
         '<path class="line acc-stroke" d="M360 90 v120 M346 196 l14 14 l14 -14"/><text class="t-acc" x="400" y="140">push the arm on</text>')
    return svg('sa', 'A servo with a plastic arm being pushed straight down onto the white shaft on top.', o)






def breadboard():
    cols = 14
    x0, dx = 60, 46
    out = '<rect class="card" x="20" y="10" width="720" height="540" rx="16"/>'
    # rails
    for ry in (40, 72, 488, 520):
        for c in range(cols):
            out += f'<rect class="hole" x="{x0 + c*dx}" y="{ry-7}" width="14" height="14" rx="2"/>'
    out += '<text x="34" y="52" class="soft-t">+</text><text x="34" y="84" class="soft-t">-</text>'
    out += '<line class="dash" x1="40" y1="100" x2="720" y2="100"/><line class="dash" x1="40" y1="460" x2="720" y2="460"/>'
    # terminal strips: each column of five holes is one wire
    for c in range(cols):
        for r in range(5):
            out += f'<rect class="hole" x="{x0 + c*dx}" y="{130 + r*30}" width="14" height="14" rx="2"/>'
            out += f'<rect class="hole" x="{x0 + c*dx}" y="{312 + r*30}" width="14" height="14" rx="2"/>'
    out += '<rect class="ph" x="40" y="276" width="680" height="22" rx="6"/>'
    s1 = (f'<g data-stage="1"><rect class="line acc-stroke bb-pulse" x="{x0 + 2*dx - 10}" y="118" width="34" height="160" rx="8"/>'
          f'<rect class="line acc-stroke bb-pulse" x="{x0 + 2*dx - 10}" y="300" width="34" height="160" rx="8"/></g>')
    chip_x = x0 + 7*dx - 8
    s2 = (f'<g data-stage="2"><rect class="chip" x="{chip_x}" y="226" width="{3*dx + 30}" height="122" rx="6"/>'
          f'<text class="chip-t" x="{chip_x + (3*dx+30)/2:.0f}" y="298" text-anchor="middle">chip</text></g>')
    s3 = (f'<g data-stage="3"><rect class="line acc-stroke bb-pulse" x="{x0-10}" y="26" width="{cols*dx - 12}" height="28" rx="8"/>'
          f'<rect class="line acc-stroke bb-pulse" x="{x0-10}" y="58" width="{cols*dx - 12}" height="28" rx="8"/></g>')
    return svg('bb', 'A breadboard from above. Each short column of five holes is one connected strip, top and bottom halves split by a gap down the middle. A chip straddles the gap. The long rails along the top and bottom edges run the whole length.', out + s1 + s2 + s3)


def uno():
    b = ('<rect class="box" x="60" y="40" width="660" height="470" rx="24"/>'
         '<rect class="box" x="20" y="90" width="130" height="120" rx="6"/>'   # USB-B
         '<rect class="ink" x="20" y="380" width="120" height="90" rx="10"/>'  # barrel jack
         '<circle class="box" cx="190" cy="80" r="18"/>'                       # reset
         '<rect class="chip" x="330" y="300" width="330" height="70" rx="8"/><text class="chip-t" x="495" y="347" text-anchor="middle">ATmega328P</text>')
    holes = ''
    for i in range(14):
        holes += f'<rect class="ink" x="{246 + i*32}" y="64" width="16" height="16" rx="2"/>'
    head = f'<rect class="box" x="236" y="54" width="456" height="36" rx="4"/>{holes}'
    nums = '<text x="254" y="128" text-anchor="middle">13</text><text x="670" y="128" text-anchor="middle">0</text>'
    led = '<rect class="lled" x="238" y="160" width="30" height="18" rx="4"/><text x="284" y="182">L</text>'
    pw = '<rect class="box" x="240" y="452" width="230" height="36" rx="4"/><rect class="box" x="500" y="452" width="190" height="36" rx="4"/>'
    pwh = ''.join(f'<rect class="ink" x="{252 + i*28}" y="462" width="14" height="14" rx="2"/>' for i in range(8))
    pwh += ''.join(f'<rect class="ink" x="{514 + i*28}" y="462" width="14" height="14" rx="2"/>' for i in range(6))
    lab = '<text x="355" y="438" text-anchor="middle">5V GND</text><text x="595" y="438" text-anchor="middle">A0-A5</text>'
    s1 = '<g data-stage="1"><rect class="line acc-stroke" x="10" y="80" width="150" height="140" rx="10"/><text class="t-acc" x="85" y="260" text-anchor="middle">USB</text></g>'
    s2 = '<g data-stage="2"><rect class="line acc-stroke" x="228" y="46" width="472" height="52" rx="8"/><text class="t-acc" x="464" y="182" text-anchor="middle">DIGITAL 0-13</text></g>'
    s3 = ('<g data-stage="3">'
          + ''.join(f'<rect class="acc" x="{254 + (13 - p) * 32 - 8}" y="64" width="16" height="16" rx="2"/>'
                    f'<text class="t-acc" x="{254 + (13 - p) * 32}" y="36" text-anchor="middle">{p}</text>' for p in (9, 2))
          + '<text class="t-acc" x="382" y="240" text-anchor="middle">servo</text><text class="t-acc" x="606" y="240" text-anchor="middle">button</text></g>')
    s4 = '<g data-stage="4"><rect class="line acc-stroke" x="300" y="444" width="110" height="52" rx="8"/></g>'
    body = b + head + nums + led + pw + pwh + lab + s1 + s2 + s3 + s4
    return svg('uno', 'A drawing of the UNO board from above: the USB port on the left, the row of digital pins 13 to 0 along the top with pin 9 marked for the servo and pin 2 for the button, the small L light by pin 13, the main chip, and the power and analog pins along the bottom.', body)


def power():
    body = ('<rect class="card" x="0" y="40" width="760" height="460" rx="16"/>'
            '<line class="line" x1="230" y1="100" x2="740" y2="100"/><text x="740" y="86" text-anchor="end">+</text>'
            '<line class="line soft" x1="230" y1="150" x2="740" y2="150"/><text x="740" y="190" text-anchor="end">-</text>'
            '<g data-stage="1"><rect class="box" x="20" y="60" width="210" height="330" rx="12"/>'
            '<rect class="ink" x="40" y="300" width="80" height="70" rx="8"/>'
            '<rect class="box" x="150" y="310" width="56" height="48" rx="6"/>'
            '<text x="125" y="280" text-anchor="middle">module</text></g>'
            '<g data-stage="2"><rect class="acc" x="120" y="86" width="40" height="28" rx="4"/><rect class="acc" x="120" y="136" width="40" height="28" rx="4"/>'
            '<text class="t-acc" x="70" y="140" text-anchor="middle">5V</text></g>'
            '<g data-stage="3"><path class="wire-fat" d="M80 370 V540"/>'
            '<circle class="acc pw-on" cx="90" cy="230" r="16"/><text class="t-acc" x="100" y="530">9V in</text></g>'
            '<g data-stage="4"><circle class="card" cx="90" cy="230" r="16"/><text class="t-acc" x="396" y="300">off while you wire</text></g>')
    return svg('pw', 'A breadboard power module clipped onto the end of the board, feeding the plus and minus rails. Its jumpers are set to 5V, the 9V adapter plugs into its jack, and its light comes on. Then it is switched off again while you wire.', body)

# UNO drawn with its real pin rows (2026-10-07): the long digital row along the top edge
# (SCL SDA AREF GND 13 12 ~11 ~10 ~9 8 | 7 ~6 ~5 4 ~3 2 1 0) and the short power row along the
# bottom (IOREF RESET 3.3V 5V GND GND Vin), USB on the left.
UNO_TOP = ['SCL', 'SDA', 'AREF', 'GND', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
UNO_PWR = ['IOREF', 'RESET', '3.3V', '5V', 'GND', 'GND', 'Vin']


def uno_top_x(name, nth=0):
    i = [k for k, n in enumerate(UNO_TOP) if n == name][nth]
    return 40 + i * 19 + (12 if i >= 10 else 0)


def uno_pwr_x(name, nth=0):
    i = [k for k, n in enumerate(UNO_PWR) if n == name][nth]
    return 130 + i * 19


def uno_board(marks_top=(), marks_pwr=()):
    """marks: (pin name, nth, label, label dx) to draw orange with a label."""
    o = ('<rect class="box" x="10" y="150" width="400" height="290" rx="16"/><rect class="ink" x="0" y="190" width="56" height="60" rx="4"/>'
         '<rect class="box" x="30" y="158" width="366" height="26" rx="3"/><rect class="box" x="120" y="406" width="146" height="26" rx="3"/>'
         '<text x="210" y="320" text-anchor="middle">UNO</text>')
    o += ''.join(f'<rect class="ink" x="{uno_top_x(n, list(UNO_TOP[:k]).count(n))}" y="165" width="10" height="12" rx="1"/>' for k, n in enumerate(UNO_TOP))
    o += ''.join(f'<rect class="ink" x="{uno_pwr_x(n, list(UNO_PWR[:k]).count(n))}" y="413" width="10" height="12" rx="1"/>' for k, n in enumerate(UNO_PWR))
    for n, nth, lab, dx in marks_top:
        x = uno_top_x(n, nth)
        o += f'<rect class="acc" x="{x - 3}" y="162" width="16" height="18" rx="2"/><text class="t-acc" x="{x + 5 + dx}" y="140" text-anchor="middle">{lab}</text>'
    for n, nth, lab, dx in marks_pwr:
        x = uno_pwr_x(n, nth)
        o += f'<rect class="acc" x="{x - 3}" y="410" width="16" height="18" rx="2"/><text class="t-acc" x="{x + 5 + dx}" y="476" text-anchor="middle">{lab}</text>'
    return o


def servo_steps(k):
    """k: 1 jumpers in the plug, 2 brown to GND, 3 red to 5V, 4 orange to ~9. Pins on their real rows."""
    marks_pwr, marks_top = [], []
    if k >= 2: marks_pwr.append(('GND', 0, 'GND', 42))
    if k >= 3: marks_pwr.append(('5V', 0, '5V', -34))
    if k >= 4: marks_top.append(('9', 0, '~9', -30))
    o = uno_board(marks_top, marks_pwr)
    o += ('<rect class="box" x="580" y="250" width="170" height="120" rx="12"/><text x="665" y="345" text-anchor="middle">servo</text>'
          '<line class="wire-fat" x1="625" y1="250" x2="625" y2="175"/><circle class="ink" cx="625" cy="250" r="16"/>'
          '<rect class="box" x="500" y="265" width="36" height="90" rx="6"/>'
          '<line class="line" x1="536" y1="285" x2="580" y2="285"/><line class="line" x1="536" y1="310" x2="580" y2="310"/><line class="line" x1="536" y1="335" x2="580" y2="335"/>')
    gnd, v5, p9 = uno_pwr_x('GND') + 5, uno_pwr_x('5V') + 5, uno_top_x('9') + 5
    # Plug order top to bottom: brown, red, orange (the real order). Power wires nest without crossing;
    # orange runs under the servo and up the right edge to pin 9.
    ys = {2: 285, 3: 310, 4: 335}
    routes = {2: f'M500 285 H445 V495 H{gnd} V428', 3: f'M500 310 H470 V520 H{v5} V428',
              4: f'M500 335 H488 V548 H756 V100 H{p9} V162'}
    for w in (2, 3, 4):
        if k == 1:
            o += f'<path class="wire-acc" d="M500 {ys[w]} H452"/>'
        elif k >= w:
            o += f'<path class="{"wire-acc" if k == w else "wire"}" d="{routes[w]}"/>'
    if k == 1:
        o += ('<text class="t-acc" x="440" y="48">top: brown</text><text class="t-acc" x="440" y="86">middle: red</text>'
              '<text class="t-acc" x="440" y="124">bottom: orange</text>')
    return svg('ss', 'The UNO drawn from above with its long row of digital pins along the top and its short row of power pins along the bottom, and a servo on the right with three jumpers in its plug. ' +
               {1: 'The three jumpers go into the plug: brown, red, orange.', 2: 'Brown runs to the first GND pin in the power row.',
                3: 'Brown to GND, and now red to 5V, right next to it.', 4: 'Brown to GND, red to 5V, and now orange to pin 9 in the digital row.'}[k], o)


def button_uno_steps(k):
    """k: 1 button across the gap, 2 corner a21 to pin 2, 3 corner j23 to the GND next to pin 13."""
    marks = []
    if k >= 2: marks.append(('2', 0, '2', -22))
    if k >= 3: marks.append(('GND', 0, 'GND', -48))
    o = uno_board(marks_top=marks)
    o += ('<rect class="ph" x="470" y="300" width="280" height="22" rx="6"/>'
          '<text x="548" y="196">a21</text><text x="700" y="436" text-anchor="middle">j23</text>')
    o += tact(550, 236, 130, hot=(k >= 2))
    if k == 1:
        o += '<rect class="line acc-stroke" x="516" y="206" width="198" height="190" rx="14"/>'
    p2, gnd = uno_top_x('2') + 5, uno_top_x('GND') + 5
    if k >= 2:
        o += f'<path class="{"wire-acc" if k == 2 else "wire"}" d="M530 256 H500 V100 H{p2} V162"/>'
    if k >= 3:
        o += f'<path class="wire-acc" d="M700 346 H740 V80 H{gnd} V162"/>'
    return svg('bu', 'The UNO from above, long row of digital pins along the top, and a push button across the middle gap of the breadboard. ' +
               {1: 'Just the button for now, legs over holes e21, e23, f21, f23.', 2: 'A jumper runs from its corner at a21 to pin 2 in the digital row.',
                3: 'Pin 2 to the corner at a21, and the opposite corner at j23 to the GND pin next to pin 13.'}[k], o)



# ---- slide builders ----

def path_keyframes(name, pts):
    """Keyframes that walk a translate() along a polyline at constant speed."""
    segs = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    total, acc, out = sum(segs), 0, []
    for i, p in enumerate(pts):
        out.append(f'{acc / total * 100:.2f}% {{ transform: translate({p[0]}px, {p[1]}px); }}')
        if i < len(segs):
            acc += segs[i]
    return f'@keyframes {name} {{ ' + ' '.join(out) + ' }'


def notes(*ps, bridge=None):
    body = ''.join(f'<p>{p}</p>' for p in ps)
    if bridge:
        body += f'<p class="bridge">{bridge}</p>'
    return f'<aside class="notes">{body}</aside>'


def split_beats(label, eyebrow, h2, beats, viz, ground=None, section=None, note='', auto=None):
    g = f' data-ground="{ground}"' if ground else ''
    g += f' data-auto="{auto}"' if auto else ''
    sec = f' data-section="{section}"' if section else ''
    lis = ''.join(f'<li data-beat>{t}<span class="detail">{d}</span></li>' if d else f'<li data-beat>{t}</li>' for t, d in beats)
    return (f'<section class="slide" data-kind="beats" data-layout="split"{sec}{g} aria-label="{label}">\n'
            f'  <div class="split__head"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>\n'
            f'  <ol class="beats split__main">{lis}</ol>\n  {viz}\n  {note}\n</section>\n')


def split_clock(label, eyebrow, h2, sub, secs, viz, ground='tint', note='', hint='Talk with your neighbors. T to start.'):
    mm = f'{secs // 60}:{secs % 60:02d}'
    return (f'<section class="slide" data-kind="clock" data-layout="split" data-ground="{ground}" data-timer="{secs}" data-room aria-label="{label}">\n'
            f'  <div class="split__head"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>\n'
            f'  <div class="split__main"><p class="sub">{sub}</p><div class="clock"><p class="clock__digits">{mm}</p><span class="clock__track"><span class="clock__fill"></span></span><p class="clock__hint">{hint}</p></div></div>\n'
            f'  {viz}\n  {note}\n</section>\n')


def do_slide(label, eyebrow, h2, steps, secs, viz, ground='tint', note='', section=None):
    """A work slide: numbered steps and a timer on the left, the picture to copy on the right. It stays up while tables build."""
    sec = f' data-section="{section}"' if section else ''
    mm = f'{secs // 60}:{secs % 60:02d}'
    lis = ''.join(f'<li><span>{t}</span></li>' for t in steps)
    return (f'<section class="slide" data-kind="clock" data-layout="split" data-do{sec} data-ground="{ground}" data-timer="{secs}" data-room aria-label="{label}">\n'
            f'  <div class="split__head"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>\n'
            f'  <div class="split__main"><ol class="steps">{lis}</ol><div class="clock"><p class="clock__digits">{mm}</p><span class="clock__track"><span class="clock__fill"></span></span><p class="clock__hint">T to start</p></div></div>\n'
            f'  {viz}\n  {note}\n</section>\n')


def code(label, h2, src, note, ground=None, section=None):
    g = f' data-ground="{ground}"' if ground else ''
    sec = f' data-section="{section}"' if section else ''
    src = src.strip('\n')
    assert len(src.split('\n')) <= 10, label
    esc = src.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    def line(l):
        code_part, sep, comment = l.partition('//')
        code_part = re.sub(r'\b(void|const|int|bool|if|else|for|while|true|return)\b', r'<span class="k">\1</span>', code_part)
        return code_part + (f'<span class="c">//{comment}</span>' if sep else '')
    esc = '\n'.join(line(l) for l in esc.split('\n'))
    return (f'<section class="slide" data-kind="code"{sec}{g} aria-label="{label}">\n  <h2>{h2}</h2>\n'
            f'<pre class="code">{esc}</pre>\n  {note}\n</section>\n')


STEP_GROUNDS = [None, 'warm', 'tint']


def steps(round_name, items, section=None):
    """One slide per step: what to do (exact holes), what you should see (fills in on its own), and the picture so far."""
    out, n = [], len(items)
    for k, (h2, do, see, detail, viz, note) in enumerate(items, 1):
        g = STEP_GROUNDS[(k - 1) % 3]
        gattr = f' data-ground="{g}"' if g else ''
        sec = f' data-section="{section}"' if section and k == 1 else ''
        out.append(f'<section class="slide" data-kind="beats" data-layout="split" data-step data-auto="1.2" data-room{sec}{gattr} aria-label="{round_name}, step {k}">\n'
                   f'  <div class="split__head"><p class="eyebrow">{round_name} · step {k} of {n}</p><h2>{h2}</h2></div>\n'
                   f'  <div class="split__main"><p class="sub">{do}</p><ol class="beats"><li data-beat>{see}<span class="detail">{detail}</span></li></ol></div>\n'
                   f'  {viz}\n  {note}\n</section>\n')
    return out


def check(label, h2, items, note, ground=None, section=None):
    g = f' data-ground="{ground}"' if ground else ''
    sec = f' data-section="{section}"' if section else ''
    lis = ''.join(f'<li data-beat>{t}<span class="detail">{d}</span></li>' for t, d in items)
    return (f'<section class="slide" data-kind="beats"{sec}{g} aria-label="{label}">\n  <p class="eyebrow">Check in</p>\n  <h2>{h2}</h2>\n'
            f'  <ol class="beats">{lis}</ol>\n  {note}\n</section>\n')


# ---- styles: put lab_css() inside the deck's <style> ----

LAB_CSS = r'''
.viz .wire { stroke: currentColor; stroke-width: 5; fill: none; stroke-linejoin: round; stroke-linecap: round; }
.viz .wire-acc { stroke: var(--acm-primary); stroke-width: 6; fill: none; stroke-linecap: round; }
.viz .wire-fat { stroke: currentColor; stroke-width: 14; fill: none; stroke-linecap: round; }
.viz .hole { fill: currentColor; opacity: 0.35; }
.viz .big { font-size: 72px; font-weight: 700; }
.viz .soft { opacity: 0.45; }
.viz .pin1 { fill: var(--acm-surface); }
.viz .lled { fill: var(--acm-primary); }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.2; } }
.is-presenting .slide.is-current .viz--bb .bb-pulse { animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { stroke-opacity: 1; } 50% { stroke-opacity: 0.35; } }
.is-presenting .slide.is-current .viz--pm .pm-spike { animation: blink 1.2s step-end infinite; }
.is-presenting .slide.is-current .viz--lp .lp-e { animation: lp-e 3.6s linear infinite; animation-delay: calc(var(--n) * -0.6s); }
LP_KEYFRAMES
.is-presenting .slide.is-current .viz :is(.lr-e, .bl-e) { animation: lr-e 3.6s linear infinite; animation-delay: calc(var(--n) * -0.6s); }
LR_KEYFRAMES
.viz--bt .bt-open { opacity: 0; }
.is-presenting .slide.is-current .viz--bt .bt-open { animation: bt-open 3s step-end infinite; }
.is-presenting .slide.is-current .viz--bt .bt-on { animation: bt-on 3s step-end infinite; }
@keyframes bt-open { 0% { opacity: 1; } 50% { opacity: 0; } }
@keyframes bt-on { 0% { opacity: 0; } 50% { opacity: 1; } }
.is-presenting .slide.is-current .viz--mr :is(.mr-cw, .mr-ccw) { transform-box: view-box; transform-origin: 380px 280px; animation: spin 0.6s linear infinite; }
.is-presenting .slide.is-current .viz--mr .mr-ccw { animation-direction: reverse; }
.is-presenting .slide.is-current .viz--dr :is(.dr-cw, .dr-ccw) { transform-box: fill-box; transform-origin: center; animation: spin 0.8s linear infinite; }
.is-presenting .slide.is-current .viz--dr .dr-ccw { animation-direction: reverse; }
.is-presenting .slide.is-current .viz--bp .bp-down { animation: bp-down 3s step-end infinite; }
.is-presenting .slide.is-current .viz--bp .bp-up { animation: bp-up 3s step-end infinite; }
@keyframes bp-down { 0% { opacity: 0.15; } 50% { opacity: 1; } }
@keyframes bp-up { 0% { opacity: 1; } 50% { opacity: 0.15; } }
.is-presenting .slide.is-current .viz--sv .sv-swing { transform-box: view-box; transform-origin: 540px 250px; animation: sv-swing 3s var(--acm-ease-standard) infinite; }
@keyframes sv-swing { 0%, 100% { transform: rotate(-70deg); } 50% { transform: rotate(70deg); } }
.is-presenting .slide.is-current .viz--an .an-sweep { transform-box: view-box; transform-origin: 380px 440px; animation: sv-swing 3.6s linear infinite; }
.steps { list-style: none; margin: 0; padding: 0; display: grid; gap: calc(14 * var(--u)); counter-reset: step; }
.steps li { counter-increment: step; display: grid; grid-template-columns: calc(72 * var(--u)) 1fr; column-gap: calc(20 * var(--u)); font-size: calc(40 * var(--u)); line-height: 1.2; }
.steps li::before { content: counter(step, decimal-leading-zero); font-family: var(--acm-font-code); font-weight: 600; color: var(--acm-primary); }
.steps code { font-family: var(--acm-font-code); }
.slide[data-ground="orange"] .steps li::before { color: currentColor; }
.slide[data-do] .clock__digits { font-size: calc(64 * var(--u)); }
.slide[data-do] .clock { display: grid; grid-template-columns: auto 1fr; align-items: baseline; column-gap: calc(28 * var(--u)); row-gap: calc(10 * var(--u)); }
.slide[data-do] .clock__digits { grid-column: 1; grid-row: 1; }
.slide[data-do] .clock__hint { grid-column: 2; grid-row: 1; margin: 0; }
.slide[data-do] .clock__track { grid-column: 1 / -1; grid-row: 2; }
.slide[data-do] .split__main { gap: calc(28 * var(--u)); }
'''


def lab_css():
    """CSS the pictures and lab slides need, with the current-flow keyframes filled in."""
    return (LAB_CSS.replace('LP_KEYFRAMES', path_keyframes('lp-e', LOOP))
                   .replace('LR_KEYFRAMES', path_keyframes('lr-e', LED_RAILS)))
