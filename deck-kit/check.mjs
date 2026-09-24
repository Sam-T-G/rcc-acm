// Deck kit check. Headless Chrome over CDP, no dependencies (Node 22 global WebSocket).
// Ported 2026-09-24 from rcc-gdg/deck-kit/check.mjs onto the ACM slide rules.
//
//   node deck-kit/check.mjs <deck.html> [--shots <dir>]
//
// Serves the repo root on a free port, opens the deck, and fails on: fill markers
// or template tokens left in; token drift from tokens.css; structure (known kinds,
// one h1 and it is on the cover, beats and statements within their caps, clocks
// with timers); the ACM slide rules (assets.md §10.5, accessibility.md §2.4):
// "ACM @ RCC" as text on the first and last slide, the Rail exactly once and on
// the cover, one callout per slide, code twelve lines at most, no ACM Blue, no
// gradients, no font-variation-settings, no {} or <> outside code, no em dash
// inside a sentence, none of the banned words; type under the floors (72 / 40 /
// 32); content outside the 96 px margins or into the progress band; console
// errors. Then it walks the deck with real key presses in five modes: motion,
// reduced motion, GSAP blocked, no script, and a 390 px phone.
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, existsSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, relative, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, '..');
const args = process.argv.slice(2);
const deckArg = args.find((a) => !a.startsWith('--') && args[args.indexOf(a) - 1] !== '--shots');
if (!deckArg) { console.error('usage: node deck-kit/check.mjs <deck.html> [--shots <dir>]'); process.exit(2); }
const DECK = resolve(deckArg);
const SHOTS = args.includes('--shots') ? resolve(args[args.indexOf('--shots') + 1]) : null;
if (SHOTS) mkdirSync(SHOTS, { recursive: true });
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const NAME = 'ACM @ RCC';
const BANNED = ['seamless', 'comprehensive', 'robust', 'leverage', 'delve', 'showcase', 'elevate', 'unlock'];
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const fails = [], passes = [];
const fail = (m) => { fails.push(m); console.log('  FAIL ' + m); };
const pass = (m) => { passes.push(m); console.log('  ok   ' + m); };
const check = (cond, m) => (cond ? pass(m) : fail(m));

// ---------- Token drift: every custom property deck.css shares with tokens.css must match.
function props(css, selector) {
  const out = {};
  const re = new RegExp('(?:^|})\\s*' + selector.replace(/[[\]().*+?^$|\\]/g, '\\$&') + '\\s*\\{([^}]*)\\}', 'g');
  let m;
  while ((m = re.exec(css))) for (const d of m[1].matchAll(/(--acm-[\w-]+)\s*:\s*([^;]+);/g)) out[d[1]] = d[2].trim().replace(/\s+/g, ' ');
  return out;
}
console.log('tokens');
{
  const kitRaw = readFileSync(join(HERE, 'deck.css'), 'utf8');
  const kit = kitRaw.replace(/\/\*[\s\S]*?\*\//g, '');
  const src = readFileSync(join(ROOT, 'docs/04-brand/design-system/tokens.css'), 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
  const a = props(kit, ':root'), b = props(src, ':root');
  const shared = Object.keys(a).filter((k) => k in b && k !== '--acm-rail-w');
  const drift = shared.filter((k) => a[k] !== b[k]);
  check(shared.length > 20 && !drift.length, `:root: ${shared.length} shared tokens, ${drift.length} drifted${drift.length ? ' (' + drift.map((k) => `${k} ${a[k]} vs ${b[k]}`).join(', ') + ')' : ''}`);
  const own = Object.keys(a).filter((k) => !(k in b));
  check(own.every((k) => ['--acm-dur-beat', '--acm-dur-move', '--acm-ease-arrive'].includes(k)), `the kit adds only the logged slide-motion tokens (${own.join(', ') || 'none'})`);
  const deckSrc = readFileSync(DECK, 'utf8');
  check(!/font-variation-settings/.test(kit + deckSrc), 'no font-variation-settings anywhere (bright-lines.md §1.3)');
  check(!/gradient\(/.test(kit + deckSrc.replace(/<svg[\s\S]*?<\/svg>/g, '')), 'no gradients in the kit or the deck (bright-lines.md §1.3)');
  check(!/#0182ac/i.test(kit + deckSrc), 'no ACM Blue (#0182ac)');
}

// ---------- A static server over the repo root.
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp4': 'video/mp4', '.json': 'application/json' };
const server = createServer((req, res) => {
  const p = resolve(ROOT, '.' + decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!p.startsWith(ROOT) || !existsSync(p) || statSync(p).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'content-type': TYPES[extname(p)] || 'application/octet-stream' }); res.end(readFileSync(p));
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const URL0 = `http://127.0.0.1:${server.address().port}/${relative(ROOT, DECK).split('\\').join('/')}`;

// ---------- Chrome.
const port = 9400 + Math.floor(Math.random() * 400);
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'deck-cdp-'))}`,
  '--no-first-run', '--hide-scrollbars', '--force-color-profile=srgb', 'about:blank'], { stdio: 'ignore' });
let target;
for (let i = 0; i < 60 && !target; i++) {
  try { target = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((t) => t.type === 'page'); } catch { await sleep(200); }
}
if (!target) { console.error('Chrome did not start'); process.exit(2); }
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let seq = 0; const pending = new Map(); const events = [];
ws.addEventListener('message', (m) => {
  const msg = JSON.parse(m.data);
  if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg); pending.delete(msg.id); } else events.push(msg);
});
const send = (method, params = {}) => new Promise((ok, no) => {
  const n = ++seq; pending.set(n, (msg) => (msg.error ? no(new Error(method + ': ' + msg.error.message)) : ok(msg.result)));
  ws.send(JSON.stringify({ id: n, method, params }));
});
const evaluate = async (expr) => {
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || JSON.stringify(r.exceptionDetails));
  return r.result.value;
};
await send('Page.enable'); await send('Runtime.enable'); await send('Network.enable');
// Headless Chrome marks a page hidden after a real key event unless it is the
// front tab, and a hidden page gets no animation frames. Without these two
// lines every tween freezes and the next press fast-forwards it, so a walk can
// pass with no animation having run at all (found in the GDG kit, 2026-09-21).
await send('Page.bringToFront');
await send('Emulation.setFocusEmulationEnabled', { enabled: true });

async function load({ w = 1920, h = 1080, reduce = false, js = true, block = [] } = {}) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 600 });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: reduce ? 'reduce' : 'no-preference' }] });
  await send('Emulation.setScriptExecutionDisabled', { value: !js });
  await send('Network.setBlockedURLs', { urls: block });
  events.length = 0;
  await send('Page.navigate', { url: URL0 + '?fresh=' + Date.now() });
  for (let i = 0; i < 80; i++) { await sleep(100); try { if ((await evaluate('document.readyState')) === 'complete') break; } catch {} }
  await evaluate('document.fonts.ready.then(() => true)');
  await sleep(js ? 2600 : 400);          // the cover entrance runs about two seconds
}
function errors() {
  return events.filter((e) => (e.method === 'Runtime.exceptionThrown') || (e.method === 'Runtime.consoleAPICalled' && e.params.type === 'error'))
    .map((e) => e.params.exceptionDetails?.exception?.description || e.params.args?.map((a) => a.value).join(' ') || 'error');
}
async function key(k, code, vk) {
  const base = { key: k, code, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk };
  await send('Input.dispatchKeyEvent', { type: 'rawKeyDown', ...base });
  if (k.length === 1) await send('Input.dispatchKeyEvent', { type: 'char', text: k, ...base });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', ...base });
}
const KEYS = { right: ['ArrowRight', 'ArrowRight', 39], left: ['ArrowLeft', 'ArrowLeft', 37], home: ['Home', 'Home', 36], end: ['End', 'End', 35], five: ['5', 'Digit5', 53], t: ['t', 'KeyT', 84] };
const press = (name) => key(...KEYS[name]);
async function settle() { for (let i = 0; i < 60; i++) { if (!(await evaluate('window.__deck && window.__deck.state().busy'))) return; await sleep(50); } }
async function shot(name) {
  if (!SHOTS) return;
  const r = await send('Page.captureScreenshot', { format: 'png' });
  writeFileSync(join(SHOTS, name + '.png'), Buffer.from(r.data, 'base64'));
}

// ---------- Scaffold: a blank deck keeps its fill markers until a person decides.
console.log('scaffold');
{
  const src = readFileSync(DECK, 'utf8');
  const fills = src.match(/<!--\s*fill:[\s\S]*?-->/g) || [];
  const tokens = src.match(/@@[A-Z_]+@@/g) || [];
  check(!fills.length, `no fill markers left (${fills.length})${fills.length ? ': first is ' + fills[0].replace(/\s+/g, ' ').slice(0, 80) : ''}`);
  check(!tokens.length, `no template tokens left (${tokens.length})${tokens.length ? ': ' + tokens.slice(0, 3).join(' ') : ''}`);
  const tbd = (src.match(/\[TBD[^\]]*\]/g) || []).length;
  if (tbd) console.log(`  note ${tbd} [TBD] marker(s), informational`);
}

// ---------- Structure and the ACM slide rules, read from the live deck.
console.log('structure and slide rules');
await load();
const info = await evaluate(`(() => {
  const slides = [...document.querySelectorAll('.deck > .slide')];
  const text = (el) => { const c = el.cloneNode(true); c.querySelectorAll('.notes, .code, script, style').forEach((n) => n.remove()); return c.textContent.replace(/\\s+/g, ' ').trim(); };
  return slides.map((s, i) => ({
    i, kind: s.getAttribute('data-kind'), room: s.hasAttribute('data-room'),
    beats: s.querySelectorAll('.beats > li').length,
    words: s.getAttribute('data-kind') === 'statement' ? (s.querySelector('h2')?.textContent.trim().split(/\\s+/).length || 0) : 0,
    timer: +s.getAttribute('data-timer') || 0,
    h1: s.querySelectorAll('h1').length, h2: s.querySelectorAll('h2').length,
    rails: s.querySelectorAll('.cover__rail').length,
    callouts: s.querySelectorAll('.callout').length,
    codeLines: Math.max(0, ...[...s.querySelectorAll('.code')].map((c) => c.textContent.replace(/\\n$/, '').split('\\n').length)),
    look: [s.getAttribute('data-kind'), s.getAttribute('data-ground') || 'paper', s.getAttribute('data-layout') || ''].join('/'),
    ground: s.getAttribute('data-ground') || 'paper',
    imgs: [...s.querySelectorAll('img')].filter((im) => !im.closest('.qr')).map((im) => ({
      src: im.getAttribute('src').slice(0, 60), alt: im.getAttribute('alt') || '', wh: im.hasAttribute('width') && im.hasAttribute('height'),
      own: !!im.closest('.collage'), faces: im.getAttribute('data-faces') || '',
      credit: !!(im.closest('.collage') ? s.querySelector('.credit') : (im.closest('figure, li') || s).querySelector('.credit a[href]')), bytes: /^data:/.test(im.getAttribute('src')) ? im.getAttribute('src').length * 0.75 : -1 })),
    vids: [...s.querySelectorAll('video')].map((v) => ({ src: (v.getAttribute('src') || '').slice(0, 60), poster: !!v.getAttribute('poster'),
      flags: ['muted', 'loop', 'playsinline'].every((a) => v.hasAttribute(a)), autoplay: v.hasAttribute('autoplay'),
      play: v.getAttribute('data-play') || 'auto', wh: v.hasAttribute('width') && v.hasAttribute('height'),
      label: v.getAttribute('aria-label') || '', own: !!v.closest('.collage'), faces: v.getAttribute('data-faces') || '',
      bytes: /^data:/.test(v.getAttribute('src') || '') ? v.getAttribute('src').length * 0.75 : -1 })),
    name: [...s.querySelectorAll('.cover__name, .ask__name')].some((n) => n.textContent.trim() === ${JSON.stringify(NAME)}),
    text: text(s),
  }));
})()`);
const KINDS = ['cover', 'statement', 'contrast', 'beats', 'board', 'code', 'figure', 'clock', 'photo', 'grid', 'signup', 'collage', 'ask'];
check(info.every((s) => KINDS.includes(s.kind)), `every slide has a known data-kind (${info.length} slides)`);
check(info.reduce((a, s) => a + s.h1, 0) === 1 && info[0].h1 === 1, 'exactly one h1, on the cover (accessibility.md §1.5)');
check(info.every((s) => s.kind === 'cover' || s.h2 === 1), 'every other slide has one h2');
check(info[0].kind === 'cover' && info[info.length - 1].kind === 'ask', 'opens on the cover and ends on the ask');
check(info[0].name && info[info.length - 1].name, `"${NAME}" as text on the first and last slide (bright-lines.md §1.4)`);
check(info.reduce((a, s) => a + s.rails, 0) === 1 && info[0].rails === 1, 'the Rail once, on the title slide (assets.md §10.5)');
check(info.every((s) => s.callouts <= 1), 'at most one callout per slide');
check(info.every((s) => s.kind !== 'beats' || s.beats <= 4), 'every beats slide has four items or fewer');
check(info.every((s) => s.kind !== 'statement' || s.words <= 14), 'every statement is fourteen words or fewer');
check(info.every((s) => s.kind !== 'clock' || s.timer > 0), 'every clock slide has a data-timer');
check(info.every((s) => s.codeLines <= 12), 'code is twelve lines or fewer');
const same = info.findIndex((s, k) => k >= 2 && s.look === info[k - 1].look && s.look === info[k - 2].look);
check(same < 0, `no three slides in a row look the same (kind, ground, layout)${same >= 0 ? ': slides ' + (same - 1) + ' to ' + (same + 1) + ' are all ' + info[same].look : ''}`);
const imgs = info.flatMap((s) => s.imgs.map((m) => ({ ...m, i: s.i + 1 })));
if (imgs.length) {
  check(imgs.every((m) => m.alt.trim() && !/\[TBD/.test(m.alt)), `every photo has real alt text${imgs.filter((m) => !m.alt.trim() || /\[TBD/.test(m.alt)).map((m) => ' (slide ' + m.i + ')').join('')}`);
  check(imgs.every((m) => m.wh), 'every photo has width and height');
  const own = imgs.filter((m) => m.own);
  if (own.length) check(own.every((m) => m.faces === 'none' || m.faces === 'consented'), `every club photo says data-faces="none" or "consented" (public page; accessibility.md §2.2)${own.filter((m) => !['none', 'consented'].includes(m.faces)).map((m) => ' (slide ' + m.i + ' ' + m.src + ')').join('')}`);
  check(imgs.every((m) => m.credit), `every photo shows a linked credit on its slide${imgs.filter((m) => !m.credit).map((m) => ' (slide ' + m.i + ' ' + m.src + ')').join('')}`);
  const sizes = await Promise.all(imgs.map((m) => m.bytes >= 0 ? m.bytes : fetch(new URL(m.src, URL0)).then((r) => r.arrayBuffer()).then((b) => b.byteLength).catch(() => 0)));
  check(sizes.every((b) => b < 700 * 1024), `every photo is under 700 KB (largest ${Math.round(Math.max(...sizes) / 1024)} KB); fetch-image.mjs sizes them`);
}
const qrText = await evaluate(`[...document.querySelectorAll('a.qr')].map((a) => ({ href: a.getAttribute('href'), label: (a.querySelector('.label') || {}).textContent || '' }))`);
if (qrText.length) check(qrText.every((q) => q.label.replace(/\s+/g, '').includes(q.href.replace(/^https?:\/\//, '').replace(/\/$/, ''))), 'every QR code has its URL printed beside it (accessibility.md §1.7)');
const vids = info.flatMap((s) => s.vids.map((v) => ({ ...v, i: s.i + 1 })));
if (vids.length) {
  check(vids.every((v) => v.poster && v.flags && !v.autoplay && v.wh), 'every video has a poster, width, height, muted, loop, playsinline, and no autoplay attribute (the engine plays it)');
  check(vids.every((v) => ['auto', 'press'].includes(v.play)), 'every video says data-play="auto" or "press"');
  check(vids.every((v) => v.label.trim() && !/\[TBD/.test(v.label)), 'every video has a real aria-label');
  check(vids.filter((v) => v.own).every((v) => ['none', 'consented'].includes(v.faces)), 'every club video says data-faces="none" or "consented"');
  const vb = await Promise.all(vids.map((v) => v.bytes >= 0 ? v.bytes : fetch(new URL(v.src, URL0)).then((r) => r.arrayBuffer()).then((b) => b.byteLength).catch(() => 0)));
  check(vb.every((b) => b > 0 && b < 1024 * 1024), `every video loads and is under 1 MB so it can be inlined (largest ${Math.round(Math.max(...vb) / 1024)} KB); encode-video.swift sizes it`);
}
const glyph = info.filter((s) => /[{}<>]/.test(s.text));
check(!glyph.length, `no {} or <> glyphs outside code${glyph.length ? ' (slide ' + glyph.map((s) => s.i + 1).join(', ') + ')' : ''}`);
const dash = info.filter((s) => /\S\s*\u2014\s*\S/.test(s.text));
check(!dash.length, `no em dash inside a sentence${dash.length ? ' (slide ' + dash.map((s) => s.i + 1).join(', ') + ')' : ''}`);
const banned = info.flatMap((s) => BANNED.filter((w) => new RegExp('\\b' + w, 'i').test(s.text)).map((w) => `${s.i + 1}:${w}`));
check(!banned.length, `none of the banned words${banned.length ? ' (' + banned.join(', ') + ')' : ''}`);
const blue = await evaluate(`[...document.querySelectorAll('.deck *')].filter((el) => { const c = getComputedStyle(el); return [c.color, c.backgroundColor, c.fill, c.stroke].includes('rgb(1, 130, 172)'); }).length`);
check(blue === 0, 'no element renders in ACM Blue');

// ---------- Floors and overflow, on every slide with every beat showing.
console.log('floors and overflow (1920 x 1080, every beat revealed)');
const layout = await evaluate(`(() => {
  const deck = document.querySelector('.deck'), u = deck.clientWidth / 1920, dr = deck.getBoundingClientRect();
  const slides = [...deck.querySelectorAll(':scope > .slide')], out = [];
  const LEDGER = '.eyebrow, .label, .ledger, .counter, .ask__stamp, .credit';
  const cv = document.createElement('canvas').getContext('2d', { willReadFrequently: true });
  const rgba = (c) => { cv.clearRect(0, 0, 1, 1); cv.fillStyle = '#000'; cv.fillStyle = c; cv.fillRect(0, 0, 1, 1); return [...cv.getImageData(0, 0, 1, 1).data]; };
  const lum = (c) => { const m = rgba(c); return [0, 1, 2].map((k) => { const v = m[k] / 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }).reduce((a, v, k) => a + v * [0.2126, 0.7152, 0.0722][k], 0); };
  const bgOf = (el) => { for (let e = el; e; e = e.parentElement) { const c = getComputedStyle(e).backgroundColor; if (rgba(c)[3] > 128) return c; } return 'rgb(255,255,255)'; };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  slides.forEach((s, i) => {
    slides.forEach((o) => o.classList.toggle('is-current', o === s));
    // Presenting, the ground is on the stage: set it for this slide, with no fade.
    deck.style.transition = 'none'; deck.setAttribute('data-ground', s.getAttribute('data-ground') || 'paper');
    s.querySelectorAll('[data-beat]').forEach((b) => b.classList.remove('is-pending'));
    const low = [], outside = [], band = [], dim = [], over = [];
    const photos = [...s.querySelectorAll('img, video')].filter((im) => !im.closest('.qr')).map((im) => im.getBoundingClientRect());
    for (const el of s.querySelectorAll('*')) {
      if (el.closest('.notes, .visually-hidden, svg') || getComputedStyle(el).visibility === 'hidden') continue;
      const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim());
      if (own) {
        const fs = parseFloat(getComputedStyle(el).fontSize) / u;
        const min = el.closest('h1, h2') ? 72 : el.closest(LEDGER) ? 32 : 40;
        if (fs < min - 0.5) low.push((el.getAttribute('class') || el.tagName) + ' ' + fs.toFixed(0) + ' < ' + min);
        const cr = ratio(getComputedStyle(el).color, bgOf(el));
        if (cr < 4.5) dim.push((el.getAttribute('class') || el.tagName) + ' ' + cr.toFixed(2) + ':1');
        const tr = el.getBoundingClientRect();
        if (photos.some((p) => tr.left < p.right && tr.right > p.left && tr.top < p.bottom && tr.bottom > p.top)) over.push(el.getAttribute('class') || el.tagName);
      }
      if (!own && !el.matches('img, video, .qr__tile, .clock__track, .cover__rail, .code, .callout')) continue;
      // A bleeding photo runs off the stage edge on purpose (decision log, 2026-09-24).
      if (el.matches('.slide[data-kind="photo"]:not([data-layout="framed"]) .photo :is(img, video)')) continue;
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const y1 = (r.bottom - dr.top) / u, x1 = (r.right - dr.left) / u, y0 = (r.top - dr.top) / u, x0 = (r.left - dr.left) / u;
      if (x0 < 95 || x1 > 1825 || y0 < 95 || y1 > 985) outside.push((el.getAttribute('class') || el.tagName) + ' [' + x0.toFixed(0) + ',' + y0.toFixed(0) + ' ' + x1.toFixed(0) + ',' + y1.toFixed(0) + ']');
      // The progress line sits at 970 to 1030; the cover has none.
      if (s.dataset.kind !== 'cover' && y1 > 960) band.push((el.getAttribute('class') || el.tagName) + ' bottom ' + y1.toFixed(0));
    }
    out.push({ i, kind: s.dataset.kind, low, outside, band, dim, over });
  });
  return out;
})()`);
layout.forEach((s) => {
  check(!s.low.length, `slide ${s.i + 1} (${s.kind}): type at or above the floors${s.low.length ? ': ' + s.low.slice(0, 3).join('; ') : ''}`);
  check(!s.outside.length, `slide ${s.i + 1} (${s.kind}): inside the 96 px margins${s.outside.length ? ': ' + s.outside.slice(0, 3).join('; ') : ''}`);
  check(!s.dim.length, `slide ${s.i + 1} (${s.kind}): every text pair at 4.5:1 or better${s.dim.length ? ': ' + s.dim.slice(0, 3).join('; ') : ''}`);
  check(!s.over.length, `slide ${s.i + 1} (${s.kind}): no text over a photo${s.over.length ? ': ' + s.over.slice(0, 3).join('; ') : ''}`);
  check(!s.band.length, `slide ${s.i + 1} (${s.kind}): clear of the progress band${s.band.length ? ': ' + s.band.slice(0, 3).join('; ') : ''}`);
});

// ---------- Walk the deck with real key presses, in each mode.
const sections = await evaluate('new Set(__deck.slides.filter((s) => s.kind !== "cover").map((s) => s.section)).size');
async function walk(label, opts, expect) {
  console.log(label);
  await load(opts);
  if (!opts.js && opts.js !== undefined) {
    const n = await evaluate('[...document.querySelectorAll(".deck > .slide")].filter((s) => s.getBoundingClientRect().height > 0).length');
    check(n === info.length, `no script: all ${info.length} slides render as a readable stack (${n})`);
    await shot(label.replace(/\W+/g, '-') + '-stack');
    check(!errors().length, 'no console errors');
    return;
  }
  const st0 = await evaluate('__deck.state()');
  check(st0.presenting === expect.presenting, `presenting: ${st0.presenting}`);
  if (!expect.presenting) {
    const hidden = await evaluate('[...document.querySelectorAll("[data-beat]")].filter((b) => getComputedStyle(b).visibility === "hidden").length');
    check(hidden === 0, 'stacked: every beat is showing');
    const wide = await evaluate('document.documentElement.scrollWidth > window.innerWidth');
    check(!wide, 'stacked: no horizontal scroll');
    await shot(label.replace(/\W+/g, '-') + '-stack');
    check(!errors().length, `no console errors${errors().length ? ': ' + errors()[0] : ''}`);
    return;
  }
  check(st0.gsap === expect.gsap, `GSAP loaded: ${st0.gsap}`);
  if (expect.midflight) {
    const drawn = await evaluate(`(() => { const r = document.querySelector('.cover__rail'); return r ? r.getBoundingClientRect().height / (document.querySelector('.deck').clientWidth / 1920) : 0; })()`);
    check(drawn > 800, `after the opening, the cover Rail is drawn full height (${drawn.toFixed(0)} stage px)`);
  }
  await shot(label.replace(/\W+/g, '-') + '-00');
  if (expect.midflight && info[0].kind === 'cover') {
    // Sample the opening move mid-flight: the Rail must be caught retracting, not jumping.
    await press('right'); await sleep(380);
    const mid = await evaluate('__deck.state()');
    check(mid.busy && mid.rail.t > 0.05 && mid.rail.t < 0.98, `leaving the cover is a move over time (t = ${mid.rail.t.toFixed(2)} at 380 ms)`);
    await shot(label.replace(/\W+/g, '-') + '-open-mid');
    await settle();
    await press('left'); await settle();
  }
  if (expect.midflight) {
    // Grounds crossfade: partway through a move onto a new ground, the stage is between the two.
    const pair = await evaluate(`(() => { const g = (s) => s.getAttribute('data-ground') || 'paper'; const S = [...document.querySelectorAll('.deck > .slide')];
      for (let k = 1; k + 1 < S.length; k++) if (g(S[k]) !== g(S[k + 1]) && !S[k].querySelector('[data-beat]')) return k; return -1; })()`);
    if (pair > 0) {
      await evaluate(`location.hash = '#${pair + 1}'`); await sleep(1200); await settle();
      const a = await evaluate('getComputedStyle(document.querySelector(".deck")).backgroundColor');
      await press('right'); await sleep(200);
      const m = await evaluate('getComputedStyle(document.querySelector(".deck")).backgroundColor');
      await settle(); await sleep(900);
      const z = await evaluate('getComputedStyle(document.querySelector(".deck")).backgroundColor');
      check(a !== z && m !== a && m !== z, `grounds crossfade (slide ${pair + 1} to ${pair + 2}: ${a} -> ${m} -> ${z})`);
      await press('home'); await settle(); await sleep(900);
    }
  }
  const vAt = info.findIndex((s) => s.vids.some((v) => v.play === 'auto'));
  if (vAt >= 0 && expect.presenting) {
    await evaluate(`location.hash = '#1'`); await sleep(200); await settle();
    await evaluate(`location.hash = '#${vAt + 1}'`); await sleep(1500); await settle();
    const t0 = await evaluate(`document.querySelectorAll('.deck > .slide')[${vAt}].querySelector('video').currentTime`);
    await sleep(800);
    const t1 = await evaluate(`document.querySelectorAll('.deck > .slide')[${vAt}].querySelector('video').currentTime`);
    const on = (await evaluate('__deck.state()')).playing[vAt];
    if (opts.reduce) check(!on && t1 === t0, `reduced motion: the auto video on slide ${vAt + 1} stays on its poster`);
    else check(on > 0 && t1 > t0, `the auto video on slide ${vAt + 1} plays on arrival (t ${t0.toFixed(2)} -> ${t1.toFixed(2)})`);
    await press('right'); await settle(); await sleep(300);
    const off = await evaluate(`document.querySelectorAll('.deck > .slide')[${vAt}].querySelector('video').paused`);
    check(off, `leaving slide ${vAt + 1} pauses its video`);
    await press('home'); await settle(); await sleep(900);
  }
  const seen = [], total = (await evaluate('__deck.slides')).reduce((a, s) => a + 1 + s.beats, 0);
  for (let k = 0; k < total + 2; k++) {
    await press('right'); await settle();
    const st = await evaluate('__deck.state()');
    seen.push(st.last);
    if (SHOTS && expect.shots) await shot(label.replace(/\W+/g, '-') + '-' + String(k + 1).padStart(2, '0'));
  }
  const end = await evaluate('__deck.state()');
  check(end.i === info.length - 1 && end.pos === end.count - 1, `ArrowRight x${total + 2} reaches the last slide (${end.i + 1}/${info.length})`);
  check(Math.abs(end.rail.frac - 1) < 1e-6 && end.rail.t === 1, 'the progress line is full on the last slide');
  if (expect.kinds) {
    const plan = await evaluate('__deck.slides');
    const sameSection = plan.some((s, k) => k > 1 && s.section === plan[k - 1].section);
    const want = expect.kinds.filter((k) => k !== 'turn' || sections > 1).filter((k) => k !== 'ascend' || sameSection)
      .filter((k) => k !== 'hold' || plan.some((s) => s.beats));
    for (const k of want) check(seen.some((s) => s.startsWith(k)), `derived a ${k} transition`);
  }
  if (expect.onlyCut) check(seen.every((s) => s.startsWith('cut')), `every transition was a cut (${[...new Set(seen)].join(', ')})`);
  for (let k = 0; k < total + 2; k++) { await press('left'); await settle(); }
  const back = await evaluate('__deck.state()');
  check(back.i === 0 && back.b === 0, 'ArrowLeft all the way back lands on slide 1, beat 0');
  if (info[0].kind === 'cover') {
    const full = await evaluate(`(() => { const r = document.querySelector('.cover__rail'); return r.getBoundingClientRect().height / (document.querySelector('.deck').clientWidth / 1920); })()`);
    check(back.rail.t === 0 && back.rail.draw === 1 && full > 800, `back on the cover, the Rail is full height again (${full.toFixed(0)} stage px)`);
  }
  // A burst of presses faster than any transition: every press has to count.
  const plan = await evaluate('__deck.slides');
  let ei = 0, eb = 0;
  for (let k = 0; k < 6; k++) { if (eb < plan[ei].beats) eb++; else if (ei + 1 < plan.length) { ei++; eb = 0; } }
  for (let k = 0; k < 6; k++) await press('right');
  await settle();
  const burst = await evaluate('__deck.state()');
  check(!burst.busy && burst.i === ei && burst.b === eb, `six presses in a burst land exactly six steps on (slide ${burst.i + 1} beat ${burst.b}, expected slide ${ei + 1} beat ${eb})`);
  // Room mode, when the deck marks any room slides.
  const rooms = info.filter((s) => s.room).length;
  if (rooms) {
    await press('home'); await settle(); await press('five'); await settle();
    const room = await evaluate('__deck.state()');
    check(room.room && room.count === rooms, `room mode shows ${rooms} slides (${room.count})`);
    for (let k = 0; k < 8; k++) { await press('right'); await settle(); }
    check((await evaluate('__deck.state()')).last.startsWith('cut'), 'room mode transitions are cuts');
    await press('five'); await settle();
  }
  // Enter on the focused QR link belongs to the link, not the deck.
  if (await evaluate('!!document.querySelector("a.qr")')) {
    // Go to the slide that holds the link, from somewhere else, so the hash really changes.
    await evaluate(`location.hash = '#1'`); await sleep(200); await settle();
    const qrAt = await evaluate(`[...document.querySelectorAll('.deck > .slide')].findIndex((s) => s.querySelector('a.qr'))`);
    await evaluate(`location.hash = '#${qrAt + 1}'`);
    // Wait until the deck is really there: a hashchange can land after a fixed sleep.
    for (let k = 0; k < 40 && (await evaluate('__deck.state().i')) !== qrAt; k++) await sleep(50);
    await settle();
    const before = (await evaluate('__deck.state()')).i;
    check(before === qrAt, `the walk reached the QR slide ${qrAt + 1} (on ${before + 1})`);
    await evaluate(`(() => { const a = document.querySelector('.slide.is-current a.qr'); a.addEventListener('click', (e) => { e.preventDefault(); window.__qrClicked = true; }, { once: true }); a.focus(); })()`);
    const focused = await evaluate('document.activeElement && document.activeElement.matches("a.qr")');
    await key('Enter', 'Enter', 13); await settle();
    const after = await evaluate('({ i: __deck.state().i, clicked: !!window.__qrClicked })');
    check(focused && after.clicked && after.i === before, `Enter on the focused QR link follows the link and does not move the deck (focused ${focused}, clicked ${after.clicked}, slide ${before + 1} -> ${after.i + 1})`);
  }
  check(!errors().length, `no console errors${errors().length ? ': ' + errors()[0] : ''}`);
}

await walk('motion (GSAP, 1920 x 1080)', { w: 1920, h: 1080 }, { presenting: true, gsap: true, kinds: ['unfold', 'ascend', 'turn', 'hold'], shots: true, midflight: true });
await walk('reduced motion', { w: 1440, h: 900, reduce: true }, { presenting: true, gsap: true, onlyCut: true });
await walk('GSAP blocked (offline fallback)', { w: 1280, h: 800, block: ['*cdnjs.cloudflare.com*'] }, { presenting: true, gsap: false });
await walk('no script', { w: 1280, h: 800, js: false }, {});
await walk('phone 390', { w: 390, h: 844 }, { presenting: false });

// ---------- Timer: T starts it, a transition during a run is a cut.
const clockAt = info.findIndex((s) => s.timer > 0);
if (clockAt >= 0) {
  console.log('clock');
  await load();
  await evaluate(`location.hash = '#${clockAt + 1}'`); await sleep(300);
  await press('t'); await sleep(1300);
  const txt = await evaluate(`document.querySelectorAll('.deck > .slide')[${clockAt}].querySelector('.clock__digits').textContent`);
  const state = await evaluate(`document.querySelectorAll('.deck > .slide')[${clockAt}].querySelector('.clock').dataset.state`);
  check(state === 'running' && txt !== fmt(info[clockAt].timer), `T starts the clock (${state}, ${txt})`);
  await press('right'); await settle();
  check((await evaluate('__deck.state()')).last.startsWith('cut'), 'leaving a slide with a running clock is a cut');
}
function fmt(s) { return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); }

ws.close(); chrome.kill(); server.close();
console.log(`\n${passes.length} passed, ${fails.length} failed${SHOTS ? '. Screenshots in ' + SHOTS : ''}`);
process.exit(fails.length ? 1 : 0);
