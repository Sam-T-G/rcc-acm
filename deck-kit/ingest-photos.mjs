// Bring the club's own photos into a deck: resize to 1600 px, strip every bit
// of metadata (EXIF, GPS, camera serials), and print collage markup.
// Node 22 plus python3 with Pillow. No network.
//
//   node deck-kit/ingest-photos.mjs <source-folder> <deck-images-folder> [prefix]
//
// Photos of club members go on a public page. Each printed <img> carries
// data-faces="", which the check refuses: set it to "none" when no face can be
// identified, or "consented" when a signed photo slip is on file for everyone
// in it (accessibility.md §2.2). Anything else stays off the deck.
import { readdirSync, mkdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve, extname } from 'node:path';

const [srcArg, outArg, prefix = 'community'] = process.argv.slice(2);
if (!srcArg || !outArg) { console.error('usage: node deck-kit/ingest-photos.mjs <source-folder> <deck-images-folder> [prefix]'); process.exit(2); }
const src = resolve(srcArg), out = resolve(outArg);
mkdirSync(out, { recursive: true });
const files = readdirSync(src).filter((f) => /\.(jpe?g|png|heic|webp)$/i.test(f)).sort();
if (!files.length) { console.error('no photos in ' + src); process.exit(1); }
const lines = [];
files.forEach((f, k) => {
  const name = `${prefix}-${String(k + 1).padStart(2, '0')}.jpg`, dest = join(out, name);
  let from = join(src, f);
  if (/\.heic$/i.test(f)) { const tmp = join(out, '.' + name + '.jpg'); execFileSync('sips', ['-s', 'format', 'jpeg', from, '--out', tmp], { stdio: 'ignore' }); from = tmp; }
  const wh = execFileSync('python3', ['-c', `
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open(${JSON.stringify(from)})).convert('RGB')
im.thumbnail((1600, 1600))
im.save(${JSON.stringify(dest)}, 'JPEG', quality=82, optimize=True, progressive=True)
print(im.width, im.height)`]).toString().trim().split(' ');
  if (from !== join(src, f)) execFileSync('rm', ['-f', from]);
  console.error(`${f} -> ${name} (${wh[0]}x${wh[1]}, metadata stripped)`);
  lines.push(`    <li><img src="${name}" width="${wh[0]}" height="${wh[1]}" alt="[TBD: what is happening, no names]" data-faces=""></li>`);
});
console.log('  <ul class="collage">\n' + lines.slice(0, 6).join('\n') + '\n  </ul>');
if (lines.length > 6) console.error(`note: ${lines.length} photos ingested; a collage shows six. Pick the best six.`);
