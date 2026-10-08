"""Builds deck-kit/lab/example-lab.html: one full lab round written to the spec.

Copy this file to start a new lab deck. Run: python3 deck-kit/lab/example_lab.py
Check: node deck-kit/check.mjs deck-kit/lab/example-lab.html
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from labkit import bb, check, do_slide, lab_css, loop_basic, notes, parts_kit, split_beats, steps  # noqa: E402

OUT = os.path.join(HERE, 'example-lab.html')
S = []

S.append('''<section class="slide" data-kind="cover" aria-label="Cover">
  <div class="cover__rail" aria-hidden="true"></div>
  <p class="cover__name">ACM @ RCC</p>
  <p class="eyebrow">Lab kit example</p>
  <h1>One round, written to the spec</h1>
  <p class="sub">A concept, seven steps, and a check-in. <strong>Copy this file to start a lab.</strong></p>
  ''' + notes('This deck exists to show the lab spec working. Read docs/03-playbooks/arduino-lab/instruction-spec.md first.',
              bridge='Every lab starts by finding the parts.') + '\n</section>\n')

S.append(do_slide('Find your parts', 'Do it · two minutes', 'Find your parts', [
    'Take out the breadboard, power module, and 9V battery',
    'Take out the UNO board, USB cable, and jumper wires',
    'Take out one red LED, one 220 Ω resistor, two buttons',
    'Take out the fan blade, the motor, and the servo'],
    120, parts_kit(), section='Circuits', ground='warm',
    note=notes('Names come from the parts glossary.', bridge='One idea behind every circuit.')))

S.append(split_beats('Every circuit is a loop', 'Circuits from zero', 'Every circuit is a loop', [
    ('Electricity leaves +, comes back to -', 'No way back, nothing flows'),
    ('Your part sits in the loop', 'It lights up, spins, or beeps'),
    ('Break the loop anywhere, it all stops', 'That\'s all a switch does'),
    ('Something in the loop has to slow it', 'With nothing there, it\'s a short')],
    loop_basic(), auto=2.5,
    note=notes('A concept slide fills in on its own.', bridge='Build one.')))

ALL = ['module', 'jumpers', 'battery', 'resistor', 'led', 'ground']
S.extend(steps('Light an LED', [
    ('Put the power module on the end',
     'Take the power module. Line up its + pins with the red lines and its - pins with the blue lines. Press it into the left end of the breadboard until its pins sink into the rails.',
     'It sits flat across both rails', '+ on red, - on blue', bb(['module'], hi=('module',)), notes('Backwards reverses the power.')),
    ('Set both jumpers to 5V',
     'Find the two small caps (jumpers) on the module, one on each side. Pull each cap off and push it back on over the pins labelled 5V.',
     'Both jumpers on 5V', 'Not 3.3V, and not OFF', bb(['module', 'jumpers'], hi=('jumpers',)), notes('Both OFF means nothing turns on.')),
    ('Plug in the 9V battery',
     'Check that the module\'s light is off. Snap the battery cable onto the 9V battery if it isn\'t already, then push its round plug into the round jack on the module.',
     'The light stays off for now', 'The switch is still off', bb(['module', 'jumpers', 'battery'], hi=('battery',)), notes('Never more than 9V.')),
    ('Add the resistor',
     'Take one resistor labelled 220. Bend both legs down. Plug one leg into any hole in the top + rail (red line) and the other leg into hole a10.',
     'One leg in the rail, one in row 10', 'Each leg in its own spot', bb(ALL[:4], hi=('resistor',)), notes('It works either way around.')),
    ('Add the LED',
     'Take one red LED. Plug its long leg into hole c10 and its short leg into hole c11.',
     'The long leg shares row 10 with the resistor', 'That\'s how they connect', bb(ALL[:5], hi=('led',)), notes('Long leg is +.')),
    ('Connect the short leg to ground',
     'Take a jumper wire. Plug one end into hole a11 and the other end into any hole in the top - rail (blue line).',
     'Row 11 now runs to the - rail', 'The loop is closed', bb(ALL, hi=('ground',)), notes('The - rail is ground.')),
    ('Trace it, then switch on',
     'Run your finger along the path: + rail, resistor, row 10, LED, row 11, jumper, - rail. Then press the module\'s power switch.',
     'The module light and your LED turn on', 'Dark LED? Flip it around', bb(ALL, hi=('resistor', 'led', 'ground'), lit=True, on=True),
     notes('Hands off after this step.', bridge='Check in.')),
]))

S.append(check('Why your LED lit up', 'Why your LED lit up', [
    ('It lit up', 'The loop is complete: +, resistor, LED, back to -'),
    ('Now pull one wire out', 'Dark. No loop, nothing flows'),
    ('Why the resistor?', 'It slows the flow so the LED doesn\'t burn out'),
    ('Habits you just used', 'Power off while wiring, trace before switching on')],
    notes('Ask first, then press.', bridge='That\'s the round.'), ground='tint'))

S.append('''<section class="slide" data-kind="ask" data-section="Close" aria-label="Next">
  <div class="ask__main">
    <p class="eyebrow">Your turn</p>
    <h2>Write the next round on the template</h2>
    <p class="sub">templates/arduino-lab-round.md, then build it with labkit.</p>
  </div>
  <div class="ask__foot">
    <p class="ask__name">ACM @ RCC</p>
    <p class="ask__stamp">Updated <time datetime="2026-10-07">2026-10-07</time></p>
  </div>
  ''' + notes('Run the check before you present.') + '\n</section>\n')

S = [x.replace('<aside class="notes">', '<aside class="notes"><p>Fills in on its own. One press lands the rest; the next press moves on.</p>', 1) if 'data-auto=' in x.split('>', 1)[0] else x for x in S]

HEAD = f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ACM @ RCC, lab kit example</title>
<!-- Built by deck-kit/lab/example_lab.py from labkit.py. Do not edit by hand; edit the generator. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400..700;1,14..32,400..700&family=JetBrains+Mono:ital,wght@0,400..700;1,400..700&display=swap">
<link rel="stylesheet" href="../deck.css">
<style>{lab_css()}</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js" integrity="sha512-oJ8QbaQThQoJZ7oEv+29jfPM6CcP+zUxh3PKJs1vyOhx0UraUrE7PQgeItu3dOuCJyrzWpoYMsVjkkPEBzbUqw==" crossorigin="anonymous" referrerpolicy="no-referrer" defer></script>
<script src="../deck.js" defer></script>
<script src="../presenter.js" defer></script>
</head>
<body>
<main class="deck" data-deck="acm-lab-example" data-ledger="ACM @ RCC · Lab kit example">

'''

open(OUT, 'w').write(HEAD + '\n'.join(S) + '\n</main>\n</body>\n</html>\n')
print('slides', len(S))
