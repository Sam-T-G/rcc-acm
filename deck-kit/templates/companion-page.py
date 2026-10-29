"""Companion page template. Copy this file next to your deck's generator, fill in every fill: line, then

    <venv with segno and markdown>/bin/python build.py
    node deck-kit/page/check-page.mjs site/decks/<slug>/index.html --shots /tmp/page-shots --click

Read deck-kit/page/README.md first. Publish the page to its own folder (decks/<slug>-<name>/), because
scripts/publish-deck.sh replaces decks/<slug>/ on every deck publish.
"""
import os
import sys

REPO = '/Users/sam/Documents/repositories/rcc-acm'          # fill: path to the repo on this machine
sys.path.insert(0, REPO + '/deck-kit/page')
from pagekit import (callout, card, cards, code, footer, mast, md, page, progress, reveal, reveals,  # noqa: E402
                     section, start_block, steps)

OUT = REPO + '/site/decks/fill-slug/index.html'             # fill: where the page is built
UPDATED = 'fill-date'                                        # fill: YYYY-MM-DD

TASKS = [  # fill: one entry per task, easiest first
    dict(title='fill: task title', goal='fill: what to do, in one plain sentence.',
         starter='// fill: starter code\n', hints=['fill: a hint'], answer='// fill: one answer\n'),
]


def task_card(k, t):
    body = (f'<p>{md(t["goal"])}</p>'
            + code(f'start-{k}', 'starter', t['starter'])
            + reveals(*[reveal('hint', f'<p>{md(h)}</p>', f'Hint {i}') for i, h in enumerate(t['hints'], 1)],
                      reveal('answer', code(f'answer-{k}', 'one answer', t['answer']))))
    return card(k, t['title'], body, cid=f'task-{k}')


body = (
    mast('fill: page title', 'fill: one line on what students do here.')
    + start_block('Start here', 'fill: the first action, in a few words.', 'fill: one line of detail, or leave empty.', '#tasks', 'fill: button words')
    + progress([(k, '', f'#task-{k}') for k in range(1, len(TASKS) + 1)], label='Your progress')
    + section('setup', 'Before you start', steps([md('fill: step one.'), md('fill: step two.')])
              + callout('warning', 'fill: label.', 'fill: the one thing that breaks if they skip it.'), eyebrow='Set up')
    + section('tasks', 'fill: tasks heading', cards([task_card(k, t) for k, t in enumerate(TASKS, 1)]), eyebrow='Step 1')
    + footer(['fill: where the facts on this page come from.'], UPDATED)
)

html = page('fill: Two To Four Words', 'fill: one sentence for the description.', body, UPDATED)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(html)
print('wrote', OUT)
