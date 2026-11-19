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
    s3 = ('<g data-stage="3"><path class="wire" d="M500 366 V440 H184"/><circle class="acc" cx="500" cy="366" r="12"/><circle class="acc" cx="310" cy="256" r="12"/></g>')
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


def snippet_hl(name, label, lines, hl=(), note=None, dim=()):
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
        cls = ' class="t-acc"' if k in hl else (' class="soft"' if t.startswith('//') or k in dim else '')
        out += f'<text{cls} x="{32 + ind * 19.2:.0f}" y="{y}">{t}</text>'
    out += '</g>'
    if note:
        out += f'<text class="t-acc" x="32" y="530">{note}</text>'
    return svg('sn', label, out)


def _kit_icons():
    """The part drawings parts_kit() and parts_grid() share, each in a 253 x 140 cell."""
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
    return dict(breadboard=breadboard, module=module, battery=battery, adapter=adapter, uno=uno, usb=usb,
                jumper=jumper, led=led, resistor=resistor, button=button, fanmotor=fanmotor, servo=servo)


def parts_kit():
    return parts_grid([('breadboard', 'breadboard'), ('module', 'power module'), ('battery', '9V battery'),
                       ('uno', 'UNO R3 board'), ('usb', 'USB cable'), ('adapter', '9V adapter'),
                       ('jumper', 'jumper wire'), ('led', 'red LED'), ('resistor', 'resistor'),
                       ('button', 'button'), ('fanmotor', 'fan + motor'), ('servo', 'servo')],
                      'Every part for today, drawn and named: breadboard, power module, 9V battery with its barrel plug, UNO R3 board, USB cable, 9V wall adapter, jumper wire, red LED, resistor, push button, fan blade on a motor, and a servo with its arm.')


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


def uno(pins=((9, 'servo'), (2, 'button')), names=True):
    """pins: (pin number, what it drives), marked in orange from beat 3. names=False marks the pins without
    naming the parts, for when the beat beside the picture already names them."""
    b = ('<rect class="box" x="60" y="40" width="660" height="470" rx="24"/>'
         '<rect class="box" x="20" y="90" width="130" height="120" rx="6"/>'   # USB-B
         '<rect class="ink" x="20" y="380" width="120" height="90" rx="10"/>'  # barrel jack
         '<circle class="box" cx="190" cy="80" r="18"/>'                       # reset
         '<rect class="chip" x="330" y="300" width="330" height="70" rx="8"/>')
    holes = ''
    for i in range(14):
        holes += f'<rect class="ink" x="{246 + i*32}" y="64" width="16" height="16" rx="2"/>'
    head = f'<rect class="box" x="236" y="54" width="456" height="36" rx="4"/>{holes}'
    nums = '<text x="254" y="36" text-anchor="middle">13</text><text x="670" y="36" text-anchor="middle">0</text>'
    led = ('<rect class="lled" x="238" y="160" width="30" height="18" rx="4"/><text x="284" y="182">L</text>'
           '<rect class="ph" x="238" y="200" width="30" height="18" rx="4"/><text x="284" y="222">TX</text>'
           '<rect class="ph" x="238" y="236" width="30" height="18" rx="4"/><text x="284" y="258">RX</text>'
           '<rect class="ph" x="600" y="200" width="30" height="18" rx="4"/><text x="646" y="222">ON</text>')
    pw = '<rect class="box" x="240" y="452" width="230" height="36" rx="4"/><rect class="box" x="500" y="452" width="190" height="36" rx="4"/>'
    pwh = ''.join(f'<rect class="ink" x="{252 + i*28}" y="462" width="14" height="14" rx="2"/>' for i in range(8))
    pwh += ''.join(f'<rect class="ink" x="{514 + i*28}" y="462" width="14" height="14" rx="2"/>' for i in range(6))
    lab = '<text x="355" y="438" text-anchor="middle">5V GND</text>'
    s1 = '<g data-stage="1"><rect class="line acc-stroke" x="10" y="80" width="150" height="140" rx="10"/><text class="t-acc" x="85" y="162" text-anchor="middle">USB</text></g>'
    s2 = '<g data-stage="2"><rect class="line acc-stroke" x="228" y="46" width="472" height="52" rx="8"/></g>'
    s3 = ('<g data-stage="3">'
          + ''.join(f'<rect class="acc" x="{254 + (13 - p) * 32 - 8}" y="64" width="16" height="16" rx="2"/>'
                    f'<text class="t-acc" x="{254 + (13 - p) * 32}" y="36" text-anchor="middle">{p}</text>'
                    + (f'<text class="t-acc" x="{254 + (13 - p) * 32}" y="132" text-anchor="middle">{what}</text>' if names else '') for p, what in pins)
          + '</g>')
    s4 = '<g data-stage="4"><rect class="line acc-stroke" x="300" y="444" width="110" height="52" rx="8"/></g>'
    body = b + head + nums + led + pw + pwh + lab + s1 + s2 + s3 + s4
    marked = ', '.join(f'pin {p} for the {what}' for p, what in pins)
    return svg('uno', f'A drawing of the UNO board from above: the USB port on the left, the row of digital pins 13 to 0 along the top with {marked} marked, the small L light by pin 13, the main chip, and the 5V and GND pins along the bottom.', body)


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
UNO_PWR = ['', 'IOREF', 'RESET', '3.3V', '5V', 'GND', 'GND', 'Vin']   # the first hole is unlabeled on the board


def uno_top_x(name, nth=0):
    i = [k for k, n in enumerate(UNO_TOP) if n == name][nth]
    return 40 + i * 19 + (12 if i >= 10 else 0)


def uno_pwr_x(name, nth=0):
    i = [k for k, n in enumerate(UNO_PWR) if n == name][nth]
    return 130 + i * 19


def uno_board(marks_top=(), marks_pwr=()):
    """marks: (pin name, nth, label, label dx) to draw orange with a label."""
    o = ('<rect class="box" x="10" y="150" width="400" height="290" rx="16"/><rect class="ink" x="0" y="190" width="56" height="60" rx="4"/>'
         '<rect class="box" x="30" y="158" width="366" height="26" rx="3"/><rect class="box" x="120" y="406" width="162" height="26" rx="3"/>'
         '<rect class="box" x="292" y="406" width="114" height="26" rx="3"/>' + ''.join(f'<rect class="ink" x="{302 + i * 17}" y="413" width="10" height="12" rx="1"/>' for i in range(6)) +
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


def servo_steps(k, gate=False):
    """k: 1 jumpers in the plug, 2 brown to GND, 3 red to 5V, 4 orange to ~9. Pins on their real rows.
    gate=True (2026-10-29): brown goes to the second GND and red goes to the breadboard's + rail (drawn with
    board(), so here red just leaves toward the breadboard); the first GND and 5V already feed the rails."""
    marks_pwr, marks_top = [], []
    if k >= 2: marks_pwr.append(('GND', 1 if gate else 0, 'GND', 42))
    if k >= 3 and not gate: marks_pwr.append(('5V', 0, '5V', -34))
    if k >= 4: marks_top.append(('9', 0, '~9', -30))
    o = uno_board(marks_top, marks_pwr)
    o += ('<rect class="box" x="580" y="250" width="170" height="120" rx="12"/><text x="665" y="345" text-anchor="middle">servo</text>'
          '<line class="wire-fat" x1="625" y1="250" x2="625" y2="175"/><circle class="ink" cx="625" cy="250" r="16"/>'
          '<rect class="box" x="500" y="265" width="36" height="90" rx="6"/>'
          '<line class="line" x1="536" y1="285" x2="580" y2="285"/><line class="line" x1="536" y1="310" x2="580" y2="310"/><line class="line" x1="536" y1="335" x2="580" y2="335"/>')
    gnd, v5, p9 = uno_pwr_x('GND', 1 if gate else 0) + 5, uno_pwr_x('5V') + 5, uno_top_x('9') + 5
    # Plug order top to bottom: brown, red, orange (the real order). Power wires nest without crossing;
    # orange runs under the servo and up the right edge to pin 9.
    ys = {2: 285, 3: 310, 4: 335}
    routes = {2: f'M500 285 H445 V495 H{gnd} V428', 3: 'M500 310 H470 V548 H300' if gate else f'M500 310 H470 V520 H{v5} V428',
              4: f'M500 335 H488 V548 H756 V100 H{p9} V162'}
    for w in (2, 3, 4):
        if k == 1:
            o += f'<path class="wire-acc" d="M500 {ys[w]} H452"/>'
        elif k >= w:
            o += f'<path class="{"wire-acc" if k == w else "wire"}" d="{routes[w]}"/>'
    # Name the servo's own wire this step uses, in ink: the newest jumper is drawn orange, which would
    # otherwise read as "the orange wire" on the brown and red steps.
    if k in (2, 3, 4):
        o += f'<text x="750" y="410" text-anchor="end">{("brown", "red", "orange")[k - 2]} wire</text>'
    if gate and k >= 3:
        o += '<text x="290" y="556" text-anchor="end">to + rail</text>'
    if gate:
        return svg('ss', 'The UNO drawn from above with its long row of digital pins along the top and its short row of power pins along the bottom, and a servo on the right with three jumpers in its plug. ' +
                   {1: 'The three jumpers go into the plug: brown, red, orange.', 2: 'Brown runs to the second GND pin in the power row.',
                    3: 'Brown to the second GND, and red runs off to the breadboard.', 4: 'Brown to the second GND, red to the breadboard, and now orange to pin 9 in the digital row.'}[k], o)
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




# ---- 2026-10-15: the fan switch (transistor), uploading, and timing ----
# A zoomed breadboard (rows 9 to 14, hole by hole) for parts that need room: the transistor's
# three legs, the resistor across the gap, the diode, and the motor. Same naming as bb().

def ZX(r):
    return 176 + (r - 9) * 76


ZY = {'+t': 62, '-t': 94, 'a': 136, 'b': 172, 'c': 208, 'd': 244, 'e': 280,
      'f': 328, 'g': 364, 'h': 400, 'i': 436, 'j': 472, '-b': 508, '+b': 540}

FAN_AT = (680, 196)   # the motor and blade, held to the right of the board


def _zoom_grid(cols, x):
    """A zoomed stretch of breadboard, hole by hole: the card, the middle gap, the row numbers along the top,
    and the line letters and rails down the left. cols: the row numbers drawn; x(r): where row r sits."""
    w = (len(cols) - 1) * 76 + 60
    o = f'<rect class="card" x="146" y="44" width="{w}" height="512" rx="10"/><rect class="ph" x="152" y="294" width="{w - 12}" height="20" rx="4"/>'
    for k in ZY:
        o += ''.join(f'<circle class="hole" cx="{x(r)}" cy="{ZY[k]}" r="6"/>' for r in cols)
    o += ''.join(f'<text x="{x(r)}" y="30" text-anchor="middle">{r}</text>' for r in cols)
    for k, t in (('+t', '+'), ('-t', '-'), ('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'),
                 ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('-b', '-'), ('+b', '+')):
        o += f'<text x="116" y="{ZY[k] + 11}" text-anchor="middle">{t}</text>'
    return o


def bbz(parts, hi=(), on=False):
    """Rows 9 to 14, zoomed. parts: transistor (legs c10, c11, c12, flat side facing you), emit_gnd (a10 to the
    top - rail), base_res (resistor e11 to f11, across the gap), diode (b12 to the top + rail at row 11, stripe at the rail),
    motor (wires a12 and the top + rail), test_jump (j11 to the bottom + rail). on: the module is on, so the fan spins."""
    acc = lambda n: n in hi
    o = _zoom_grid(range(9, 15), ZX)
    def wire(d, n):
        return f'<path class="{"wire-acc" if acc(n) else "wire"}" d="{d}"/>'
    def dot(r, k, n):
        return f'<circle class="{"acc" if acc(n) else "ink"}" cx="{ZX(r)}" cy="{ZY[k]}" r="9"/>'
    if 'emit_gnd' in parts:
        o += wire(f'M{ZX(10)} {ZY["a"]} Q{ZX(10) - 38} {ZY["-t"] + 8} {ZX(9)} {ZY["-t"]}', 'emit_gnd') + dot(10, 'a', 'emit_gnd') + dot(9, '-t', 'emit_gnd')
    if 'transistor' in parts:
        x0, x1, yb = ZX(10) - 24, ZX(12) + 24, ZY['c'] + 22
        cls = 'line acc-stroke' if acc('transistor') else 'line'
        o += (f'<path class="ph" d="M{x0} {yb} V{yb - 12} A{(x1 - x0) / 2} 30 0 0 1 {x1} {yb - 12} V{yb} Z"/>'
              f'<path class="{cls}" d="M{x0} {yb} V{yb - 12} A{(x1 - x0) / 2} 30 0 0 1 {x1} {yb - 12} V{yb} Z"/>'
              f'<line class="{"wire-acc" if acc("transistor") else "wire"}" x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}"/>'
              + ''.join(dot(r, 'c', 'transistor') for r in (10, 11, 12)))
        if acc('transistor'):
            o += f'<text class="t-acc" x="{ZX(11)}" y="314" text-anchor="middle">flat side faces you</text>'
    if 'base_res' in parts:
        x = ZX(11)
        st = ' acc-stroke' if acc('base_res') else ''
        o += (f'<line class="line{st}" x1="{x}" y1="{ZY["e"]}" x2="{x}" y2="{ZY["f"]}"/>'
              f'<rect class="box" x="{x - 13}" y="289" width="26" height="30" rx="10"/>'
              + ''.join(f'<rect class="ink" x="{x - 12}" y="{y}" width="24" height="4"/>' for y in (295, 302, 309))
              + dot(11, 'e', 'base_res') + dot(11, 'f', 'base_res'))
    if 'diode' in parts:
        (xa, ya), (xb, yb) = (ZX(12), ZY['b']), (ZX(11), ZY['+t'])
        p = lambda t: (xa + (xb - xa) * t, ya + (yb - ya) * t)
        (b0x, b0y), (b1x, b1y), (s0x, s0y) = p(0.3), p(0.72), p(0.6)
        st = ' acc-stroke' if acc('diode') else ''
        o += (f'<line class="line{st}" x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}"/>'
              f'<line class="dbody" x1="{b0x:.0f}" y1="{b0y:.0f}" x2="{b1x:.0f}" y2="{b1y:.0f}"/>'
              f'<line class="dstripe" x1="{s0x:.0f}" y1="{s0y:.0f}" x2="{b1x:.0f}" y2="{b1y:.0f}"/>'
              + dot(12, 'b', 'diode') + dot(11, '+t', 'diode'))
        if acc('diode'):
            o += '<text class="t-acc" x="672" y="150" text-anchor="middle">stripe</text><text class="t-acc" x="672" y="190" text-anchor="middle">toward +</text>'
    if 'motor' in parts:
        cx, cy = FAN_AT
        o += (wire(f'M{ZX(12)} {ZY["a"]} C{ZX(12) + 80} {ZY["a"]} {cx - 90} {cy} {cx - 26} {cy}', 'motor')
              + wire(f'M{cx} {cy - 26} C{cx} {cy - 90} {ZX(14) + 50} {ZY["+t"]} {ZX(14)} {ZY["+t"]}', 'motor')
              + fan(cx, cy, 'acc' if (acc('motor') or on) else 'ink', 'bz-spin' if on else '', 0.62)
              + f'<circle class="box" cx="{cx}" cy="{cy}" r="26"/>'
              + dot(12, 'a', 'motor') + dot(14, '+t', 'motor'))
    if 'test_jump' in parts:
        o += wire(f'M{ZX(11)} {ZY["j"]} Q{ZX(11) - 30} {ZY["+b"] - 12} {ZX(10)} {ZY["+b"]}', 'test_jump') + dot(11, 'j', 'test_jump') + dot(10, '+b', 'test_jump')
    if on:
        o += '<text class="t-acc" x="680" y="330" text-anchor="middle">spins</text>'
    return svg('bz', 'A close-up of the breadboard, rows 9 to 14 drawn hole by hole, letters a to j down the side and the rails marked plus and minus. ' + ', '.join(parts) + ' placed; the newest part is drawn in orange.', o)


def fan_uno_steps(k):
    """k: 1 the jumper from j11 to pin ~5, 2 also the top - rail to the free GND in the power row, 3 both, to check before power."""
    marks_top = [('5', 0, '~5', -30)]
    marks_pwr = [('GND', 1, 'GND', 44)] if k >= 2 else []
    o = uno_board(marks_top, marks_pwr)
    o += ('<rect class="card" x="460" y="190" width="290" height="270" rx="10"/>'
          '<line class="line soft" x1="480" y1="222" x2="730" y2="222"/><text x="605" y="262" text-anchor="middle">- rail</text>'
          '<path class="ph" d="M540 330 V318 A60 26 0 0 1 660 318 V330 Z"/><path class="line" d="M540 330 V318 A60 26 0 0 1 660 318 V330 Z"/>'
          '<rect class="ph" x="470" y="350" width="270" height="16" rx="4"/><line class="line" x1="600" y1="330" x2="600" y2="420"/>'
          '<rect class="box" x="588" y="342" width="24" height="30" rx="9"/>'
          '<text x="660" y="432">j11</text>')
    p5, g2 = uno_top_x('5') + 5, uno_pwr_x('GND', 1) + 5
    o += f'<path class="{"wire-acc" if k in (1, 3) else "wire"}" d="M600 420 H440 V100 H{p5} V162"/><circle class="{"acc" if k in (1, 3) else "ink"}" cx="600" cy="420" r="9"/>'
    if k >= 2:
        o += f'<path class="wire-acc" d="M710 222 H752 V540 H{g2} V428"/><circle class="acc" cx="710" cy="222" r="9"/>'
    return svg('fu', 'The UNO from above, and a close-up of the breadboard with the transistor and the resistor across the gap. ' +
               {1: 'A jumper runs from hole j11, below the resistor, to pin 5 in the digital row.',
                2: 'Hole j11 to pin 5, and now a jumper from the top minus rail to the free GND pin in the short row of power pins.',
                3: 'Both board wires highlighted to check: hole j11 to pin 5, and the top minus rail to the free GND pin in the short row of power pins.'}[k], o)


# ---- 2026-10-14: the breadboard drawn true to the object ----
# One view of the 830-hole board for every step of a lab, so parts accumulate on the same picture.
# The real board, which these drawings must match (see docs/03-playbooks/arduino-lab/breadboard-drawing.md):
#   - holes sit on one 0.1 inch grid, the same pitch across and down, so the drawing never stretches one axis;
#   - each numbered row is two strips of 5 joined holes, a to e and f to j, split by the middle channel;
#   - the channel and the four rails all run the long way; rails sit along the long edges, apart from lines a and j,
#     each marked by a printed red (+) or blue (-) line, with their holes in groups of 5;
#   - held so its printing reads upright (the club's Elegoo boards, checked against Elegoo's product photo and
#     manual p.193): line a is at the far edge, the rows count up from 1 at the RIGHT end, and both edges print
#     red above blue, so the far pair is + outside, - inside, and the near pair is + inside, - outside;
#   - the power module plugs into the row-1 end (the right), its + pins on the red lines.

BD_P = 24                                     # one hole pitch, across and down alike
BD_COLS = range(1, 24)                        # rows 1 to 23, counted leftward from the module
BD_ROWS = {'+t': 0, '-t': 1, 'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7,
           'f': 10, 'g': 11, 'h': 12, 'i': 13, 'j': 14, '+b': 16, '-b': 17}
BD_FAN = (586, 196)                           # the motor and blade, held up in the air near rows 3 to 6


def bdx(c):
    return 670 - (c - 1) * BD_P


def bdy(k):
    return 76 + BD_ROWS[k] * BD_P


def _bd_rail_hole(c):
    return (c - 1) % 6 < 5                    # rail holes in groups of 5, one gap between groups


def _bd_strip(c, k):
    """The joined set a hole belongs to: a whole rail, or one 5-hole strip."""
    if k in ('+t', '-t', '+b', '-b'):
        return ('rail', k)
    return ('strip', c, 'top' if k in 'abcde' else 'bottom')


# Each part: the holes it uses, and how to draw it (newest part in orange).
def _bd_parts(on, spin, lit=()):
    X, Y = bdx, bdy
    def dot(c, k, hot):
        return f'<circle class="{"acc" if hot else "ink"}" cx="{X(c)}" cy="{Y(k)}" r="6"/>'
    def wire(d, hot):
        return f'<path class="{"wire-acc" if hot else "wire"}" d="{d}"/>'
    def halo(x, y, t, hot, anchor='start'):
        return f'<text class="halo{" t-acc" if hot else ""}" x="{x}" y="{y}" text-anchor="{anchor}">{t}</text>'
    def off(c, k, dx, up, label, hot, anchor, tag=True):
        """A jumper from a hole to the UNO: it leaves the board between holes and ends at the pin's name.
        tag=False drops the name (gate parts name a wire only on the step that adds it)."""
        x0, y0, x1 = X(c), Y(k), X(c) + dx
        ye = 22 if up else 530
        bend = y0 - 20 if up else y0 + 20
        tip = (f'M{x1 - 9} {ye + 9} l9 -9 l9 9' if up else f'M{x1 - 9} {ye - 9} l9 9 l9 -9')
        ty = 44 if up else 552
        tx = x1 + 16 if anchor == 'start' else x1 - 16
        return (wire(f'M{x0} {y0} Q{x0} {bend} {x1} {bend} V{ye}', hot)
                + f'<path class="line{" acc-stroke" if hot else ""}" d="{tip}"/>' + dot(c, k, hot)
                + (halo(tx, ty, label, hot, anchor) if tag else ''))
    P = {}
    def module(hot):
        # Plugged into the row-1 end: its pins sit in all four rails. On the board: the two 5V / OFF / 3.3 caps,
        # the light, the flat USB socket, and at the outer corner the round jack with the push switch beside it.
        return ('<rect class="box" x="696" y="56" width="58" height="448" rx="8"/>'
                + (f'<rect class="line acc-stroke" x="690" y="50" width="70" height="460" rx="10"/>' if hot else '')
                + ''.join(f'<rect class="ink" x="680" y="{Y(k) - 5}" width="22" height="10" rx="2"/>' for k in ('+t', '-t', '+b', '-b'))
                + '<rect class="ink" x="714" y="72" width="24" height="18" rx="3"/><rect class="ink" x="714" y="470" width="24" height="18" rx="3"/>'
                + f'<circle class="{"acc" if on else "card"}" cx="726" cy="150" r="10"/>'
                + '<rect class="ph" x="708" y="214" width="40" height="70" rx="3"/>'
                + '<rect class="box" x="704" y="330" width="26" height="26" rx="4"/>'
                + '<rect class="ink" x="712" y="372" width="38" height="52" rx="5"/>')
    P['module'] = ([], module)
    P['battery'] = ([], lambda hot: (f'<rect class="{"acc" if hot else "ink"}" x="710" y="370" width="42" height="56" rx="5"/>'
                                     + f'<text class="{"t-acc" if hot else ""}" x="725" y="460" text-anchor="middle">9V</text>'))
    def button(hot):
        xs, ye, yf = (X(21), X(23)), Y('e'), Y('f')
        cx, cy = sum(xs) / 2, (ye + yf) / 2
        o = ''.join(f'<line class="line" x1="{x}" y1="{y}" x2="{cx + (x - cx) * 0.6:.0f}" y2="{cy + (y - cy) * 0.6:.0f}"/>' for x in xs for y in (ye, yf))
        o += f'<rect class="box" x="{cx - 28:.0f}" y="{cy - 28:.0f}" width="56" height="56" rx="8"/><circle class="ph" cx="{cx:.0f}" cy="{cy:.0f}" r="14"/>'
        if hot:
            o += f'<rect class="line acc-stroke" x="{cx - 34:.0f}" y="{cy - 34:.0f}" width="68" height="68" rx="11"/>'
        return o + ''.join(dot(c, k, hot) for c in (21, 23) for k in 'ef')
    P['button'] = ([(21, 'e'), (23, 'e'), (21, 'f'), (23, 'f')], button)
    P['btn_a'] = ([(21, 'a')], lambda hot: off(21, 'a', -36, True, 'pin 2', hot, 'end'))
    P['btn_j'] = ([(23, 'j')], lambda hot: off(23, 'j', 12, False, 'GND by 13', hot, 'start'))
    def transistor(hot):
        # Flat side toward you (the near edge). Seen that way the legs are E, B, C from left to right, and the
        # rows count up to the left, so E is in c12, B in c11, C in c10.
        x0, x1, yb = X(12) - 10, X(10) + 10, Y('c') + 4
        cls = 'line acc-stroke' if hot else 'line'
        d = f'M{x0} {yb} V{yb - 10} A{(x1 - x0) / 2} 26 0 0 1 {x1} {yb - 10} V{yb} Z'
        o = f'<path class="ph" d="{d}"/><path class="{cls}" d="{d}"/>' + ''.join(dot(c, 'c', hot) for c in (10, 11, 12))
        if hot:
            o += halo(X(9) + 14, Y('d') + 2, 'flat side', True) + halo(X(9) + 14, Y('e') + 6, 'faces you', True)
        return o
    P['transistor'] = ([(12, 'c'), (11, 'c'), (10, 'c')], transistor)
    P['emit_gnd'] = ([(12, 'a'), (13, '-t')], lambda hot: wire(f'M{X(12)} {Y("a")} Q{X(12)} {Y("-t") + 6} {X(13)} {Y("-t")}', hot) + dot(12, 'a', hot) + dot(13, '-t', hot))
    def base_res(hot):
        x, ym = X(11), (Y('e') + Y('f')) / 2
        st = ' acc-stroke' if hot else ''
        return (f'<line class="line{st}" x1="{x}" y1="{Y("e")}" x2="{x}" y2="{Y("f")}"/>'
                f'<rect class="box" x="{x - 9}" y="{ym - 20:.0f}" width="18" height="40" rx="8"/>'
                + ''.join(f'<rect class="ink" x="{x - 8}" y="{ym + dy:.0f}" width="16" height="4"/>' for dy in (-12, -4, 4))
                + dot(11, 'e', hot) + dot(11, 'f', hot))
    P['base_res'] = ([(11, 'e'), (11, 'f')], base_res)
    def diode(hot):
        (xa, ya), (xb, yb) = (X(10), Y('b')), (X(9), Y('+t'))
        p = lambda t: (xa + (xb - xa) * t, ya + (yb - ya) * t)
        (b0x, b0y), (b1x, b1y), (s0x, s0y) = p(0.28), p(0.7), p(0.58)
        st = ' acc-stroke' if hot else ''
        o = (f'<line class="line{st}" x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}"/>'
             f'<line class="dbody" style="stroke-width:16px" x1="{b0x:.0f}" y1="{b0y:.0f}" x2="{b1x:.0f}" y2="{b1y:.0f}"/>'
             f'<line class="dstripe" style="stroke-width:16px" x1="{s0x:.0f}" y1="{s0y:.0f}" x2="{b1x:.0f}" y2="{b1y:.0f}"/>'
             + dot(10, 'b', hot) + dot(9, '+t', hot))
        if hot:
            o += halo(X(8) + 6, Y('c') + 8, 'stripe', True) + halo(X(8) + 6, Y('d') + 12, 'at +', True)
        return o
    P['diode'] = ([(10, 'b'), (9, '+t')], diode)
    def motor(hot):
        cx, cy = BD_FAN
        return (wire(f'M{X(10)} {Y("a")} C{X(10) + 40} {Y("a")} {cx - 70} {cy} {cx - 22} {cy}', hot)
                + wire(f'M{cx} {cy - 22} C{cx} {cy - 70} {X(7) + 30} {Y("+t")} {X(7)} {Y("+t")}', hot)
                + fan(cx, cy, 'acc' if (hot or spin) else 'ink', 'bd-spin' if spin else '', 0.5)
                + f'<circle class="box" cx="{cx}" cy="{cy}" r="20"/>'
                + dot(10, 'a', hot) + dot(7, '+t', hot)
                + (halo(cx, Y('f') - 22, 'spins', True, 'middle') if spin else ''))
    P['motor'] = ([(10, 'a'), (7, '+t')], motor)
    P['test_jump'] = ([(11, 'j'), (10, '+b')], lambda hot: wire(f'M{X(11)} {Y("j")} Q{X(11)} {Y("+b") - 6} {X(10)} {Y("+b")}', hot) + dot(11, 'j', hot) + dot(10, '+b', hot))
    P['to_pin5'] = ([(11, 'j')], lambda hot: off(11, 'j', 12, False, 'pin ~5', hot, 'start'))
    P['gnd_link'] = ([(3, '-b')], lambda hot: off(3, '-b', 12, False, 'GND', hot, 'start'))

    # ---- 2026-10-29 parking gate (no power module; the UNO's 5V feeds the bottom + rail) ----
    # A gate wire is named only on the step that adds it, so a full board stays readable.
    def edge(c, k, x, label, hot):
        """The top rail fed from the UNO: the jumper runs past the row-1 end, where the module used to sit, toward the UNO."""
        tip = f'M{x - 9} 521 l9 9 l9 -9'
        return (wire(f'M{X(c)} {Y(k)} H{x} V530', hot) + f'<path class="line{" acc-stroke" if hot else ""}" d="{tip}"/>'
                + dot(c, k, hot) + (halo(756, 552, label, True, 'end') if hot else ''))
    P['g_5v'] = ([(2, '+b')], lambda hot: off(2, '+b', 12, False, '5V', hot, 'start', tag=hot))
    P['g_gnd'] = ([(4, '-b')], lambda hot: off(4, '-b', 12, False, 'GND', hot, 'start', tag=hot))
    P['g_topgnd'] = ([(1, '-t')], lambda hot: edge(1, '-t', 682, 'GND by 13', hot))
    def sensor(hot):
        # HC-SR04 standing in a20 to a23, eyes facing the far edge. Real size: board 45 x 20 mm, pins in the middle
        # of its long edge, two 16 mm eyes 26 mm apart (one pitch = 2.54 mm = 24 px). It hangs over the top rails
        # from about row 13 to row 30, so the window cuts it off on the left, as the real board goes on there too.
        mm = BD_P / 2.54
        cx, ya = (X(21) + X(22)) / 2, Y('a')
        st = ' acc-stroke' if hot else ''
        o = ''
        top = 56                                  # the board's far edge; the real eyes stick out a little past it
        for ex in (cx - 13 * mm, cx + 13 * mm):
            h = ya - 8 - top
            o += (f'<rect class="box" x="{ex - 8 * mm:.0f}" y="{top}" width="{16 * mm:.0f}" height="{h}" rx="10"/>'
                  f'<rect class="line{st}" x="{ex - 8 * mm:.0f}" y="{top}" width="{16 * mm:.0f}" height="{h}" rx="10"/>'
                  + ''.join(f'<line class="line soft" x1="{ex - 8 * mm + 8:.0f}" y1="{top + 14 + i * 14}" x2="{ex + 8 * mm - 8:.0f}" y2="{top + 14 + i * 14}"/>' for i in range(5)))
        o += f'<rect class="ink" x="{cx - 22.5 * mm:.0f}" y="{ya - 8}" width="{45 * mm:.0f}" height="16" rx="3"/>'
        if hot:
            o += f'<rect class="line acc-stroke" x="{cx - 22.5 * mm - 6:.0f}" y="{ya - 14}" width="{45 * mm + 12:.0f}" height="28" rx="6"/>'
        o += ''.join(dot(c, 'a', hot) for c in (20, 21, 22, 23))
        if hot:
            o += halo(X(20), Y('c') + 12, 'Vcc', True, 'middle')
        return o
    P['g_sensor'] = ([(20, 'a'), (21, 'a'), (22, 'a'), (23, 'a')], sensor)
    def jump(c0, k0, c1, k1, hot):
        x0, y0, x1, y1 = X(c0), Y(k0), X(c1), Y(k1)
        return wire(f'M{x0} {y0} C{x0} {(y0 + y1) / 2:.0f} {x1} {(y0 + y1) / 2:.0f} {x1} {y1}', hot) + dot(c0, k0, hot) + dot(c1, k1, hot)
    P['g_vcc'] = ([(20, 'e'), (19, '+b')], lambda hot: jump(20, 'e', 19, '+b', hot))
    P['g_sgnd'] = ([(23, 'e'), (23, '-b')], lambda hot: jump(23, 'e', 23, '-b', hot))
    P['g_trig'] = ([(21, 'e')], lambda hot: off(21, 'e', 12, False, 'pin 12', hot, 'start', tag=hot))
    P['g_echo'] = ([(22, 'e')], lambda hot: off(22, 'e', 12, False, 'pin ~11', hot, 'end', tag=hot))
    P['g_servo'] = ([(17, '+b')], lambda hot: off(17, '+b', 12, False, 'servo red', hot, 'start', tag=hot))
    def led(c, name, side):
        def draw(hot):
            # Seen from above: the round top, with its flat edge on the short leg's side (row c + 1, to the left).
            x, y = (X(c) + X(c + 1)) / 2, Y('c')
            cls = 'acc' if name in lit else 'box'
            o = (f'<circle class="{cls}" cx="{x:.0f}" cy="{y}" r="21"/>'
                 f'<path class="line{" acc-stroke" if hot else ""}" d="M{x - 13:.0f} {y - 17} A21 21 0 1 1 {x - 13:.0f} {y + 17} Z"/>'
                 + dot(c, 'c', hot) + dot(c + 1, 'c', hot))
            if hot:
                o += halo(x + 32 if side == 'right' else x - 32, y + 10, name, True, 'start' if side == 'right' else 'end')
            return o
        return draw
    def res(c0, k0, c1, k1):
        def draw(hot):
            x0, y0, x1, y1 = X(c0), Y(k0), X(c1), Y(k1)
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
            st = ' acc-stroke' if hot else ''
            return (f'<line class="line{st}" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}"/>'
                    f'<g transform="translate({mx:.0f} {my:.0f}) rotate({ang:.0f})"><rect class="box" x="-17" y="-8" width="34" height="16" rx="7"/>'
                    + ''.join(f'<rect class="ink" x="{dx}" y="-7" width="4" height="14"/>' for dx in (-9, -2, 5)) + '</g>'
                    + dot(c0, k0, hot) + dot(c1, k1, hot))
        return draw
    P['g_red'] = ([(5, 'c'), (6, 'c')], led(5, 'red', 'right'))
    P['g_rres'] = ([(6, 'a'), (7, '-t')], res(6, 'a', 7, '-t'))
    P['g_rpin'] = ([(5, 'e')], lambda hot: off(5, 'e', 12, False, 'pin 4', hot, 'end', tag=hot))
    P['g_green'] = ([(8, 'c'), (9, 'c')], led(8, 'green', 'left'))
    P['g_gres'] = ([(9, 'a'), (10, '-t')], res(9, 'a', 10, '-t'))
    P['g_gpin'] = ([(8, 'e')], lambda hot: off(8, 'e', 12, False, 'pin ~5', hot, 'start', tag=hot))
    def gbutton(hot):
        xs, ye, yf = (X(11), X(13)), Y('e'), Y('f')
        cx, cy = sum(xs) / 2, (ye + yf) / 2
        o = ''.join(f'<line class="line" x1="{x}" y1="{y}" x2="{cx + (x - cx) * 0.6:.0f}" y2="{cy + (y - cy) * 0.6:.0f}"/>' for x in xs for y in (ye, yf))
        o += f'<rect class="box" x="{cx - 28:.0f}" y="{cy - 28:.0f}" width="56" height="56" rx="8"/><circle class="ph" cx="{cx:.0f}" cy="{cy:.0f}" r="14"/>'
        if hot:
            o += f'<rect class="line acc-stroke" x="{cx - 34:.0f}" y="{cy - 34:.0f}" width="68" height="68" rx="11"/>'
        return o + ''.join(dot(c, k, hot) for c in (11, 13) for k in 'ef')
    P['g_btn'] = ([(11, 'e'), (13, 'e'), (11, 'f'), (13, 'f')], gbutton)
    P['g_bgnd'] = ([(11, 'a'), (11, '-t')], lambda hot: wire(f'M{X(11)} {Y("a")} V{Y("-t")}', hot) + dot(11, 'a', hot) + dot(11, '-t', hot))
    P['g_bpin'] = ([(13, 'j')], lambda hot: off(13, 'j', 12, False, 'pin 2', hot, 'start', tag=hot))
    return P


BD_ORDER = ['module', 'battery', 'button', 'btn_a', 'btn_j', 'transistor', 'emit_gnd', 'base_res', 'diode',
            'test_jump', 'to_pin5', 'gnd_link', 'motor',
            'g_5v', 'g_gnd', 'g_topgnd', 'g_vcc', 'g_sgnd', 'g_trig', 'g_echo', 'g_servo', 'g_rres', 'g_gres', 'g_rpin', 'g_gpin',
            'g_bgnd', 'g_bpin', 'g_btn', 'g_red', 'g_green', 'g_sensor']
BD_SAY = {'module': 'the power module at the right end, plugged into all four rails', 'battery': 'the battery plug in the module\'s round jack',
          'button': 'a button across the channel in e21, e23, f21, f23', 'btn_a': 'a jumper from a21 to pin 2',
          'btn_j': 'a jumper from j23 to the GND by pin 13', 'transistor': 'the transistor in c12, c11, c10, flat side toward you',
          'emit_gnd': 'a jumper from a12 to the top minus rail', 'base_res': 'the resistor from e11 across the channel to f11',
          'diode': 'the diode from b10 to the top plus rail, stripe at the rail', 'motor': 'the motor from a10 and the top plus rail, held up in the air',
          'test_jump': 'a test jumper from j11 to the bottom plus rail', 'to_pin5': 'a jumper from j11 to pin 5',
          'gnd_link': 'a jumper from the bottom minus rail to a GND pin in the power row',
          'g_5v': 'a jumper from the UNO 5V pin to the bottom plus rail', 'g_gnd': 'a jumper from the UNO GND next to 5V to the bottom minus rail',
          'g_topgnd': 'a jumper from the GND by pin 13 to the top minus rail',
          'g_sensor': 'the ultrasonic sensor standing in a20 to a23, Vcc in a20, its two round eyes facing the far edge',
          'g_vcc': 'a jumper from e20 to the bottom plus rail', 'g_sgnd': 'a jumper from e23 to the bottom minus rail',
          'g_trig': 'a jumper from e21 to pin 12', 'g_echo': 'a jumper from e22 to pin 11', 'g_servo': "the servo's red wire in the bottom plus rail",
          'g_red': 'the red light, long leg c5, short leg c6', 'g_rres': 'a resistor from a6 to the top minus rail', 'g_rpin': 'a jumper from e5 to pin 4',
          'g_green': 'the green light, long leg c8, short leg c9', 'g_gres': 'a resistor from a9 to the top minus rail', 'g_gpin': 'a jumper from e8 to pin 5',
          'g_btn': 'a button across the channel in e11, e13, f11, f13', 'g_bgnd': 'a jumper from a11 to the top minus rail', 'g_bpin': 'a jumper from j13 to pin 2'}


def board(parts, hi=(), on=False, module=True, lit=()):
    """The breadboard, true to scale and as it sits on the table: printing upright, line a at the far edge, rows 1 to 23
    counted leftward from the power module at the right end, every hole on one grid, each 5-hole strip and each rail
    drawn as the joined set it is, rails with their red and blue lines. parts: names in BD_ORDER. hi: the newest parts,
    drawn in orange, and the strips they touch tinted, so the picture shows what just got joined.
    on: the module is switched on, so its light is lit; the fan spins only while the test jumper closes the switch.
    module=False: the module is off the board (the UNO feeds the rails), and the letters move to the row-1 end.
    lit: gate lights drawn on ('red', 'green')."""
    X, Y = bdx, bdy
    spin = on and 'test_jump' in parts
    P = _bd_parts(on, spin, lit)
    o = '<rect class="card" x="82" y="52" width="608" height="456" rx="10"/>'
    o += f'<rect class="chan" x="88" y="{Y("e") + 16}" width="596" height="{Y("f") - Y("e") - 32}" rx="4"/>'
    tint = {_bd_strip(c, k) for n in hi if n in P for c, k in P[n][0]}
    for c in BD_COLS:
        for half, k0, k1 in (('top', 'a', 'e'), ('bottom', 'f', 'j')):
            cls = 'pt' if ('strip', c, half) in tint else 'ph'
            o += f'<rect class="{cls}" x="{X(c) - 8}" y="{Y(k0) - 10}" width="16" height="{Y(k1) - Y(k0) + 20}" rx="8"/>'
    # Each rail's printed line runs on the outside of its pair: red above the + rail, blue below the - rail,
    # on both edges (red above blue, as printed).
    for k, line_y, cl in (('+t', Y('+t') - 13, 'rl-p'), ('-t', Y('-t') + 13, 'rl-n'), ('+b', Y('+b') - 13, 'rl-p'), ('-b', Y('-b') + 13, 'rl-n')):
        cls = 'pt' if ('rail', k) in tint else 'ph'
        o += f'<rect class="{cls}" x="{X(23) - 10}" y="{Y(k) - 8}" width="{X(1) - X(23) + 20}" height="16" rx="8"/>'
        o += f'<line class="{cl}" x1="{X(23) - 10}" y1="{line_y}" x2="{X(1) + 10}" y2="{line_y}"/>'
    for k in BD_ROWS:
        rail = k in ('+t', '-t', '+b', '-b')
        o += ''.join(f'<circle class="hole" cx="{X(c)}" cy="{Y(k)}" r="3.5"/>' for c in BD_COLS if not rail or _bd_rail_hole(c))
    # Row numbers sit above the board like a ruler, clear of the parts; 1, 10, and 20 only, since the steps count
    # from those and the gaps between them hold the wire tags. Letters and rail signs are printed at the far end.
    o += ''.join(f'<text x="{X(c)}" y="40" text-anchor="middle">{c}</text>' for c in (1, 10, 20))
    for k, t in (('+t', '+'), ('-t', '-'), ('a', 'a'), ('e', 'e'), ('f', 'f'), ('j', 'j'), ('+b', '+'), ('-b', '-')):
        o += f'<text x="{X(23) - 34 if module else X(1) + 34}" y="{Y(k) + 11}" text-anchor="middle">{t}</text>'
    has = lambda n: n in parts or (n == 'module' and module)
    for n in BD_ORDER:
        if has(n):
            o += P[n][1](n in hi)
    built = [BD_SAY[n] for n in BD_ORDER if has(n)]
    new = [BD_SAY[n] for n in BD_ORDER if n in hi]
    end = 'from the power module at the right end' if module else 'from the right end, where the power module is taken off'
    return svg('bd', 'The breadboard from above, true to scale, as it sits on the table: printing upright, line a at the far edge, rows '
               '1 to 23 counted leftward ' + end + ', lines a to e and f to j on either side of the middle '
               'channel, and two rails along each long edge, each plus rail marked by a red line and each minus rail by a blue line. On it: '
               + ('; '.join(built) if built else 'nothing yet') + '.' + (' New in this step, in orange: ' + '; '.join(new) + '.' if new else '')
               + (' The module is on and the fan spins.' if spin else ' The module is on and the fan stays still.' if on else ''), o)


def ide_toolbar(mode='verify'):
    """The Arduino IDE 2 toolbar. mode: 'verify' (check mark, with the size report) or 'upload' (round arrow, with the board's lights)."""
    o = ('<rect class="card" x="0" y="0" width="760" height="560" rx="16"/><rect class="ph" x="8" y="12" width="744" height="100" rx="10"/>'
         '<circle class="box" cx="72" cy="62" r="30"/><path class="line" d="M58 63 l10 10 l20 -22"/>'
         '<circle class="box" cx="150" cy="62" r="30"/><path class="line" d="M134 62 h30 M152 50 l12 12 l-12 12"/>'
         '<circle class="box soft" cx="228" cy="62" r="30"/>'
         '<rect class="box" x="290" y="36" width="330" height="52" rx="8"/><text x="310" y="73">Arduino UNO</text>'
         + ''.join(f'<rect class="ph" x="40" y="{y}" width="{w}" height="14" rx="4"/>' for y, w in ((200, 360), (236, 520), (272, 440), (308, 300), (344, 400)))
         + '<rect class="box" x="16" y="392" width="728" height="150" rx="10"/>')
    if mode == 'verify':
        o += ('<circle class="line acc-stroke" cx="72" cy="62" r="40"/><text class="t-acc" x="40" y="160">Verify</text>'
              '<text x="36" y="448">Sketch uses 922 bytes (2%)</text><text x="36" y="500">Maximum is 32256 bytes.</text>')
        label = 'The Arduino IDE toolbar with the check mark, Verify, circled. The output panel at the bottom reads: Sketch uses 922 bytes, 2 percent. Maximum is 32256 bytes.'
    else:
        o += ('<circle class="line acc-stroke" cx="150" cy="62" r="40"/><text class="t-acc" x="118" y="160">Upload</text>'
              '<rect class="box" x="410" y="290" width="334" height="66" rx="10"/><text x="430" y="334">Done uploading.</text>'
              '<text class="soft" x="36" y="448">on the board:</text>'
              + ''.join(f'<rect class="lled {c}" x="{x}" y="482" width="40" height="22" rx="5"/><text x="{x + 52}" y="506">{t}</text>'
                        for x, t, c in ((40, 'TX', 'tb-tx'), (220, 'RX', 'tb-rx'), (400, 'L', 'tb-l'))))
        label = 'The Arduino IDE toolbar with the round arrow, Upload, circled. A pop-up reads Done uploading, and the board\'s TX and RX lights flicker before the L light blinks fast.'
    return svg('tb', label, o)


UP_CABLE = [(256, 300), (330, 300), (400, 330), (470, 300), (520, 300)]


def upload_path():
    """How a sketch gets onto the board: write, Verify, Upload, run. Four beats."""
    laptop = ('<rect class="box" x="20" y="150" width="236" height="150" rx="10"/><rect class="ph" x="38" y="166" width="200" height="118" rx="4"/>'
              '<path class="box" d="M0 300 h276 l-18 26 h-240 z"/>'
              + ''.join(f'<rect class="ink" x="54" y="{y}" width="{w}" height="10" rx="3"/>' for y, w in ((184, 120), (208, 160), (232, 100), (256, 140))))
    board = ('<rect class="box" x="520" y="170" width="230" height="200" rx="14"/><rect class="ink" x="506" y="280" width="30" height="40" rx="4"/>'
             '<rect class="chip" x="580" y="270" width="130" height="50" rx="6"/>')
    cable = '<path class="wire" d="M256 300 C320 300 340 330 400 330 C460 330 470 300 520 300"/>'
    s1 = '<g data-stage="1"><text class="t-acc" x="138" y="380" text-anchor="middle">sketch</text></g>'
    s2 = ('<g data-stage="2"><rect class="box" x="280" y="150" width="210" height="64" rx="10"/><text x="385" y="194" text-anchor="middle">10110010</text>'
          '<text class="t-acc" x="385" y="126" text-anchor="middle">Verify</text></g>')
    s3 = ('<g data-stage="3">' + flow_dots('up-e', UP_CABLE, 5)
          + '<text class="t-acc" x="400" y="400" text-anchor="middle">Upload</text></g>')
    s4 = ('<g data-stage="4"><rect class="acc" x="580" y="270" width="130" height="50" rx="6"/><rect class="lled up-l" x="560" y="200" width="34" height="20" rx="4"/>'
          '<text x="606" y="218">L</text><text class="t-acc" x="635" y="420" text-anchor="middle">runs</text></g>')
    return svg('up', 'A laptop with a sketch on screen, a USB cable, and the UNO. Verify turns the sketch into numbers, ones and zeros. Upload sends them down the cable to the board. The board saves them and runs them, and its L light blinks.',
               laptop + board + cable + s1 + s2 + s3 + s4)


TS_PATH = [(380, 40), (380, 530)]


def transistor_switch(diode=True):
    """Why the fan needs a transistor: the pin can't power it, but it can flip a switch the module's power runs through.
    diode=False leaves out the fourth beat (the diode), for a three-beat slide."""
    o = ('<line class="line" x1="0" y1="40" x2="760" y2="40"/><text x="0" y="28">+ rail</text>'
         '<line class="line soft" x1="0" y1="530" x2="760" y2="530"/><text x="420" y="518">- rail</text>')
    o += ('<path class="wire" d="M380 40 V90"/><rect class="box" x="320" y="90" width="120" height="100" rx="12"/>'
          '<text x="300" y="150" text-anchor="end">fan</text>'
          '<rect class="box" x="20" y="285" width="140" height="70" rx="10"/><text x="90" y="331" text-anchor="middle">pin 5</text>')
    still_fan = fan(380, 140, 'ink', '', 0.45)
    s1 = ('<g data-until="2">' + still_fan + '<path class="dash" d="M90 285 V170 H320"/><path class="line acc-stroke" d="M186 156 l28 28 M214 156 l-28 28"/>'
          '</g>')
    s2 = ('<g data-stage="2">' + fan(380, 140, 'acc', 'ts-spin', 0.45)
          + '<path class="wire" d="M380 190 V280"/><rect class="box" x="330" y="280" width="100" height="80" rx="10"/>'
          '<path class="wire" d="M380 360 V530"/><path class="wire-acc" d="M160 320 H330"/>'
          + flow_dots('ts-e', TS_PATH, 5)
          + '<text class="t-acc" x="180" y="300">small</text><text class="t-acc" x="400" y="262">big</text>'
          '<text x="450" y="335">transistor</text></g>')
    s3 = ('<g data-stage="3"><line class="wire-acc" x1="0" y1="40" x2="760" y2="40"/><text class="t-acc" x="20" y="96">from the module</text></g>')
    s4 = ('<g data-stage="4"><path class="wire" d="M380 235 H560 V40"/><rect class="ink" x="546" y="100" width="28" height="70" rx="6"/>'
          '<rect class="dstripe-r" x="546" y="106" width="28" height="14"/>'
          '<text class="t-acc" x="585" y="130">jolt</text><text class="t-acc" x="585" y="170">goes here</text></g>')
    label = ('Plus rail at the top, minus rail at the bottom. A fan hangs from the plus rail. Pin 5 gives only a little power and the fan needs more, so a direct wire is crossed out. Then a transistor sits under the fan. A small flow from pin 5 into it lets a big flow go from the plus rail through the fan to ground, and the fan spins. The power comes from the module. The pin only flips the switch.'
             + (' Last, a diode across the fan gives the motor\'s jolt a safe path when it stops.' if diode else ''))
    return svg('ts', label, o + s1 + s2 + s3 + (s4 if diode else ''))


def arm_timeline():
    """The board can't see the arm: write(90) then the fan, against one degree at a time then the fan."""
    o = ('<text x="20" y="44">write(90), then the fan</text>'
         '<line class="line soft" x1="40" y1="250" x2="740" y2="250"/><text x="0" y="141">90</text><text x="14" y="261">0</text>'
         '<path class="line" d="M60 250 C100 250 130 130 180 130 H740"/>'
         '<text x="20" y="330">one degree at a time</text>'
         '<line class="line soft" x1="40" y1="520" x2="740" y2="520"/><text x="0" y="431">90</text><text x="14" y="531">0</text>')
    stair = 'M60 520' + ''.join(' h40 v-7.14' for _ in range(14)) + ' H740'
    s1 = ('<g data-stage="1"><line class="wire-acc" x1="66" y1="100" x2="66" y2="250"/><text class="t-acc" x="80" y="106">fan on</text>'
          '<text class="t-acc" x="210" y="180">fan starts mid-move</text></g>')
    s2 = ''
    s3 = (f'<g data-stage="3"><path class="line" d="{stair}"/><text class="t-acc" x="60" y="392">wait 15 ms each degree</text></g>')
    s4 = ('<g data-stage="4"><line class="wire-acc" x1="622" y1="400" x2="622" y2="520"/><text class="t-acc" x="634" y="480">fan on</text></g>')
    return svg('at', 'Two timelines of the servo arm\'s angle. Top: write 90, then the fan line runs right away, so the fan starts while the arm is still moving. Bottom: the arm steps up one degree at a time, waiting 15 milliseconds each degree, and the fan turns on only after the last step, when the arm is at 90.',
               o + s1 + s2 + s3 + s4)


def servo_sweep90():
    """A servo whose arm sweeps from 0 up to 90 and back, over and over (Sweep with both 180s changed to 90)."""
    o = ('<rect class="box" x="230" y="330" width="300" height="140" rx="14"/><text x="380" y="420" text-anchor="middle">servo</text>'
         '<path class="dash" d="M200 330 A180 180 0 0 1 380 150"/>'
         '<text x="180" y="342" text-anchor="end">0</text><text x="380" y="128" text-anchor="middle">90</text>'
         '<g class="s9-arm"><line class="wire-acc" x1="380" y1="330" x2="380" y2="170"/></g><circle class="ink" cx="380" cy="330" r="20"/>')
    return svg('s9', 'A servo from the front. Its arm sweeps from 0 degrees, pointing left, up to 90, pointing straight up, and back down, over and over.', o)


def press_sequence(fan_on=True):
    """Press, the arm climbs to 90, then (fan_on) the fan starts. Loops while the slide is up."""
    d = 0 if fan_on else 140   # without the fan, centre the two parts
    o = (tact(40 + d, 200, 140) + f'<circle class="acc ps-btn" cx="{110 + d}" cy="270" r="35"/><text x="{110 + d}" y="430" text-anchor="middle">press</text>'
         f'<path class="line" d="M{200 + d} 270 h56 M{244 + d} 258 l12 12 l-12 12"/>'
         f'<rect class="box" x="{290 + d}" y="250" width="180" height="90" rx="12"/><circle class="ink" cx="{340 + d}" cy="250" r="16"/>'
         f'<g class="ps-arm" style="transform-origin: {340 + d}px 250px"><line class="wire-acc" x1="{340 + d}" y1="250" x2="{340 + d}" y2="160"/></g>'
         f'<text x="{380 + d}" y="430" text-anchor="middle">up to 90</text>')
    if fan_on:
        o += ('<path class="line" d="M490 270 h56 M534 258 l12 12 l-12 12"/>'
              + fan(650, 270, 'acc', 'ps-fan', 0.9) + '<circle class="box" cx="650" cy="270" r="22"/><text x="650" y="430" text-anchor="middle">then fan</text>')
        return svg('ps', 'Three steps in a row: the button is pressed, the servo arm climbs from 0 up to 90 degrees, and only then does the fan start spinning.', o)
    return svg('ps', 'Two steps in a row: the button is pressed, and the servo arm climbs from 0 up to 90 degrees and stays there.', o)


PARTS_ICONS = {
    'sensor': ('<rect class="box" x="56" y="22" width="140" height="56" rx="6"/>'
               + ''.join(f'<circle class="box" cx="{x}" cy="50" r="22"/><circle class="ph" cx="{x}" cy="50" r="12"/>' for x in (94, 158))
               + ''.join(f'<rect class="ink" x="{x}" y="78" width="6" height="12"/>' for x in (108, 120, 132, 144))),
    'transistor': ('<path class="box" d="M96 70 V52 A30 30 0 0 1 156 52 V70 Z"/>'
                   + ''.join(f'<line class="line" x1="{x}" y1="70" x2="{x}" y2="100"/>' for x in (106, 126, 146))),
    'diode': ('<line class="line" x1="40" y1="55" x2="212" y2="55"/><rect class="ink" x="92" y="40" width="68" height="30" rx="8"/>'
              '<rect class="dstripe-r" x="140" y="40" width="10" height="30"/>'),
}


def parts_grid(cells, label):
    """Up to 12 parts in a 3 x 4 grid. cells: (icon name, caption). Icons: the parts_kit() set plus PARTS_ICONS."""
    icons = dict(_kit_icons(), **PARTS_ICONS)
    out = ''
    for i, (key, name) in enumerate(cells):
        x0, y0 = (i % 3) * 253, (i // 3) * 140
        out += f'<g transform="translate({x0} {y0})">{icons[key]}<text x="126" y="128" text-anchor="middle">{name}</text></g>'
    return svg('pk', label, out)


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
                   f'  <div class="split__main"><p class="sub">{do}</p><ol class="beats"><li data-beat>{see}' + (f'<span class="detail">{detail}</span>' if detail else '') + '</li></ol></div>\n'
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
.steps { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--st-2); counter-reset: step; }
.steps li { counter-increment: step; display: grid; grid-template-columns: var(--st-7) 1fr; column-gap: var(--st-2); font-size: var(--s-body-sm); line-height: 1.2; }
.steps li::before { content: counter(step, decimal-leading-zero); font-family: var(--acm-font-code); font-weight: 500; color: var(--acm-primary); }
.steps code { font-family: var(--acm-font-code); }
.slide[data-ground="orange"] .steps li::before { color: currentColor; }
.slide[data-do] .clock__digits { font-size: calc(64 * var(--u)); }
.slide[data-do] .clock { display: grid; grid-template-columns: auto 1fr; align-items: baseline; column-gap: var(--st-3); row-gap: var(--st-1); }
.slide[data-do] .clock__digits { grid-column: 1; grid-row: 1; }
.slide[data-do] .clock__hint { grid-column: 2; grid-row: 1; margin: 0; }
.slide[data-do] .clock__track { grid-column: 1 / -1; grid-row: 2; }
.slide[data-do] .split__main { gap: var(--st-3); }
.viz .dbody { stroke: currentColor; stroke-width: 20; stroke-linecap: round; }
.viz .dstripe { stroke: var(--acm-surface); stroke-width: 20; }
.viz .dstripe-r { fill: var(--acm-surface); }
.viz .rl-p { stroke: var(--acm-mark-failure); stroke-width: 3; }
.viz .rl-n { stroke: var(--acm-mark-xref); stroke-width: 3; }
.viz .chan { fill: var(--acm-outline-variant); opacity: 0.55; }
.viz .pt { fill: var(--acm-primary); opacity: 0.22; }
.viz .halo { paint-order: stroke; stroke: var(--acm-surface); stroke-width: 10px; stroke-linejoin: round; }
.is-presenting .slide.is-current .viz--bd .bd-spin { transform-box: view-box; transform-origin: 586px 196px; animation: spin 0.6s linear infinite; }
.is-presenting .slide.is-current .viz--bz .bz-spin { transform-box: view-box; transform-origin: 680px 196px; animation: spin 0.6s linear infinite; }
.is-presenting .slide.is-current .viz--ts .ts-spin { transform-box: view-box; transform-origin: 380px 140px; animation: spin 0.6s linear infinite; }
.is-presenting .slide.is-current .viz--ts .ts-e { animation: ts-e 2.4s linear infinite; animation-delay: calc(var(--n) * -0.48s); }
TS_KEYFRAMES
.is-presenting .slide.is-current .viz--up .up-e { animation: up-e 2s linear infinite; animation-delay: calc(var(--n) * -0.4s); }
UP_KEYFRAMES
.is-presenting .slide.is-current .viz--up .up-l { animation: blink 0.4s step-end infinite; }
.is-presenting .slide.is-current .viz--tb :is(.tb-tx, .tb-rx) { animation: tb-flick 3s step-end infinite; }
.is-presenting .slide.is-current .viz--tb .tb-rx { animation-delay: -0.1s; }
.is-presenting .slide.is-current .viz--tb .tb-l { animation: tb-l 3s step-end infinite; }
@keyframes tb-flick { 0%, 8%, 16%, 24%, 32% { opacity: 1; } 4%, 12%, 20%, 28%, 36%, 100% { opacity: 0.15; } }
@keyframes tb-l { 0%, 44%, 52%, 60%, 68%, 76%, 84%, 92% { opacity: 0.15; } 40%, 48%, 56%, 64%, 72%, 80%, 88%, 96% { opacity: 1; } }
.is-presenting .slide.is-current .viz--ps .ps-arm { transform-box: view-box; transform-origin: 340px 250px; animation: ps-arm 4s var(--acm-ease-standard) infinite; }
@keyframes ps-arm { 0%, 12% { transform: rotate(-90deg); } 50%, 100% { transform: rotate(0deg); } }
.is-presenting .slide.is-current .viz--ps .ps-fan { transform-box: view-box; transform-origin: 650px 270px; animation: ps-fan 4s linear infinite; }
@keyframes ps-fan { 0%, 55% { transform: rotate(0deg); } 100% { transform: rotate(1080deg); } }
.is-presenting .slide.is-current .viz--s9 .s9-arm { transform-box: view-box; transform-origin: 380px 330px; animation: s9-arm 2.8s linear infinite; }
@keyframes s9-arm { 0%, 100% { transform: rotate(-90deg); } 50% { transform: rotate(0deg); } }
.viz--ps .ps-btn { opacity: 0; }
.is-presenting .slide.is-current .viz--ps .ps-btn { animation: ps-btn 4s step-end infinite; }
@keyframes ps-btn { 0% { opacity: 1; } 10% { opacity: 0; } }
'''


def _is_picture_motion(line):
    return '@keyframes' in line or '.is-presenting' in line or 'KEYFRAMES' in line or line.startswith('.viz--')


def lab_css_base():
    """The lab slides' list and Do-slide styles plus the static picture classes. No animation."""
    return '\n'.join(l for l in LAB_CSS.split('\n') if not _is_picture_motion(l))


def lab_css_pictures():
    """Only the picture animations (wires, current dots, spinning parts), with their keyframes filled in."""
    motion = '\n'.join(l for l in LAB_CSS.split('\n') if _is_picture_motion(l))
    return (motion.replace('LP_KEYFRAMES', path_keyframes('lp-e', LOOP))
                  .replace('LR_KEYFRAMES', path_keyframes('lr-e', LED_RAILS))
                  .replace('TS_KEYFRAMES', path_keyframes('ts-e', TS_PATH))
                  .replace('UP_KEYFRAMES', path_keyframes('up-e', UP_CABLE)))


def lab_css():
    """Everything: lab_css_base() and lab_css_pictures() in the original order. Older decks call this."""
    return (LAB_CSS.replace('LP_KEYFRAMES', path_keyframes('lp-e', LOOP))
                   .replace('LR_KEYFRAMES', path_keyframes('lr-e', LED_RAILS))
                   .replace('TS_KEYFRAMES', path_keyframes('ts-e', TS_PATH))
                   .replace('UP_KEYFRAMES', path_keyframes('up-e', UP_CABLE)))
