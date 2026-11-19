// What the browser checks open in this repo. Paths are from the repo root.
import { readdirSync, existsSync } from 'node:fs';

const find = (dir, re) => existsSync(dir)
  ? readdirSync(dir, { recursive: true }).map(String).filter((f) => re.test(f)).sort().map((f) => `${dir}/${f}`)
  : [];

// Meeting decks.
export const decks = find('semesters', /^[^/]+\/meetings\/[^/]+-deck\.html$/);
// Companion pages, once built into site/ by their generators (site/ is gitignored).
export const pages = find('site/decks', /^[^/]+\/index\.html$/).filter((p) => !/\/\d{4}-\d\d-\d\d\/index\.html$/.test(p));
