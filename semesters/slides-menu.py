"""Build the ACM @ RCC slides menu: this week's deck on top, every earlier deck under it.

Served at https://sam-t-g.github.io/rcc-acm/slides/ (the root redirects there).
Each week: add the new deck as the FIRST row of DECKS, then rebuild and publish:

    python3 semesters/slides-menu.py
    node deck-kit/page/check-page.mjs site/slides/index.html --shots /tmp/slides-shots
    (push site/slides/index.html to gh-pages slides/index.html)

The first row is always shown as "This week". Links are relative to /slides/.
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'deck-kit', 'page'))
from pagekit import page, mast, start_block, section, card, cards, footer, esc  # noqa: E402

UPDATED = '2026-11-19'

# (date shown, title from the deck's cover, what it covered, [(link text, path under the site root)])
DECKS = [
    ('Thu Nov 19', 'What can we build with what we have?',
     'Spring project ideas: the parts we own, five projects they can start, and parts to buy.',
     [('Slides', 'decks/2026-11-19/')]),
    ('Thu Oct 29', 'Solve a contest problem, or build a parking gate',
     'Two tracks: ICPC practice problems on Kattis, or a parking garage gate on the Arduino.',
     [('Slides', 'decks/2026-10-29/'), ('ICPC practice page', 'decks/2026-10-29-icpc/'), ('Parking gate lab', 'decks/2026-10-29-gate/')]),
    ('Thu Oct 15', 'From your laptop to a moving arm',
     'Uploading code to the Arduino, and a transistor switch that runs a fan.',
     [('Slides', 'decks/2026-10-15/')]),
    ('Thu Oct 8', 'A feed that never ends, and your first Arduino build',
     'How infinite scroll works, then a servo and a button on the Arduino, step by step.',
     [('Slides', 'decks/2026-10-08/')]),
    ('Thu Oct 1', 'From one app to a hundred careers',
     "How Instagram's feed, Reels, and who-to-follow work, and a map of tech jobs.",
     [('Slides', 'decks/2026-10-01/')]),
    ('Thu Sep 24', 'Come build with us',
     'Tech roles, and sample ICPC problems.',
     [('Slides', 'decks/2026-09-24/')]),
]


def links(items):
    return '<p class="sm-links">' + ' · '.join(f'<a href="../{esc(p)}">{esc(t)}</a>' for t, p in items) + '</p>'


def build():
    now = DECKS[0]
    date, title, what, items = now
    extra = links(items[1:]) if len(items) > 1 else ''
    top = start_block(f'This week · {date}', title, what, href=f'../{items[0][1]}', button='Open the slides', extra_html=extra)
    rows = [card('', t, links(i), meta=f'{d} · {w}') for d, t, w, i in DECKS[1:]]
    body = (mast('Meeting slides', "This week's deck first, then every meeting before it.")
            + top
            + section('earlier', 'Earlier meetings', cards(rows, ordered=False), eyebrow='Fall 2026')
            + footer(['Open any deck and press the arrow keys to move through it.'], UPDATED))
    html = page('ACM Slides', "ACM @ RCC meeting slides, Fall 2026: this week's deck and every earlier one.", body, UPDATED)
    html = html.replace('</style>', '.sm-links { margin-block-start: var(--acm-space-2); font-weight: var(--acm-weight-strong); }\n</style>', 1)
    out = os.path.join(REPO, 'site', 'slides', 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(html)
    print('wrote', out)


if __name__ == '__main__':
    build()
