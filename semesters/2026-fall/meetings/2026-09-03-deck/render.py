#!/usr/bin/env python3
"""Render a single-file slide deck the way the Artifact host will, screenshot every slide, and audit it.

Usage:
  render.py DECK.html OUTDIR [--viewports 1920x1080,1280x720,1024x768] [--keys n,o] [--wait 450]

Conventions the deck must follow (mandated by the build spec):
  - a stage element with id="stage" that is 1920x1080 design px, scaled with transform to fit the viewport
  - one <section class="slide" id="..."> per slide inside the stage
  - hash routing: setting location.hash to "#<slide id>" shows that slide
  - the visible slide carries aria-current="true"

Outputs in OUTDIR:
  wrapped.html                 the deck wrapped in the host skeleton and reset (what is actually rendered)
  <WxH>/slide-NN-<id>.png      one screenshot per slide per viewport
  <WxH>/key-<k>-slide-01.png   screenshot after pressing key k on slide 1 (then pressed again to toggle back)
  audit.json, audit.md         findings: font-size floors, margin/stage overflow, forbidden colours,
                               gradients, console errors, slide count, external resources
"""
import json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HOST_WRAP_HEAD = ('<!doctype html><html><head><meta charset="utf-8">'
                  '<meta name="viewport" content="width=device-width,initial-scale=1">'
                  '<style>html{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif;background:#f7f7f5;color:#111}'
                  'img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
HOST_WRAP_TAIL = '</body></html>'

AUDIT_JS = r"""
(() => {
  const stage = document.getElementById('stage');
  if (!stage) return { error: 'no #stage element' };
  const sr = stage.getBoundingClientRect();
  const scale = sr.width / 1920;
  const slide = document.querySelector('section.slide[aria-current="true"]') || document.querySelector(location.hash ? 'section.slide' + location.hash : 'section.slide');
  if (!slide) return { error: 'no active slide' };
  const out = { id: slide.id, scale, texts: [], overflow: [], colors: [], gradients: [], small: [] };
  const seen = new Set();
  const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    // skip anything inside a hidden notes/overview layer
    if (el.closest('[hidden], [aria-hidden="true"], .notes, .overview, [data-layer="notes"], [data-layer="overview"]')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const px = parseFloat(cs.fontSize); // computed font-size is in untransformed layout px, i.e. design px already
    const rec = { text: t.slice(0, 60), tag: el.tagName.toLowerCase(), cls: el.className && el.className.baseVal !== undefined ? el.className.baseVal : (el.className || ''), px: Math.round(px * 10) / 10,
      left: Math.round((r.left - sr.left) / scale), top: Math.round((r.top - sr.top) / scale), right: Math.round((r.right - sr.left) / scale), bottom: Math.round((r.bottom - sr.top) / scale) };
    out.texts.push(rec);
    if (px < 40) out.small.push(rec);
    if (rec.left < 96 || rec.top < 96 || rec.right > 1920 - 96 || rec.bottom > 1080 - 96) {
      const kind = (rec.left < 0 || rec.top < 0 || rec.right > 1920 || rec.bottom > 1080) ? 'outside-stage' : 'inside-margin';
      out.overflow.push(Object.assign({ kind }, rec));
    }
    if (el.scrollWidth > el.clientWidth + 1 && cs.overflowX !== 'visible') out.overflow.push(Object.assign({ kind: 'clipped-x' }, rec));
  }
  // colours and gradients across every element in the slide (and the stage chrome)
  const all = [stage, ...stage.querySelectorAll('*')];
  const bad = ['rgb(1, 130, 172)'];
  for (const el of all) {
    const cs = getComputedStyle(el);
    for (const p of ['color', 'backgroundColor', 'borderTopColor', 'borderLeftColor', 'borderBottomColor', 'borderRightColor', 'outlineColor', 'fill', 'stroke']) {
      const v = cs[p];
      if (v && bad.includes(v)) out.colors.push({ prop: p, value: v, tag: el.tagName.toLowerCase(), cls: el.className && el.className.baseVal !== undefined ? el.className.baseVal : (el.className || '') });
    }
    const bi = cs.backgroundImage;
    if (bi && bi.includes('gradient')) out.gradients.push({ tag: el.tagName.toLowerCase(), cls: el.className && el.className.baseVal !== undefined ? el.className.baseVal : (el.className || ''), value: bi.slice(0, 120) });
    if (cs.webkitFontSmoothing === 'antialiased' && el === document.body) out.colors.push({ prop: 'webkitFontSmoothing', value: 'antialiased on body' });
  }
  return out;
})()
"""

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    deck = Path(args[0]).resolve(); outdir = Path(args[1]).resolve(); outdir.mkdir(parents=True, exist_ok=True)
    viewports = [(1920, 1080)]; keys = []; wait_ms = 450
    i = 2
    while i < len(args):
        if args[i] == '--viewports': viewports = [tuple(int(x) for x in v.split('x')) for v in args[i+1].split(',')]; i += 2
        elif args[i] == '--keys': keys = [k for k in args[i+1].split(',') if k]; i += 2
        elif args[i] == '--wait': wait_ms = int(args[i+1]); i += 2
        else: i += 1

    src = deck.read_text(encoding='utf-8')
    wrapped = outdir / 'wrapped.html'
    wrapped.write_text(HOST_WRAP_HEAD + src + HOST_WRAP_TAIL, encoding='utf-8')

    report = { 'deck': str(deck), 'bytes': len(src.encode('utf-8')), 'external': [], 'forbidden_tags': [], 'viewports': {}, 'console': [], 'pageerrors': [] }
    for m in re.finditer(r'(?:src|href)\s*=\s*["\']([^"\']+)["\']', src):
        u = m.group(1)
        if re.match(r'^(https?:)?//', u) and 'fonts.googleapis.com' not in u and 'fonts.gstatic.com' not in u:
            report['external'].append(u)
    for tag in ['<!doctype', '<html', '<head', '<body']:
        if tag in src.lower(): report['forbidden_tags'].append(tag)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for (w, h) in viewports:
            vdir = outdir / f'{w}x{h}'; vdir.mkdir(exist_ok=True)
            ctx = browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, color_scheme='light')
            page = ctx.new_page()
            page.on('console', lambda msg: report['console'].append({'type': msg.type, 'text': msg.text[:300]}) if msg.type in ('error', 'warning') else None)
            page.on('pageerror', lambda err: report['pageerrors'].append(str(err)[:300]))
            page.goto(wrapped.as_uri(), wait_until='load')
            try: page.wait_for_function("document.fonts && document.fonts.status === 'loaded'", timeout=8000)
            except Exception: pass
            page.wait_for_timeout(600)
            ids = page.evaluate("Array.from(document.querySelectorAll('section.slide[id]')).map(s => s.id)")
            vrep = { 'slides': [], 'count': len(ids) }
            for idx, sid in enumerate(ids, 1):
                page.evaluate(f"location.hash = '#{sid}'")
                page.wait_for_timeout(wait_ms)
                shot = vdir / f'slide-{idx:02d}-{sid}.png'
                page.screenshot(path=str(shot))
                audit = page.evaluate(AUDIT_JS)
                audit['shot'] = str(shot)
                vrep['slides'].append(audit)
            if ids and keys:
                page.evaluate(f"location.hash = '#{ids[0]}'"); page.wait_for_timeout(wait_ms)
                for k in keys:
                    page.keyboard.press(k); page.wait_for_timeout(wait_ms)
                    page.screenshot(path=str(vdir / f'key-{k}-slide-01.png'))
                    page.keyboard.press(k); page.wait_for_timeout(wait_ms)
                # keyboard navigation smoke test
                before = page.evaluate("location.hash")
                page.keyboard.press('ArrowRight'); page.wait_for_timeout(wait_ms)
                after = page.evaluate("location.hash")
                vrep['arrow_right_changes_hash'] = (before != after)
                page.keyboard.press('ArrowLeft'); page.wait_for_timeout(wait_ms)
                vrep['arrow_left_returns'] = (page.evaluate("location.hash") == before)
            report['viewports'][f'{w}x{h}'] = vrep
            ctx.close()
        browser.close()

    (outdir / 'audit.json').write_text(json.dumps(report, indent=1), encoding='utf-8')

    lines = [f"# Render audit for {deck.name}", '', f"Bytes: {report['bytes']}. External resources (must be empty): {report['external'] or 'none'}. Forbidden wrapper tags present: {report['forbidden_tags'] or 'none'}.", '']
    if report['pageerrors']: lines += ['## Page errors'] + [f'- {e}' for e in report['pageerrors']] + ['']
    if report['console']: lines += ['## Console warnings and errors'] + [f"- {c['type']}: {c['text']}" for c in report['console'][:40]] + ['']
    for vp, vrep in report['viewports'].items():
        lines += [f'## Viewport {vp}: {vrep["count"]} slides', '']
        if 'arrow_right_changes_hash' in vrep:
            lines += [f"Keyboard: ArrowRight changes hash = {vrep['arrow_right_changes_hash']}; ArrowLeft returns = {vrep['arrow_left_returns']}", '']
        for k, a in enumerate(vrep['slides'], 1):
            if a.get('error'): lines.append(f"- slide {k}: ERROR {a['error']}"); continue
            small = [s for s in a['small'] if s['px'] < 32]
            mid = [s for s in a['small'] if 32 <= s['px'] < 40]
            lines.append(f"- slide {k:02d} `{a['id']}`: scale {a['scale']:.3f}; text elements {len(a['texts'])}; below 32px: {len(small)}; 32 to 39.9px (must be ledger/footer/source only): {len(mid)}; margin/stage overflow: {len(a['overflow'])}; forbidden colours: {len(a['colors'])}; gradients: {len(a['gradients'])}")
            for s in small: lines.append(f"    - BELOW 32px: {s['px']}px <{s['tag']} class=\"{s['cls']}\"> \"{s['text']}\"")
            for s in mid: lines.append(f"    - 32-39px: {s['px']}px <{s['tag']} class=\"{s['cls']}\"> \"{s['text']}\"")
            for o in a['overflow']: lines.append(f"    - OVERFLOW {o['kind']}: <{o['tag']} class=\"{o['cls']}\"> \"{o['text']}\" box {o['left']},{o['top']} to {o['right']},{o['bottom']}")
            for c in a['colors']: lines.append(f"    - FORBIDDEN COLOUR {c}")
            for g in a['gradients']: lines.append(f"    - GRADIENT <{g['tag']} class=\"{g['cls']}\"> {g['value']}")
        lines.append('')
    (outdir / 'audit.md').write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
