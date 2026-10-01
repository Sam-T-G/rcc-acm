// Find and fetch an openly licensed photo for a slide, with its credit.
// The same file lives in rcc-acm/deck-kit and rcc-gdg/deck-kit; change both.
// Node 22, no npm install. Resizing uses python3 + Pillow if present, else macOS sips.
//
//   node deck-kit/fetch-image.mjs search "arduino uno r4" [--n 8]
//   node deck-kit/fetch-image.mjs get <id> <dir> <name> [--alt "..."]
//
// search prints candidates from Wikimedia Commons and Openverse, only under
// licenses a public repo and a public page can carry: CC0, public domain,
// CC BY, CC BY-SA. Never NC or ND. Each line starts with an id to pass to get.
//
// get downloads the photo at 1600 px on the long side, re-encodes it as a JPEG
// with no metadata (EXIF and GPS gone), writes <dir>/<name>.jpg, adds a row to
// <dir>/CREDITS.md, and prints a <figure> snippet with width, height, alt, and
// the credit line the slide must show.
import { writeFileSync, readFileSync, existsSync, mkdirSync, statSync, unlinkSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const UA = 'rcc-club-deck-kit/1.0 (https://github.com/Sam-T-G)';
const OK = /^(cc0|pdm|public domain|pd|cc by(-sa)?( \d(\.\d)?)?)$/i;
const [cmd, ...rest] = process.argv.slice(2);
const flag = (k, d) => { const i = rest.indexOf('--' + k); return i >= 0 ? rest[i + 1] : d; };
const pos = rest.filter((a, i) => !a.startsWith('--') && !(i > 0 && rest[i - 1].startsWith('--')));
const strip = (h) => String(h || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const get = async (url) => { const r = await fetch(url, { headers: { 'user-agent': UA } }); if (!r.ok) throw new Error(r.status + ' ' + url); return r; };

async function commons(q, n) {
  const u = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=' + n +
    '&gsrsearch=' + encodeURIComponent(q + ' filetype:bitmap') + '&prop=imageinfo&iiprop=url|extmetadata|size|mime&iiurlwidth=1600';
  const d = await (await get(u)).json();
  return Object.values(d.query?.pages || {}).map((p) => {
    const ii = p.imageinfo?.[0] || {}, m = ii.extmetadata || {};
    return { id: 'commons:' + p.title.replace(/^File:/, ''), title: p.title.replace(/^File:|\.\w+$/g, ''), w: ii.width, h: ii.height,
      license: strip(m.LicenseShortName?.value), creator: strip(m.Artist?.value) || 'unknown', source: ii.descriptionurl, file: ii.thumburl || ii.url, mime: ii.mime };
  }).filter((r) => /jpeg|png|webp/.test(r.mime || ''));
}
async function openverse(q, n) {
  const d = await (await get('https://api.openverse.org/v1/images/?license=by,by-sa,cc0,pdm&page_size=' + n + '&q=' + encodeURIComponent(q))).json();
  return (d.results || []).map((r) => ({ id: 'openverse:' + r.id, title: r.title, w: r.width, h: r.height,
    license: (r.license === 'cc0' || r.license === 'pdm' ? r.license.toUpperCase() : 'CC ' + r.license.toUpperCase() + ' ' + (r.license_version || '')).trim(),
    creator: r.creator || 'unknown', source: r.foreign_landing_url, file: r.url }));
}
async function lookup(id) {
  if (id.startsWith('commons:')) {
    const t = id.slice(8), rs = await commons('"' + t.replace(/\.\w+$/, '') + '"', 5);
    const hit = rs.find((r) => r.id === id);
    if (hit) return hit;
    const u = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata|size|mime&iiurlwidth=1600&titles=' + encodeURIComponent('File:' + t);
    const p = Object.values((await (await get(u)).json()).query.pages)[0], ii = p.imageinfo[0], m = ii.extmetadata;
    return { id, title: t.replace(/\.\w+$/, ''), w: ii.width, h: ii.height, license: strip(m.LicenseShortName?.value), creator: strip(m.Artist?.value) || 'unknown', source: ii.descriptionurl, file: ii.thumburl || ii.url };
  }
  if (id.startsWith('openverse:')) {
    const r = await (await get('https://api.openverse.org/v1/images/' + id.slice(10) + '/')).json();
    return { id, title: r.title, w: r.width, h: r.height, license: (r.license === 'cc0' || r.license === 'pdm' ? r.license.toUpperCase() : 'CC ' + r.license.toUpperCase() + ' ' + (r.license_version || '')).trim(),
      creator: r.creator || 'unknown', source: r.foreign_landing_url, file: r.url };
  }
  throw new Error('id must start with commons: or openverse:');
}

if (cmd === 'search') {
  const q = pos[0], n = +flag('n', 8);
  if (!q) { console.error('usage: node deck-kit/fetch-image.mjs search "<words>" [--n 8]'); process.exit(2); }
  const [a, b] = await Promise.allSettled([commons(q, n), openverse(q, n)]);
  const rows = [...(a.value || []), ...(b.value || [])].filter((r) => OK.test(r.license.replace(/\s+/g, ' ').trim()));
  if (!rows.length) { console.log('nothing under an open license; try other words, or leave the slide as type'); process.exit(0); }
  for (const r of rows) console.log(`${r.id}\n    ${r.title} · ${r.w}x${r.h} · ${r.license} · ${r.creator.slice(0, 60)}\n    ${r.source}`);
} else if (cmd === 'get') {
  const [id, dirArg, name] = pos;
  if (!id || !dirArg || !name || !/^[a-z0-9-]+$/.test(name)) { console.error('usage: node deck-kit/fetch-image.mjs get <id> <dir> <name: lowercase-hyphens> [--alt "..."]'); process.exit(2); }
  const r = await lookup(id);
  if (!OK.test(r.license.replace(/\s+/g, ' ').trim())) { console.error(`refused: license "${r.license}" is not CC0, public domain, CC BY, or CC BY-SA`); process.exit(1); }
  const dir = resolve(dirArg); mkdirSync(dir, { recursive: true });
  const raw = join(dir, '.' + name + '.download'), out = join(dir, name + '.jpg');
  writeFileSync(raw, Buffer.from(await (await get(r.file)).arrayBuffer()));
  // Re-encode: 1600 px long side, JPEG q82, no metadata. Pillow first, sips as the fallback.
  let size;
  try {
    size = execFileSync('python3', ['-c', `
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open(${JSON.stringify(raw)})).convert('RGB')
im.thumbnail((1600, 1600))
im.save(${JSON.stringify(out)}, 'JPEG', quality=82, optimize=True, progressive=True)
print(im.width, im.height)`]).toString().trim().split(' ').map(Number);
  } catch {
    execFileSync('sips', ['-s', 'format', 'jpeg', '-s', 'formatOptions', '82', '-Z', '1600', raw, '--out', out], { stdio: 'ignore' });
    const s = execFileSync('sips', ['-g', 'pixelWidth', '-g', 'pixelHeight', out]).toString();
    size = [+/pixelWidth: (\d+)/.exec(s)[1], +/pixelHeight: (\d+)/.exec(s)[1]];
    console.error('note: resized with sips; EXIF may remain. Install Pillow to strip it.');
  }
  unlinkSync(raw);
  const kb = Math.round(statSync(out).size / 1024);
  const credits = join(dir, 'CREDITS.md');
  const creator = r.creator.replace(/\|/g, '/').slice(0, 120);
  if (!existsSync(credits)) writeFileSync(credits, '# Image credits\n\nEvery photo in this folder, where it came from, and its license. Written by `deck-kit/fetch-image.mjs`; the slide that uses a photo shows the same credit.\n\n| File | Title | Creator | License | Source |\n| --- | --- | --- | --- | --- |\n');
  const table = readFileSync(credits, 'utf8').split('\n').filter((l) => !l.startsWith('| ' + name + '.jpg |')).join('\n').replace(/\n*$/, '\n');
  writeFileSync(credits, table + `| ${name}.jpg | ${r.title.replace(/\|/g, '/')} | ${creator} | ${r.license} | <${r.source}> |\n`);
  const credit = `Photo: ${creator.slice(0, 60)}, ${r.license}`;
  const alt = flag('alt', '[TBD: one sentence saying what the photo shows]');
  console.log(`wrote ${out} (${size[0]}x${size[1]}, ${kb} KB) and a row in ${credits}\n`);
  console.log(`<figure class="photo">\n  <img src="${name}.jpg" width="${size[0]}" height="${size[1]}" alt="${alt}">\n  <figcaption class="credit"><a href="${r.source}">${credit}</a></figcaption>\n</figure>`);
  console.log('\nFix the src path relative to the deck. The credit line stays on the slide.');
} else {
  console.error('usage: node deck-kit/fetch-image.mjs search "<words>" | get <id> <dir> <name> [--alt "..."]'); process.exit(2);
}
