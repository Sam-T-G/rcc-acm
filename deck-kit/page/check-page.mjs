// Page kit check. Headless Chrome over CDP, no dependencies (Node 22 global WebSocket), same approach as
// deck-kit/check.mjs.
//
//   node deck-kit/page/check-page.mjs <page.html> [--shots <dir>] [--click]
//
// Fails on: token drift from tokens.css; duplicate ids; text under the page floor (13 px, the smallest
// documented role in running text); text below 4.5:1 (3:1 at 24 px, or 18.66 px at weight 700) against its
// real background, in light AND dark; horizontal page scroll at 390 px and 1280 px; console errors.
// --shots writes full-page screenshots at 1280 and 390, light and dark (headless screenshots taken after a
// scroll come out blank, so these are full-page captures instead).
// --click presses the first Copy button with a real mouse event and checks the clipboard got the whole text.
import { spawn } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, '../..');
const args = process.argv.slice(2);
const file = args.find((a, i) => !a.startsWith('--') && args[i - 1] !== '--shots');
if (!file) { console.error('usage: node deck-kit/page/check-page.mjs <page.html> [--shots <dir>] [--click]'); process.exit(2); }
const PAGE = resolve(file);
const SHOTS = args.includes('--shots') ? resolve(args[args.indexOf('--shots') + 1]) : null;
if (SHOTS) mkdirSync(SHOTS, { recursive: true });
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const fails = [];
const check = (ok, m) => { console.log((ok ? '  ok   ' : '  FAIL ') + m); if (!ok) fails.push(m); };

// ---------- Static checks
const src = readFileSync(PAGE, 'utf8');
function props(css) {
  const out = {};
  for (const m of css.replace(/\/\*[\s\S]*?\*\//g, '').matchAll(/(?:^|})\s*:root\s*\{([^}]*)\}/g))
    for (const d of m[1].matchAll(/(--acm-[\w-]+)\s*:\s*([^;]+);/g)) if (!(d[1] in out)) out[d[1]] = d[2].trim().replace(/\s+/g, ' ');
  return out;
}
console.log('static');
{
  const tokens = props(readFileSync(join(ROOT, 'docs/04-brand/design-system/tokens.css'), 'utf8'));
  const css = [...src.matchAll(/<style>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');
  const mine = props(css);
  const shared = Object.keys(mine).filter((k) => k in tokens);
  const drift = shared.filter((k) => mine[k] !== tokens[k]);
  check(shared.length > 100 && !drift.length, `tokens: ${shared.length} shared with tokens.css, ${drift.length} drifted${drift.length ? ': ' + drift.join(', ') : ''}`);
  const own = Object.keys(mine).filter((k) => !(k in tokens));
  check(!own.length, `no --acm-* token the system does not define${own.length ? ': ' + own.join(', ') : ''}`);
  const ids = [...src.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]);
  const dup = [...new Set(ids.filter((x, i) => ids.indexOf(x) !== i))];
  check(!dup.length, `${ids.length} ids, all unique${dup.length ? ' (dup: ' + dup.join(', ') + ')' : ''}`);
  check(!/font-variation-settings/.test(css), 'no font-variation-settings');
  check(!/#0182ac/i.test(src), 'no ACM Blue');
}

// ---------- Chrome
const port = 9800 + Math.floor(Math.random() * 150);
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'page-cdp-'))}`,
  '--no-first-run', '--hide-scrollbars', '--force-color-profile=srgb', 'about:blank'], { stdio: 'ignore' });
let target;
for (let i = 0; i < 60 && !target; i++) { try { target = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((t) => t.type === 'page'); } catch { await sleep(200); } }
if (!target) { console.error('Chrome did not start'); process.exit(2); }
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let seq = 0; const pending = new Map(); const events = [];
ws.addEventListener('message', (m) => { const msg = JSON.parse(m.data); if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg); pending.delete(msg.id); } else events.push(msg); });
const send = (method, params = {}) => new Promise((ok, no) => { const n = ++seq; pending.set(n, (msg) => (msg.error ? no(new Error(method + ': ' + msg.error.message)) : ok(msg.result))); ws.send(JSON.stringify({ id: n, method, params })); });
const evaluate = async (expr) => { const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true, userGesture: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || 'eval'); return r.result.value; };
await send('Page.enable'); await send('Runtime.enable'); await send('Log.enable');
await send('Page.bringToFront'); await send('Emulation.setFocusEmulationEnabled', { enabled: true });
const URL0 = pathToFileURL(PAGE).href;

async function load(w, scheme) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 600 });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: scheme }] });
  events.length = 0;
  await send('Page.navigate', { url: URL0 + '?t=' + Date.now() });
  for (let i = 0; i < 80; i++) { await sleep(100); try { if ((await evaluate('document.readyState')) === 'complete') break; } catch {} }
  await evaluate('document.fonts.ready.then(() => 1)'); await sleep(200);
}

// Contrast of every text node against the first opaque background behind it. Closed <details> are skipped
// (their content is not shown); the check opens every <details> first so revealed text is checked too.
const CONTRAST = `(() => {
  document.querySelectorAll('details').forEach((d) => d.open = true);
  const parse = (c) => { const m = c.match(/[\\d.]+/g); return m ? m.map(Number) : [0,0,0,0]; };
  const lum = ([r,g,b]) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v/12.92 : ((v+0.055)/1.055) ** 2.4; }; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b); };
  const bg = (el) => { for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c.length < 4 || c[3] > 0.9) return c; } return parse(getComputedStyle(document.body).backgroundColor); };
  const out = []; const small = []; const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode; if (!t.textContent.trim()) continue; const el = t.parentElement;
    if (!el || seen.has(el) || el.closest('svg') || el.closest('script,style')) continue; seen.add(el);
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none' || !el.getClientRects().length) continue;
    const fg = parse(cs.color); const b = bg(el);
    const op = Number(cs.opacity) * (fg[3] ?? 1);
    const mix = fg.slice(0,3).map((v,i) => v*op + b[i]*(1-op));
    const L1 = lum(mix), L2 = lum(b); const ratio = (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && Number(cs.fontWeight) >= 700);
    if (ratio < (large ? 3 : 4.5)) out.push(el.tagName.toLowerCase() + '.' + (el.className || '') + ' "' + t.textContent.trim().slice(0,30) + '" ' + ratio.toFixed(2));
    if (size < 13) small.push(el.tagName.toLowerCase() + ' ' + size + 'px "' + t.textContent.trim().slice(0,20) + '"');
  }
  return { out, small, n: seen.size };
})()`;

for (const scheme of ['light', 'dark']) {
  for (const w of [1280, 390]) {
    console.log(`${scheme} ${w}`);
    await load(w, scheme);
    const sw = await evaluate('document.scrollingElement.scrollWidth'), iw = await evaluate('innerWidth');
    check(sw <= iw, `no horizontal page scroll (${sw} <= ${iw})`);
    if (SHOTS) {
      const h = await evaluate('document.scrollingElement.scrollHeight');
      const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: w, height: Math.min(h, 16000), scale: 1 } });
      writeFileSync(join(SHOTS, `${scheme}-${w}.png`), Buffer.from(shot.data, 'base64'));
    }
    const r = await evaluate(CONTRAST);
    check(!r.out.length, `${r.n} text elements clear contrast${r.out.length ? ': ' + r.out.slice(0, 6).join('; ') : ''}`);
    check(!r.small.length, `no text under 13 px${r.small.length ? ': ' + r.small.slice(0, 4).join('; ') : ''}`);
    if (SHOTS) {
      const h = await evaluate('document.scrollingElement.scrollHeight');
      const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: w, height: Math.min(h, 16000), scale: 1 } });
      writeFileSync(join(SHOTS, `${scheme}-${w}-open.png`), Buffer.from(shot.data, 'base64'));
    }
    const errs = events.filter((e) => (e.method === 'Runtime.exceptionThrown') || (e.method === 'Log.entryAdded' && e.params.entry.level === 'error' && !/fonts\.g/.test(e.params.entry.url || '')));
    check(!errs.length, `no console errors${errs.length ? ': ' + JSON.stringify(errs[0]).slice(0, 200) : ''}`);
  }
}

if (args.includes('--click')) {
  console.log('copy button, real click');
  await load(1280, 'light');
  await send('Browser.grantPermissions', { permissions: ['clipboardReadWrite', 'clipboardSanitizedWrite'], origin: new URL(URL0).origin === 'null' ? undefined : new URL(URL0).origin }).catch(() => {});
  const box = await evaluate(`(() => { const b = document.querySelector('button[data-copy]'); b.scrollIntoView({block:'center'}); const r = b.getBoundingClientRect(); return { x: r.x + r.width/2, y: r.y + r.height/2, key: b.dataset.copy }; })()`);
  await sleep(200);
  const hit = await evaluate(`document.elementFromPoint(${box.x}, ${box.y})?.closest('button[data-copy]')?.dataset.copy || null`);
  check(hit === box.key, `the Copy button is the element under its own center (${hit})`);
  for (const type of ['mouseMoved', 'mousePressed', 'mouseReleased']) await send('Input.dispatchMouseEvent', { type, x: box.x, y: box.y, button: 'left', clickCount: 1 });
  await sleep(300);
  const state = await evaluate(`document.querySelector('button[data-copy="${box.key}"]').dataset.state`);
  const label = await evaluate(`document.querySelector('button[data-copy="${box.key}"] .pk-copy__label').textContent`);
  const want = await evaluate(`document.getElementById('${box.key}').dataset.cleanCode.length`);
  let got = null; try { got = (await evaluate('navigator.clipboard.readText()')).length; } catch (e) { got = 'unreadable: ' + e.message.slice(0, 60); }
  check(state === 'done' || label.startsWith('Press'), `after a real click the button says "${label}"`);
  console.log(`  info clipboard ${got} chars, block ${want} chars`);
  // The fallback, with the clipboard made to fail: it must select the whole text, not the preview.
  const key2 = await evaluate(`(() => { navigator.clipboard.writeText = () => Promise.reject(new Error('blocked'));
    const b = document.querySelector('.pk-code--preview button[data-copy]') || document.querySelector('button[data-copy]');
    b.scrollIntoView({block:'center'}); return b.dataset.copy; })()`);
  await sleep(200);
  const b2 = await evaluate(`(() => { const r = document.querySelector('button[data-copy="${key2}"]').getBoundingClientRect(); return { x: r.x + r.width/2, y: r.y + r.height/2 }; })()`);
  for (const type of ['mouseMoved', 'mousePressed', 'mouseReleased']) await send('Input.dispatchMouseEvent', { type, x: b2.x, y: b2.y, button: 'left', clickCount: 1 });
  await sleep(300);
  const fb = await evaluate(`(() => { const blk = document.getElementById('${key2}'); const t = blk.querySelector('textarea.pk-clean');
    return { label: blk.querySelector('.pk-copy__label').textContent, full: blk.dataset.cleanCode.length, ta: t ? t.value.length : -1,
             sel: t ? t.selectionEnd - t.selectionStart : -1, focused: document.activeElement === t }; })()`);
  check(fb.ta === fb.full && fb.sel === fb.full && fb.focused && fb.label.startsWith('Press'), `clipboard blocked: the whole text is selected (${fb.sel} of ${fb.full} chars, "${fb.label}")`);
}

chrome.kill();
console.log(fails.length ? `\n${fails.length} failed` : '\nall passed');
process.exit(fails.length ? 1 : 0);
