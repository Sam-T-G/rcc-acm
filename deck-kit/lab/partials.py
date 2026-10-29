"""Slide partials for ACM decks: whole slides built from the kit's existing kinds.

Each function returns one <section> string that passes deck-kit/check.mjs. They cover the
shapes the 2026-10 decks kept rebuilding by hand: a track picker, a QR handoff to a page,
safety rules, a work clock that ends at a set time, a round map, and a round's win slide.
Markup and styles: deck-kit/README.md, "Partials". qr() needs segno (pip install segno).

    import sys; sys.path.insert(0, '<repo>/deck-kit/lab')
    from partials import pick, sendoff, rules, work_clock, round_map, win, qr
"""
from html import escape


def _notes(note, bridge):
    ps = [note] if isinstance(note, str) and note else list(note or [])
    body = ''.join(f'<p>{p}</p>' for p in ps)
    if bridge:
        body += f'<p class="bridge">{bridge}</p>'
    return f'<aside class="notes">{body}</aside>' if body else ''


def _attrs(section=None, ground=None, room=False):
    a = f' data-section="{section}"' if section else ''
    a += f' data-ground="{ground}"' if ground else ''
    return a + (' data-room' if room else '')


def qr_svg(url):
    """The URL as an inline QR code (error level M), drawn as one path. Decode it once before trusting it."""
    import segno
    m = segno.make(url, error='m', micro=False).matrix
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
    return (f'<svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges">'
            f'<path fill="#ffffff" d="M0 0h{n}v{n}H0z"/><path stroke="#221f1e" d="{"".join(d)}"/></svg>')


def qr(url, label=None):
    """A linked QR tile with the URL printed under it (accessibility.md §1.7)."""
    label = label or url.removeprefix('https://').removeprefix('http://').rstrip('/')
    return f'<a class="qr" href="{url}"><span class="qr__tile">{qr_svg(url)}</span><span class="label">{_url_lines(label)}</span></a>'


def _url_lines(label, width=18):
    """Split a long URL label at its slashes into lines of about `width` characters, so it reads as a few
    whole pieces under the tile instead of wrapping mid-word. The text is unchanged (check.mjs strips whitespace)."""
    parts = [p + '/' for p in label.split('/')[:-1]] + [label.split('/')[-1]]
    lines, cur = [], ''
    for part in parts:
        if cur and len(cur) + len(part) > width:
            lines.append(cur)
            cur = ''
        cur += part
    lines.append(cur)
    return ''.join(f'<span class="qr__line">{escape(x)}</span>' for x in lines if x)


def pick(left, right, h2='Pick one for today', section=None, ground=None, note='', bridge=None):
    """Two equal track tiles. left and right are (label, text). Neither side is styled as the better one."""
    tiles = ''.join(f'<div><p class="label">{escape(l)}</p><p>{t}</p></div>' for l, t in (left, right))
    return (f'<section class="slide" data-kind="contrast" data-layout="tiles"{_attrs(section, ground)} aria-label="{escape(h2)}">\n'
            f'  <h2>{h2}</h2>\n  <div class="contrast contrast--even">{tiles}</div>\n  {_notes(note, bridge)}\n</section>\n')


def sendoff(eyebrow, h2, sub, url, label=None, section=None, ground=None, note='', bridge=None, room=True):
    """Hand a group off to a page: headline and one line on the left, a large QR with its URL on the right.
    The URL wraps under the tile at the ledger size, so the headline keeps its width."""
    # Kept in room mode by default, so late arrivals can still scan the page.
    return (f'<section class="slide" data-kind="signup" data-layout="sendoff"{_attrs(section, ground, room=room)} aria-label="{escape(h2)}">\n'
            f'  <div class="signup__main">\n    <p class="eyebrow">{eyebrow}</p>\n    <h2>{h2}</h2>\n    <p class="sub">{sub}</p>\n  </div>\n'
            f'  {qr(url, label)}\n  {_notes(note, bridge)}\n</section>\n')


def rules(eyebrow, h2, items, warn=None, section=None, ground=None, note='', bridge=None):
    """Up to three rules as beats, plus at most one Warning callout for the one that breaks hardware.
    The callout is the last beat, so it never shows before the rules it belongs to.
    items are (rule, detail) pairs; warn is one sentence or None."""
    assert len(items) <= (3 if warn else 4), 'rules: three items with a warning, four without'
    lis = ''.join(f'<li data-beat>{r}<span class="detail">{d}</span></li>' if d else f'<li data-beat>{r}</li>' for r, d in items)
    callout = f'\n  <p class="callout callout--warning" data-beat><b>Careful.</b> {warn}</p>' if warn else ''
    return (f'<section class="slide" data-kind="beats" data-layout="rules"{_attrs(section, ground, room=True)} aria-label="{escape(h2)}">\n'
            f'  <p class="eyebrow">{eyebrow}</p>\n  <h2>{h2}</h2>\n  <ol class="beats">{lis}</ol>{callout}\n  {_notes(note, bridge)}\n</section>\n')


def work_clock(h2, sub, ends='14:25', eyebrow=None, section=None, ground='orange', note='', bridge=None):
    """A clock that counts down to a wall-clock time today (data-ends), not a fixed length,
    so pressing T late never runs past the end. Stays up in room mode. Hint hides while it runs."""
    h, m = (int(x) for x in ends.split(':'))
    eb = eyebrow or f'Work time · until {h % 12 or 12}:{m:02d}'
    return (f'<section class="slide" data-kind="clock" data-ends="{ends}"{_attrs(section, ground, room=True)} aria-label="Work time">\n'
            f'  <p class="eyebrow">{eb}</p>\n  <h2>{h2}</h2>\n  <p class="sub">{sub}</p>\n  {_notes(note, bridge)}\n</section>\n')


def round_map(h2, rounds, current, eyebrow=None, sub=None, section=None, ground=None, note='', bridge=None):
    """Where the room is: every round as a numbered segment, done ones in ink, the current one in primary.
    rounds is a list of short names; current is 1-based."""
    lis = ''.join(f'<li class="{"is-done" if k < current else "is-current" if k == current else "is-next"}"><b>{k}</b><span>{escape(r)}</span></li>'
                  for k, r in enumerate(rounds, 1))
    eb = f'\n  <p class="eyebrow">{eyebrow or f"Round {current} of {len(rounds)}"}</p>'
    s = f'\n  <p class="sub">{sub}</p>' if sub else ''
    return (f'<section class="slide" data-kind="statement" data-layout="map"{_attrs(section, ground)} aria-label="{escape(h2)}">{eb}\n'
            f'  <h2>{h2}</h2>{s}\n  <ol class="roundmap" aria-label="Rounds">{lis}</ol>\n  {_notes(note, bridge)}\n</section>\n')


def win(h2, see, fixes=(), eyebrow='It works when', section=None, ground='orange', note='', bridge=None):
    """The end of a round: what a working build does, in one line, then up to three fixes for the usual misses.
    fixes are (problem, fix) pairs."""
    assert len(fixes) <= 3
    lis = ''.join(f'<li data-beat>{p}<span class="detail">{f}</span></li>' for p, f in fixes)
    ol = f'\n  <ol class="beats">{lis}</ol>' if fixes else ''
    return (f'<section class="slide" data-kind="beats" data-layout="win"{_attrs(section, ground)} aria-label="{escape(h2)}">\n'
            f'  <p class="eyebrow">{eyebrow}</p>\n  <h2>{h2}</h2>\n  <p class="sub">{see}</p>{ol}\n  {_notes(note, bridge)}\n</section>\n')
