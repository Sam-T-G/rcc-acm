"""Template: a two-track work session deck (decision log 2026-10-28).

The room splits into two groups that each work from their own page. The deck only opens the
meeting, has people pick, hands each group its page, and keeps a work clock up:

    cover, the hour, coming up, pick, send-off A, send-off B, rules, work clock, pack up, wrap

Usage (from the repo root, with a Python that has segno):
    python deck-kit/templates/two-track.py <out.html>            # example copy, passes the check
    python deck-kit/templates/two-track.py <out.html> --blank    # fill: markers where copy goes

Edit the TRACKS and DATES blocks, or copy this file next to the meeting and change it there
(scratch/<date>-deck/gen.py is the usual place). Every slide comes from deck-kit/lab/partials.py
or a plain kind from deck-kit/README.md. Run node deck-kit/check.mjs <out.html> before publishing.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'lab'))
from partials import pick, qr, rules, sendoff, work_clock  # noqa: E402

BLANK = '--blank' in sys.argv
F = (lambda what: f'<!-- fill: {what} -->[TBD]') if BLANK else (lambda what: None)


def t(text, what):
    return F(what) or text


DECK = dict(date='2026-10-29', day='Thursday, October 29', start='13:30', ends='14:25',
            ledger='ACM @ RCC · Deck kit · two-track template', title='Pick a track and work at your own pace')
TRACKS = [
    dict(name='Track A', blurb='Short line on what group A does.', url='https://example.com/track-a/',
         h2='Open this page on your laptop', sub='One line on where the page starts.'),
    dict(name='Track B', blurb='Short line on what group B does.', url='https://example.com/track-b/',
         h2='Build it at your own pace', sub='One line on where the page starts and where help is.'),
]
DATES = [('2026-11-05', 'Thu, Nov 5', 'Next meeting')]
RULES = [('Unplug USB before you move a wire', 'Plug it back in only to test'),
         ('Take the power module off the breadboard', 'The board gets power from USB')]
WARN = 'Read the part labels before it goes in. Power on the wrong pin can break it.'


def notes(*ps, bridge=None):
    b = ''.join(f'<p>{p}</p>' for p in ps) + (f'<p class="bridge">{bridge}</p>' if bridge else '')
    return f'<aside class="notes">{b}</aside>'


A, B = TRACKS
S = []
S.append(f'''<section class="slide" data-kind="cover" data-starts="{DECK['start']}" aria-label="Cover">
  <div class="cover__rail" aria-hidden="true"></div>
  <p class="cover__name">ACM @ RCC</p>
  <p class="eyebrow"><time datetime="{DECK['date']}">{DECK['day']}</time></p>
  <h1>{t(DECK['title'], 'the meeting in one line')}</h1>
  <p class="sub">{t('Two groups, two pages.', 'what happens')} <strong>{t('Start the moment you sit down.', 'the bold clause')}</strong></p>
  {notes('Say the club name first.', bridge='Here is how the hour goes.')}
</section>
''')
S.append(f'''<section class="slide" data-kind="beats" data-section="Today" data-ground="tint" aria-label="The hour">
  <h2>How the hour goes</h2>
  <ol class="beats">
    <li data-beat>Pick a track<span class="detail">Sit with your group</span></li>
    <li data-beat>Open your page<span class="detail">Everything you need is on it</span></li>
    <li data-beat>Work at your own pace<span class="detail">Officers walk around to help</span></li>
  </ol>
  {notes('Three lines, then go.', bridge='Dates first.')}
</section>
''')
S.append(f'''<section class="slide" data-kind="board" data-ground="warm" aria-label="Coming up">
  <h2>Coming up</h2>
  <ol class="board">{''.join(f'<li><time datetime="{d}">{w}</time><span>{t(x, "what is on this date")}</span></li>' for d, w, x in DATES)}</ol>
  {notes('Source every date in the notes.', bridge='Now pick.')}
</section>
''')
S.append(pick((A['name'], t(A['blurb'], 'track A in one line')), (B['name'], t(B['blurb'], 'track B in one line')),
              h2='Pick one for today', section='Pick', note='Thirty seconds to move.', bridge=f"{A['name']}, here is your page."))
S.append(sendoff(A['name'], t(A['h2'], 'send-off A headline'), t(A['sub'], 'send-off A line'), A['url'], section='Go',
                 note='Group A starts now.', bridge=f"{B['name']}, here is yours."))
S.append(sendoff(B['name'], t(B['h2'], 'send-off B headline'), t(B['sub'], 'send-off B line'), B['url'], ground='tint',
                 note='Group B starts now.', bridge='Rules before anyone plugs in.'))
S.append(rules(B['name'], 'Before you plug in', RULES, warn=WARN, note='These prevent the problems you cannot fix in the room.', bridge='Go.'))
S.append(work_clock('Go as far as you can', t('Group A: next problem. Group B: next step.', 'one line per group'), ends=DECK['ends'],
                    note='Press T. It counts down to the end time, so starting late is fine.', bridge='Time to pack up.'))
S.append(f'''<section class="slide" data-kind="beats" data-section="Wrap" data-ground="warm" aria-label="Pack up">
  <h2>Pack up</h2>
  <ol class="beats">
    <li data-beat>Unplug the USB cable</li>
    <li data-beat>Every part back in the kit box</li>
    <li data-beat>Save your code</li>
  </ol>
  {notes('Count parts back into each kit.', bridge='One last thing.')}
</section>
''')
S.append(f'''<section class="slide" data-kind="ask" data-room aria-label="Wrap-up">
  <div class="ask__main">
    <p class="eyebrow">Before you go</p>
    <h2>{t('Both pages stay up after today', 'the one ask')}</h2>
    <p class="ask__meta">Thursdays, <time datetime="13:30">1:30</time> to <time datetime="14:30">2:30 PM</time>, BLCIS A-210</p>
  </div>
  <div class="qrs">{qr(A['url'])}{qr(B['url'])}</div>
  <div class="ask__foot">
    <p class="ask__name">ACM @ RCC</p>
    <p class="ask__stamp">Updated <time datetime="{DECK['date']}">{DECK['date']}</time></p>
  </div>
  {notes('Both QR codes again for anyone who missed them.')}
</section>
''')

KIT = os.path.relpath(os.path.join(HERE, '..'), os.path.dirname(os.path.abspath(sys.argv[1])))
html = f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ACM @ RCC, {DECK['date']}</title>
<!-- Made from deck-kit/templates/two-track.py. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400..700;1,14..32,400..700&family=JetBrains+Mono:ital,wght@0,400..700;1,400..700&display=swap">
<link rel="stylesheet" href="{KIT}/deck.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js" integrity="sha512-oJ8QbaQThQoJZ7oEv+29jfPM6CcP+zUxh3PKJs1vyOhx0UraUrE7PQgeItu3dOuCJyrzWpoYMsVjkkPEBzbUqw==" crossorigin="anonymous" referrerpolicy="no-referrer" defer></script>
<script src="{KIT}/deck.js" defer></script>
<script src="{KIT}/presenter.js" defer></script>
</head>
<body>
<main class="deck" data-deck="acm-{DECK['date']}" data-ledger="{DECK['ledger']}">

''' + '\n'.join(S) + '</main>\n</body>\n</html>\n'
open(sys.argv[1], 'w').write(html)
print('slides', len(S), '->', sys.argv[1])
