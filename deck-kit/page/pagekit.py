"""ACM @ RCC page kit: helpers that build a companion page (the page students open beside a deck).

A page is one HTML file with everything inlined: the design system's tokens.css, viz.css, page.css,
and optionally labkit's lab_css() for breadboard drawings. Read README.md beside this file first.

    import sys; sys.path.insert(0, '<repo>/deck-kit/page')
    from pagekit import *
    body = mast('Build a parking gate', 'One line on what this page is.') + start_block(...) + ...
    open(out, 'w').write(page('Parking Gate Lab', 'One-sentence description.', body, updated='2026-10-28'))

Every helper returns an HTML string. Text arguments are plain text unless the name says html; md() turns
`code` and **bold** into markup for the few places that take a sentence.
"""
import html as _html
import os
import re

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(KIT + '/../..')
TOKENS = REPO + '/docs/04-brand/design-system/tokens.css'
MEETING = 'Thursdays 1:30 to 2:30 PM, BLCIS A-210'

__all__ = ['esc', 'md', 'page', 'mast', 'start_block', 'progress', 'section', 'steps', 'code', 'reveal', 'reveals',
           'card', 'cards', 'table', 'figure', 'io', 'qr', 'qr_svg', 'callout', 'footer']


def esc(s):
    return _html.escape(s, quote=True)


def md(s):
    """A sentence with `code` and **bold** in it, escaped."""
    s = esc(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)


def _css(name):
    return open(os.path.join(KIT, name)).read()


COPY_ICON = ('<svg class="pk-idle" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5">'
             '<rect x="6.5" y="6.5" width="10" height="11" rx="2"/><path d="M13.5 4.5v-1a1 1 0 0 0-1-1h-8a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h1"/></svg>'
             '<svg class="pk-done" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5">'
             '<path d="M4 10.5l4 4 8-9"/></svg>')

COPY_JS = '''
document.addEventListener('click', async (e) => {
  const b = e.target.closest('button[data-copy]');
  if (!b) return;
  const block = document.getElementById(b.dataset.copy);
  const text = block.dataset.cleanCode;
  const label = b.querySelector('.pk-copy__label');
  try { await navigator.clipboard.writeText(text); b.dataset.state = 'done'; label.textContent = 'Copied'; }
  catch {
    // No clipboard access: select the whole text (not the preview) in a textarea, so the student copies it by hand.
    let t = block.querySelector('textarea.pk-clean');
    if (!t) { t = document.createElement('textarea'); t.className = 'pk-clean'; t.readOnly = true; t.value = text;
              t.setAttribute('aria-label', 'The full code, selected'); block.appendChild(t); }
    t.focus(); t.select(); label.textContent = 'Press Cmd+C or Ctrl+C';
  }
  setTimeout(() => { b.dataset.state = ''; label.textContent = 'Copy'; }, 4000);
});
'''


def page(title, description, body, updated, lab_css='', lang='en'):
    """The whole document. title is the tab title (two to four words); lab_css is labkit.lab_css() when the page draws boards."""
    css = open(TOKENS).read()
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="pk-updated" content="{esc(updated)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&family=JetBrains+Mono:wght@400..700&display=swap">
<style>
/* tokens.css, inlined from docs/04-brand/design-system/ */
{css}
/* deck-kit/page/viz.css */
{_css('viz.css')}
{lab_css}
/* deck-kit/page/page.css */
{_css('page.css')}
</style>
</head>
<body>
<main class="acm-container acm-container--doc pk-page">
{body}
</main>
<script>{COPY_JS}</script>
</body>
</html>
'''


def mast(h1, lede, pic_html=''):
    """The top of the page: the Rail, the club name, the h1, one line under it, an optional header picture."""
    pic = f'<div class="pk-mast__pic">{pic_html}</div>' if pic_html else ''
    return (f'<header class="pk-mast"><div class="acm-rail"><p class="acm-ledger">ACM @ RCC</p>'
            f'<h1>{esc(h1)}</h1><p class="pk-lede">{md(lede)}</p></div>{pic}</header>')


def start_block(eyebrow, do, detail='', href=None, button=None, extra_html=''):
    """One action, above the fold, on the orange fill. do is the action in a few words; extra_html goes under the
    detail line (a code() block for a command, say)."""
    btn = f'<a class="acm-button" href="{esc(href)}">{esc(button)}</a>' if href and button else ''
    det = f'<p>{md(detail)}</p>' if detail else ''
    return f'<aside class="pk-start" aria-label="Start here"><p class="acm-ledger">{esc(eyebrow)}</p><p class="pk-start__do">{md(do)}</p>{det}{extra_html}{btn}</aside>'


def progress(items, label='Steps'):
    """A sticky strip of jump links. items: (number or short mark, words, '#anchor'); either may be empty."""
    def chip(n, t, h):
        num = f'<b>{esc(str(n))}</b>' if str(n) else ''
        return f'<li><a href="{esc(h)}">{num}{esc(t)}</a></li>'
    lis = ''.join(chip(n, t, h) for n, t, h in items)
    return f'<nav class="pk-progress" aria-label="{esc(label)}"><ol>{lis}</ol></nav>'


def section(sid, title, body_html, eyebrow='', intro=''):
    eb = f'<span class="acm-ledger">{esc(eyebrow)}</span>' if eyebrow else ''
    it = f'<p class="pk-intro">{md(intro)}</p>' if intro else ''
    return f'<section id="{esc(sid)}"><h2>{eb}{esc(title)}</h2>{it}{body_html}</section>'


def steps(items_html, start=1):
    """A numbered list of short steps. items_html: each item's HTML (use md() for plain sentences). start: the first
    number, so one sequence can continue after a table or a picture."""
    sa = f' start="{start}" style="counter-reset: pk-step {start - 1}"' if start != 1 else ''
    return f'<ol class="pk-steps"{sa}>' + ''.join(f'<li><p>{x}</p></li>' for x in items_html) + '</ol>'


def _lines(text, numbered):
    out = []
    for ln in text.split('\n'):
        out.append(f'<span class="pk-l">{esc(ln)}\n</span>' if numbered else esc(ln) + '\n')
    return ''.join(out).rstrip('\n')


def code(key, label, text, preview=None, mark=None, numbered=None):
    """A code block per components.md §7.11: a header row with the file label and a Copy button that copies
    the whole text from data-clean-code.

    preview: a list of 0-based line numbers. Then the block shows only those lines, wrapped so nothing is cut
    off on a phone, with the full listing one tap away. mark: a function(line) that picks lines to highlight
    in the preview (the lines a student edits)."""
    text = text.rstrip('\n')
    lines = text.split('\n')
    if numbered is None:
        numbered = len(lines) > 10
    head = (f'<div class="pk-code__head"><p class="acm-ledger">{esc(label)}</p>'
            f'<button class="pk-copy" type="button" data-copy="{esc(key)}" translate="no">{COPY_ICON}<span class="pk-copy__label">Copy</span></button></div>')
    full_cls = ' pk-code--numbered' if numbered else ''
    if preview is None:
        return (f'<div class="pk-code{full_cls}" id="{esc(key)}" data-clean-code="{esc(text)}">{head}'
                f'<pre><code>{_lines(text, numbered)}</code></pre></div>')
    shown, last = [], None
    for i in sorted(set(preview)):
        if last is not None and i != last + 1:
            shown.append('<span class="pk-gap">...</span>')
        ln = esc(lines[i])
        shown.append(f'<span class="pk-mark">{ln}</span>' if mark and mark(lines[i]) else ln)
        last = i
    pv = '\n'.join(shown)
    return (f'<div class="pk-code pk-code--preview" id="{esc(key)}" data-clean-code="{esc(text)}">{head}'
            f'<pre><code>{pv}</code></pre>'
            f'<details><summary>Show all {len(lines)} lines</summary>'
            f'<div class="pk-code{full_cls}"><pre><code>{_lines(text, numbered)}</code></pre></div></details></div>')


REVEAL_LABEL = {'starter': 'Starter code', 'hint': 'Hint', 'mistake': 'Common mistake', 'answer': 'Show an answer', 'more': 'More'}


def reveal(kind, body_html, label=None):
    """A closed block the student opens when they want it. kind: starter, hint, mistake, answer, more."""
    lab = label or REVEAL_LABEL[kind]
    return f'<details class="pk-reveal pk-reveal--{kind}"><summary>{esc(lab)}</summary><div>{body_html}</div></details>'


def reveals(*blocks):
    return '<div class="pk-reveals">' + ''.join(blocks) + '</div>'


def card(n, title, body_html, meta='', cid=None, title_html=None):
    """A numbered card. n is a short mark (1, 12, S); meta is one line under the title."""
    idattr = f' id="{esc(cid)}"' if cid else ''
    mt = f'<p class="pk-card__meta">{md(meta)}</p>' if meta else ''
    num = f'<span class="pk-card__n">{esc(str(n))}</span>' if n != '' else ''
    return (f'<li{idattr}><article class="acm-card"><div class="pk-card__head">{num}'
            f'<h3>{title_html or esc(title)}</h3></div>{mt}{body_html}</article></li>')


def cards(cards_html, ordered=True):
    tag = 'ol' if ordered else 'ul'
    return f'<{tag} class="pk-cards">' + ''.join(cards_html) + f'</{tag}>'


def table(head, rows, cls='', caption=''):
    """A table with column headers (th scope="col") and a tinted header row. Cells take md() sentences."""
    ths = ''.join(f'<th scope="col">{esc(h)}</th>' for h in head)
    trs = ''.join('<tr>' + ''.join(f'<td>{md(c)}</td>' for c in r) + '</tr>' for r in rows)
    cap = f'<caption class="acm-ledger">{esc(caption)}</caption>' if caption else ''
    return f'<div class="acm-table-scroll"><table class="{esc(cls)}">{cap}<thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'


def figure(svg_html, caption, board=False):
    """A picture with a caption. board=True is for a labkit board(): its viewBox widens to the left so the sensor
    that hangs past the board's edge fits without padding, and the picture can run the full width on a phone."""
    if board:
        svg_html = svg_html.replace('viewBox="0 0 760 560"', 'viewBox="-50 0 780 570"', 1)
    cls = 'pk-fig pk-fig--board' if board else 'pk-fig'
    return f'<figure class="{cls}">{svg_html}<figcaption>{md(caption)}</figcaption></figure>'


def io(inp, out, labels=('Input', 'Output')):
    return (f'<div class="pk-io"><div><p class="acm-ledger">{labels[0]}</p><pre><code>{esc(inp.rstrip())}</code></pre></div>'
            f'<div><p class="acm-ledger">{labels[1]}</p><pre><code>{esc(out.rstrip())}</code></pre></div></div>')


def callout(kind, label, body):
    """The closed set from components.md §7.7: note, warning, check."""
    return f'<div class="acm-callout acm-callout--{kind}" role="note"><p><b>{esc(label)}</b> {md(body)}</p></div>'


def qr_svg(url):
    import segno
    q = segno.make(url, error='m', micro=False)
    m = q.matrix
    n = len(m) + 4
    d = []
    for y, row in enumerate(m):
        x = 0
        while x < len(row):
            if row[x]:
                s = x
                while x < len(row) and row[x]:
                    x += 1
                d.append(f'M{s+2} {y+2.5}h{x-s}')
            else:
                x += 1
    # A QR tile stays dark-on-white in both themes so phones can read it.
    return (f'<svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges">'
            f'<path fill="#ffffff" d="M0 0h{n}v{n}H0z"/><path stroke="#221f1e" d="{"".join(d)}"/></svg>')


def qr(url, label):
    return f'<a class="pk-qr" href="{esc(url)}">{qr_svg(url)}<span class="acm-ledger">{esc(label)}</span></a>'


def footer(lines_html, updated):
    ps = ''.join(f'<p>{x}</p>' for x in lines_html)
    return (f'<footer class="pk-foot" role="contentinfo">{ps}<p>ACM @ RCC · {MEETING} · '
            f'Updated <time datetime="{esc(updated)}">{esc(updated)}</time></p></footer>')
