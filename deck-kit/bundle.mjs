// Bundle a deck into one HTML file (ported from rcc-gdg/deck-kit, 2026-09-24): deck.css, deck.js, and every local image
// inlined, so the deck travels on a USB stick, in an email, or as an artifact
// upload. GSAP and the fonts stay on their CDNs, so the file still degrades
// the same way offline (the kit README, Offline). No dependencies.
//
//   node deck-kit/bundle.mjs <deck.html> [out.html] [--artifact]
//
// Default output is <deck>.bundle.html beside the source, which .gitignore skips.
// --artifact shapes the file for a claude.ai artifact, whose host supplies the
// doctype, html, head, and body itself: those wrappers and the meta tags are
// dropped, <title> comes first, and the root attributes are set by a one-line
// script. data-theme is not carried, so the viewer's own theme choice applies.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve, dirname, extname } from 'node:path';

const argv = process.argv.slice(2), artifact = argv.includes('--artifact');
const [src, out] = argv.filter((a) => a !== '--artifact');
if (!src) { console.error('usage: node deck-kit/bundle.mjs <deck.html> [out.html] [--artifact]'); process.exit(2); }
const inPath = resolve(src), base = dirname(inPath);
const outPath = resolve(out || inPath.replace(/\.html$/, '.bundle.html'));
let html = readFileSync(inPath, 'utf8');
const local = (url) => !/^(https?:|data:|\/\/)/.test(url);
const MIME = { '.mp4': 'video/mp4', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp' };
let n = 0;

html = html.replace(/<link rel="stylesheet" href="([^"]+)">/g, (tag, href) => {
  if (!local(href)) return tag;
  n++; return '<style>\n' + readFileSync(resolve(base, href), 'utf8') + '\n</style>';
});
html = html.replace(/<script src="([^"]+)"( defer)?><\/script>/g, (tag, href, defer) => {
  if (!local(href)) return tag;
  // An inline script cannot be deferred, so it waits for the parser itself.
  // The CDN scripts above it stay deferred and still run first.
  n++; return "<script>\ndocument.addEventListener('DOMContentLoaded', function () {\n" + readFileSync(resolve(base, href), 'utf8').replace(/<\/script/gi, '<\\/script') + '\n});\n</script>';
});
html = html.replace(/<img([^>]*?) src="([^"]+)"/g, (tag, attrs, href) => {
  const file = resolve(base, href);
  if (!local(href) || !existsSync(file)) return tag;
  n++; return `<img${attrs} src="data:${MIME[extname(file)] || 'application/octet-stream'};base64,${readFileSync(file).toString('base64')}"`;
});
// Video: src and poster inline too. Clips are encoded under 1 MB (encode-video.swift).
html = html.replace(/<video([^>]*)>/g, (tag, attrs) => '<video' + attrs.replace(/ (src|poster)="([^"]+)"/g, (m, k, href) => {
  const file = resolve(base, href);
  if (!local(href) || !existsSync(file)) return m;
  n++; return ` ${k}="data:${MIME[extname(file)] || 'application/octet-stream'};base64,${readFileSync(file).toString('base64')}"`;
}) + '>');
if (artifact) {
  const attrs = /<html([^>]*)>/i.exec(html)?.[1] || '';
  const sets = [...attrs.matchAll(/([\w-]+)="([^"]*)"/g)].filter(([, k]) => k !== 'data-theme')
    .map(([, k, v]) => `document.documentElement.setAttribute(${JSON.stringify(k)}, ${JSON.stringify(v)});`).join(' ');
  const title = /<title>[\s\S]*?<\/title>/i.exec(html)?.[0] || '';
  html = html.replace(/<!doctype[^>]*>\s*/i, '').replace(/<\/?html[^>]*>\s*/gi, '').replace(/<\/?head>\s*/gi, '')
    .replace(/<\/?body>\s*/gi, '').replace(/<meta [^>]*>\s*/gi, '').replace(title, '');
  html = title + '\n<script>' + sets + '</script>\n' + html.trim() + '\n';
}
writeFileSync(outPath, html);
console.log(`${n} local files inlined -> ${outPath} (${Math.round(html.length / 1024)} KB)`);
