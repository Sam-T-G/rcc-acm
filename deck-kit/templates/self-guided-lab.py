"""Template: a self-guided lab deck (decision log 2026-10-28).

Tables build from a companion page at their own pace; the projector only frames the rounds:

    cover, the build, rules, then for each round: its map slide, then its win slide, then a work
    clock, pack up, wrap

Usage (from the repo root, with a Python that has segno):
    python deck-kit/templates/self-guided-lab.py <out.html>

Edit BUILD and ROUNDS. Step-by-step projected rounds (one slide per wire) live in
deck-kit/lab/labkit.py instead; this template is for labs where the page carries the steps.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'lab'))
from partials import qr, round_map, rules, sendoff, win, work_clock  # noqa: E402

BUILD = dict(date='2026-10-29', day='Thursday, October 29', start='13:30', ends='14:25',
             title='Build a small machine, one round at a time', url='https://example.com/lab/',
             ledger='ACM @ RCC · Deck kit · self-guided lab template')
ROUNDS = [  # (short name, map headline, win headline, what a working build does, [(problem, fix)])
    ('Set up', 'Get power to the breadboard', 'Power is on', 'The board light is on and nothing gets warm.',
     [('No light?', 'Check the USB cable is all the way in')]),
    ('Sensor', 'Make the sensor read a distance', 'The sensor reads', 'The number drops as your hand comes closer.',
     [('Always 0?', 'Swap the two signal wires'), ('Jumps around?', 'Use a flat object, not your hand')]),
    ('Output', 'Make something move', 'It moves', 'The arm lifts when something is close and drops when it leaves.',
     [('Nothing moves?', 'Check the signal wire is on the right pin')]),
]


def notes(*ps, bridge=None):
    b = ''.join(f'<p>{p}</p>' for p in ps) + (f'<p class="bridge">{bridge}</p>' if bridge else '')
    return f'<aside class="notes">{b}</aside>'


names = [r[0] for r in ROUNDS]
S = [f'''<section class="slide" data-kind="cover" data-starts="{BUILD['start']}" aria-label="Cover">
  <div class="cover__rail" aria-hidden="true"></div>
  <p class="cover__name">ACM @ RCC</p>
  <p class="eyebrow"><time datetime="{BUILD['date']}">{BUILD['day']}</time></p>
  <h1>{BUILD['title']}</h1>
  <p class="sub">The page has every step. <strong>Hints and answers are there if you get stuck.</strong></p>
  {notes('Say the club name first.', bridge='Here is the page.')}
</section>
''']
S.append(sendoff('Every table', 'Open the build page', 'Start with round 1. Each round ends with a check that it works.', BUILD['url'],
                 section='Start', ground='tint', note='Two or three people per kit.', bridge='Rules before anyone plugs in.'))
S.append(rules('Every table', 'Before you plug in', [('Unplug USB before you move a wire', 'Plug it back in only to test'),
                                                      ('Ask before you use a part not on the page', None)],
               warn='Read the part labels before it goes in. Power on the wrong pin can break it.', note='Read these out loud.', bridge='Round 1.'))
grounds = [None, 'warm']
for k, (name, h2, wh2, see, fixes) in enumerate(ROUNDS, 1):
    S.append(round_map(h2, names, k, section=name, ground=grounds[k % 2], sub=f'About {4 + 2 * k} minutes.',
                       note='Leave this up while tables work on the round.', bridge='When it works, it looks like this.'))
    S.append(win(wh2, see, fixes, note='Ask one table to show theirs.', bridge='Next round.' if k < len(ROUNDS) else 'Now the challenges.'))
S.append(work_clock('Go as far as you can', 'Finished? Try a challenge from the page.', ends=BUILD['ends'], ground='tint', section='Challenges',
                    note='Press T.', bridge='Pack up.'))
S.append(f'''<section class="slide" data-kind="beats" data-ground="warm" aria-label="Pack up">
  <h2>Pack up</h2>
  <ol class="beats"><li data-beat>Unplug the USB cable</li><li data-beat>Every part back in the kit box</li></ol>
  {notes('Count parts back into each kit.', bridge='One last thing.')}
</section>
''')
S.append(f'''<section class="slide" data-kind="ask" data-room aria-label="Wrap-up">
  <div class="ask__main">
    <p class="eyebrow">Before you go</p>
    <h2>The page stays up after today</h2>
    <p class="ask__meta">Thursdays, <time datetime="13:30">1:30</time> to <time datetime="14:30">2:30 PM</time>, BLCIS A-210</p>
  </div>
  <div class="qrs">{qr(BUILD['url'])}</div>
  <div class="ask__foot"><p class="ask__name">ACM @ RCC</p><p class="ask__stamp">Updated <time datetime="{BUILD['date']}">{BUILD['date']}</time></p></div>
  {notes('Finish at home with the same page.')}
</section>
''')

KIT = os.path.relpath(os.path.join(HERE, '..'), os.path.dirname(os.path.abspath(sys.argv[1])))
html = f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ACM @ RCC, {BUILD['date']}</title>
<!-- Made from deck-kit/templates/self-guided-lab.py. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400..700;1,14..32,400..700&family=JetBrains+Mono:ital,wght@0,400..700;1,400..700&display=swap">
<link rel="stylesheet" href="{KIT}/deck.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js" integrity="sha512-oJ8QbaQThQoJZ7oEv+29jfPM6CcP+zUxh3PKJs1vyOhx0UraUrE7PQgeItu3dOuCJyrzWpoYMsVjkkPEBzbUqw==" crossorigin="anonymous" referrerpolicy="no-referrer" defer></script>
<script src="{KIT}/deck.js" defer></script>
<script src="{KIT}/presenter.js" defer></script>
</head>
<body>
<main class="deck" data-deck="acm-{BUILD['date']}-lab" data-ledger="{BUILD['ledger']}">

''' + '\n'.join(S) + '</main>\n</body>\n</html>\n'
open(sys.argv[1], 'w').write(html)
print('slides', len(S), '->', sys.argv[1])
