# Design docs

The system for the club's written artifacts: playbooks, meeting pages, station cards, semester plans, event plans, and the HTML pages built from them. It covers what a document is made of, how it is structured, what markdown constructs are legal, and how a `.md` file becomes a styled page.

**Scope.** This section owns document structure and markdown legality. [components.md](components.md) owns what a callout, table, and code block *look like*; this section owns which ones exist and when an author is allowed to use one. [foundations.md](foundations.md) owns every value. Nothing here restates a token value.

**Governing principle, and everything below follows from it:** *an author writes structure, never appearance.* GitHub strips `class`, `style`, `id`, and all CSS from markdown. Any convention that depends on an attribute an author types works in exactly one of the two renderers. So the converter derives styling from structure the author already had to write, and the author has no styling controls at all.

---

## 1. Anatomy of a club document

The anatomy comes from Google's technical-writing guidance by way of the sibling GDG chapter's system, which is the precedent this file ports: one h1, sentence case, heading grammar that encodes section type, a closed callout set with an admission test, and a list-versus-table decision rule. That is method, and method is free to learn from. What it deliberately does **not** take is any corporate design-doc review structure (security, privacy, i18n, storage sign-off sections). A student club that ships a sign-off matrix it never fills in has built theater.

The blocks, in order. Blocks 1, 2, and 9 are required in every document. The rest appear when the document has that job.

| # | Block | What it is for | How it fails |
|---|---|---|---|
| 1 | **Title** (single h1) | Names the artifact. Sentence case. Matches the filename slug. | It is a category ("Playbook"), it is Title Case for no reason, or a second h1 appears further down |
| 2 | **Job line** (1 to 2 sentences, no heading, directly under the h1) | Tells a reader in one breath what this file does and who holds it. The weekly meeting playbook's Purpose opens correctly: "The weekly meeting is the club." The meeting plan does too: "Every Thursday this term, what it is, and who owns it." | It becomes a preamble, it restates the title in longer words, or it pre-announces what the document will cover. The rule is blunt: do not pre-announce anything |
| 3 | **Facts table** (two-column, empty header row) | The constants a reader needs before acting: owner role, room, inputs, status. The weekly meeting playbook's When table and every station card's header table already do this, and it is the house signature. Keep it. | It carries prose instead of values, it duplicates something the body says again, or a value is guessed instead of marked `[TBD]` |
| 4 | **The shape** (h2, noun phrase) | The thing itself, laid out as a table or a short list. "Meeting formats" and its four-row table. "The term" and its sixteen Thursdays. A reader who stops here knows what they are looking at. | It is written as narrative when it is really a table of three or more facts per row |
| 5 | **The rules that bind it** (h2, noun phrase) | The constraints that do not bend. "Standing rules." "Design rules." Short, numbered, each with its consequence stated. | More than about six, or a rule that is really a preference. A rule nobody would enforce weakens the ones you would |
| 6 | **The procedure** (h2, infinitive verb) | Ordered steps a person executes. "To file a lab day:" The station card's Steps section is the model: each step names the TODO, gives one hint, and says what should happen when it works. | Conditions land after the instruction instead of before it. Put conditions before instructions, not after; that one sentence-level rule has an outsized effect on whether a step gets executed correctly |
| 7 | **Failure modes** (h2, noun phrase) | Named ways this goes wrong and the specific correction. The station card's Common bugs table is the model: symptom, real cause, fix in one line. | Vague symptoms ("the board acts weird"). A failure mode a facilitator cannot recognize at the bench is a paragraph, not a tool |
| 8 | **Boundary** (h2, noun phrase) | What this document does not cover, and where that lives. The lab-day playbook's table of what lives in the lab repo is the model. | Missing. Without it every reader who wants the adjacent thing either asks or duplicates it |
| 9 | **Maintenance footer** | `Last reviewed: YYYY-MM-DD. Owner: ROLE.` A stale date is a bug, not a cosmetic issue. Put a review date on anything the club publishes | Missing, or updated by a bot so it means nothing |

Two anatomy rules that are worth stating as rules:

**Single source.** A fact lives in exactly one file. Every other file links to it. The meeting plan says so out loud: "The repeatable structure lives in the weekly meeting playbook; this file is only the semester's assignments." That sentence is the pattern. Copy it into any new document family.

**Roles, not names.** Documents name a role (Chair, Lab lead, Advisor); one table per semester maps roles to people, with consent. This is already the club's convention, it keeps the repo inside its own [privacy policy](../../01-governance/privacy-and-public-repo-policy.md), and it makes documents reusable next year. Design docs inherit it without exception.

---

## 2. Heading hierarchy and structure

### Depth

| Level | Use | Rule |
|---|---|---|
| h1 | The document title | Exactly one per file, always the first line |
| h2 | Sections | The working level. Aim for four to seven per document |
| h3 | Subsections inside a long h2 | Allowed. Never skip from h2 to h4 |
| h4 | Nothing | If you need one, the h2 above it is a document. Split |

The h4 ban has a structural reason, not a taste reason. In this type scale the heading roles run out at h3 (`headline-sm`); h4 drops to `title-lg`, which is body-sized type at a heavier weight. Below the section level a heading stops being a section and becomes a bold sentence, and at h4 the reader has already lost the outline.

### Grammar

Heading grammar encodes section type, so a reader knows what kind of section they are in from the first word.

- **Task section: bare infinitive.** "Run one." "Flash the boards."
- **Concept section: noun phrase.** "The pin map." "Meeting formats."
- **No `-ing` openers.** "Running a lab day" becomes "Run a lab day".
- **Sentence case everywhere,** including the h1. This is the single highest-yield change to how a document reads, and it costs nothing. Enforce it in review.
- **No numbers, links, or inline code inside a heading text.** Headings are also anchors and link labels.

Three sanctioned exceptions, all already live in the repos. Keeping the exception list closed and written down is what keeps the rule alive.

1. **Playbook titles carry the prefix.** `# Playbook: Weekly meeting` stays. The prefix is how a reader tells a playbook from a policy in a search result, and every playbook in `docs/03-playbooks/` already uses it.
2. **Station card facts tables and timings stay in the heading.** `## Check for understanding (60 seconds)` keeps its parenthetical. The number is the promise the section makes, and the lab repo's template writes it that way.
3. **Role and tier names in table cells stay in backticks.** That is a cell, not a heading, and it is fine.

### Ordering

Order by what the reader needs to act, not by the order you figured it out.

1. Title, job line, facts table.
2. The shape of the thing.
3. The rules that bind it.
4. The procedure.
5. Edge cases, failure modes, degradation ("If only three officers are free, run three stations").
6. Boundary, maintenance footer.

The test: a reader who stops after the facts table can still show up and do the right thing. A reader who stops after block 4 knows the shape well enough to explain it to someone else.

### When to split

Split when any one of these is true. They are triggers, not a scoring system.

| Trigger | Split into |
|---|---|
| One h2 runs past roughly two screens | Its own file, linked from a one-line summary |
| More than seven h2 sections | Two documents, or an index plus children |
| Two blocks change on different cadences | Evergreen part to `docs/`, dated part to `semesters/<term>/`. This is the repo's existing rule 1 and it is the primary split axis |
| Two different roles own two halves | Two files, one owner each |
| A section is linked to from three or more documents | It was always a document |
| The document holds both a machine and its instances | Machine to the playbook or the lab repo's `docs/program.md`; instances to the semester folder or `challenges/`. The lab program plus its 24 station cards is the worked example, and so is the weekly meeting playbook plus the meeting plan |

---

## 3. Constructs that render correctly on GitHub and as HTML

**Provenance note before the rules:** none of the GitHub renderer behavior below has been verified against today's github.com. It is carried over from the sibling system and from general knowledge of GitHub Flavored Markdown, and it should be treated as accurate but unverified. Section 3.5 gives the canary that turns it into verified fact, and the club should run that once before trusting any line of it.

### 3.1 The two hard constraints

1. **GitHub sanitizes HTML.** `class`, `style`, and `id` attributes are stripped, `<style>` and `<script>` are removed, and only a whitelisted tag set survives. `<aside>` is not on that list, so an `<aside class="note">` callout is unusable here. Anything styled by an attribute the author typed renders in the standalone page and disappears on GitHub.
2. **CommonMark alone is not enough for the standalone page.** Tables, task lists, strikethrough, autolinked bare URLs, footnotes, and GitHub alerts are all GFM extensions. A converter running plain CommonMark silently drops or mangles every one of them. The parity traps are listed in 3.4.

### 3.2 Callouts

Use GitHub alert syntax. It is the only native callout on GitHub, and it is plain blockquote structure, so a converter can detect it with no author-supplied attribute.

The club's set is closed at three. GitHub offers five (`NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`); `TIP` and `CAUTION` are banned so the remaining three keep their distinctiveness. The mapping is the same one [components.md](components.md) §7.7 renders, so a doc that passes review here renders correctly there without a second decision.

| Syntax | Means | Example use |
|---|---|---|
| `> [!NOTE]` | Useful, not critical. The reader can skip it and still succeed | "The next club has A-210 at 2:30, so pack up starts at 1:45" |
| `> [!WARNING]` | Get this wrong and the session, the kit, or the event degrades. Money, safety, privacy, a room booking, a pin map change | "The pin map is a contract. Changing it means rewiring six stations and reprinting six cards" |
| `> [!IMPORTANT]` with a bold `Check:` lead-in | The 60-second check for understanding, or the one concrete ask a meeting ends with | "**Check:** ask why the LED still blinks when the button is held. Good answer names the loop, not the wire" |

Admission test, applied before anything becomes a callout. All three conditions must hold:

1. The information is relevant but not necessary to the current task.
2. The interruption does not obstruct the reader's progress.
3. The content does not flow from the sentence before it.

Explicit non-uses: cross-references, prerequisites, a step of a procedure, anything critical to success, and anything the preceding paragraph already leads into. Most callout systems specify what a callout looks like. This one specifies what is allowed to become one, which is the half that actually holds.

Scarcity rule, and it is what lets the styling stay quiet: **at most two callouts per document, never two adjacent, never immediately after a heading.** When multiple notices share a page they begin to lose their visual distinctiveness. (The three-per-page ceiling in components.md is the same rule for a built page that may render more than one source file.)

Banned callout forms: `!!! note` (MkDocs), `:::note` (Docusaurus), a bolded `> **Note:**` blockquote, and an emoji-prefixed line. The first two render as literal text on GitHub. The third is superseded by alerts. The fourth depends on emoji shortcodes that only GitHub expands.

### 3.3 Tables, code, links, lists

**Lists versus tables.** One datum per item is a bulleted list, two is a description list, three or more is a table. A single-column table is a list. A table with one row is two sentences.

**Tables.**

- GFM pipe tables only. No `colspan`, no `rowspan`, no nested tables, no merged cells, no `<caption>`, and no block content inside a cell (a list or a fenced block inside a cell does not render).
- A line break inside a cell is `<br>`. A literal pipe is `\|`.
- The header row is required by the parser. A key/value facts table uses an empty header (`| | |`), which is exactly what the weekly meeting playbook and every station card already write, and the converter detects that shape and styles it as a facts block.
- Column heads are sentence case, concise, no end punctuation of any kind.
- Every table gets a complete introducing sentence above it. The complete sentence is the part that matters.
- Six columns is the practical ceiling. GitHub wraps cell text rather than scrolling, so a wide table gets very tall on a phone instead of scrolling. The event plan template's budget table runs six and the kit inventory in the lab repo is the known exception; the standalone page wraps every table in a horizontal scroll container, and GitHub gets the tall version.
- Styling, owned by components.md: horizontal rules only, tinted header row, body text one step below running prose. No vertical rules, no zebra stripes.

**Code blocks.**

- Always fenced, never indented, and always with a language token: `cpp`, `python`, `sh`, `text` when there is no language.
- GitHub ignores extra info-string content (`title=`, line-range highlights). Do not write it. Put the filename in the introducing sentence.
- ` ```diff ` is the only line-level highlighting that works in both renderers.
- ` ```mermaid ` renders natively on GitHub. The converter must render it too, or the standalone page shows raw source. Section 6 covers this.
- Inline code is for literal strings a reader types or matches: paths, filenames, role and tier tokens, pin names (`GP14`), commands, flags.

**Links.**

- Relative links between `.md` files, exactly as the repo already does. `lychee --offline` in CI checks them, and `scripts/check.sh` checks them again locally.
- The converter rewrites `.md` to `.html` and preserves relative depth. Absolute paths to `github.com/...` are banned inside the docs tree with one exception: links into the lab repo, which is a different repository and cannot be reached relatively. Those are the cross-references components.md marks `data-xref` and colors `secondary`.
- No custom anchor IDs. `{#my-id}` is kramdown and pandoc syntax; GitHub prints it as literal text.
- Anchors are generated from heading text: lowercase, punctuation dropped, spaces to hyphens, duplicates suffixed `-1`, `-2`. The converter must use the identical algorithm (see section 6) or every cross-document anchor link breaks on the published site while passing CI.
- Bare URLs autolink on GitHub, which is why `MD034` is off in `.markdownlint.yml`. The converter must have linkification enabled or those URLs render as dead text.

**Other constructs.**

| Construct | GitHub | Standalone | Verdict |
|---|---|---|---|
| Task lists `- [ ]` | Renders as checkboxes | Needs an enabled plugin | Use. Already used in the playbooks and the event-plan template |
| Footnotes `[^1]` | Supported | Needs an enabled plugin | Allowed, rarely needed |
| `<details>` / `<summary>` | Supported | Native HTML | Allowed. Leave a blank line after `</summary>` or the markdown inside is not parsed |
| `<br>` | Supported | Native | Allowed inside table cells only |
| HTML comments | Hidden in both | Hidden | Use for `<!-- fill: -->` markers, which `check.sh` counts |
| YAML front matter | Rendered as a visible table, not hidden | Depends on the converter | Do not use. Metadata goes in the facts table |
| Emoji shortcodes `:warning:` | Expands | Does not expand | Banned |
| `#gh-dark-mode-only` image suffix | Deprecated GitHub-only hack | No effect | Banned. Use one image that reads in both themes, or the `<picture>` block in components.md §8.8 |
| `<style>`, `<script>`, `class`, `id` | Stripped | Works | Banned. This is the whole principle |
| Math `$$...$$` | Renders | Needs a math plugin | Not needed yet. The lab's T3 cards may want it; add the plugin when a card does |

### 3.4 The parity traps, in one place

These are the constructs that pass CI, look right on GitHub, and quietly break the published page if the converter is not configured for them: **tables, task lists, strikethrough, autolinked bare URLs, footnotes, GitHub alerts, mermaid fences, heading anchor slugs, and `.md` link rewriting.** Nine items. Every one of them is a converter configuration, not an authoring decision.

### 3.5 The canary

Add `docs/04-brand/render-canary.md`: one file that uses every legal construct once, including all three callouts, a facts table, a six-column table, a `cpp` block with a header, a `diff` block, a mermaid fence, a footnote, a task list, a bare URL, a relative link, an absolute link into the lab repo, and an anchor link into itself. Render it both ways and compare, once per semester and on any converter change. A construct that is not in the canary is not supported, and that is the rule that keeps this section from rotting. The file does not exist yet (§12).

---

## 4. The template

Copy to `templates/design-doc.md`. Adding it to `templates/` needs a decision-log entry first (repo rule 3). Run `scripts/check.sh` on a filled copy before shipping it.

````markdown
<!-- Design doc. Copy into docs/<section>/ for evergreen material, or
     semesters/<YYYY-term>/ for anything tied to a date, a person, or a dollar figure.
     Delete every block you do not need. Do not add h4 headings; split the doc instead.
     Run scripts/check.sh before opening the PR. -->

# <!-- fill: sentence case title, matches the filename slug -->

<!-- fill: one or two sentences. What this file does, and what it is the source of truth for.
     No preamble. Do not announce what the sections below will say. -->

| | |
|---|---|
| Owner | <!-- fill: a ROLE, never a person's name --> |
| Applies to | <!-- fill: what this governs --> |
| Inputs | <!-- fill: what a reader needs in hand, or "none" --> |
| Related | <!-- fill: relative link to the nearest doc, or "none" --> |

## <!-- fill: the shape. Noun phrase. -->

<!-- fill: a complete sentence introducing the table below. -->

| <!-- fill: head --> | <!-- fill: head --> | <!-- fill: head --> |
|---|---|---|
| | | |

## The rules

These do not bend for a good idea.

1. **<!-- fill: rule, as an imperative -->** <!-- fill: one sentence on the consequence of breaking it. -->
2. **<!-- fill: -->** <!-- fill: -->

## To <!-- fill: task, bare infinitive -->

<!-- fill: state any condition before the step it applies to, not after. -->

1. <!-- fill: -->
2. <!-- fill: -->

> [!NOTE]
> <!-- fill: only if all three hold: relevant but not necessary, does not block
>      the reader, does not flow from the sentence above. Otherwise delete.
>      Maximum two callouts in this file, never two in a row. -->

## Failure modes

- **<!-- fill: the symptom, recognizable in the moment -->.** <!-- fill: the correction, one sentence. -->
- **<!-- fill: -->.** <!-- fill: -->

## Not in this doc

- <!-- fill: adjacent thing --> lives in <!-- fill: relative link -->.

---

Last reviewed: <!-- fill: YYYY-MM-DD -->. Owner: <!-- fill: ROLE -->.
Unknowns are marked `[TBD]`. Never guess a date, a room, a name, or an amount.
````

---

## 5. Length and density

Every line loads every time someone reads the file, and instruction files load every turn for the tooling that reads them. A line that is not load-bearing costs something on every read.

### Budgets

Set by this system, not measured from anything. Treat them as review triggers, not hard failures.

| Document type | Target | Hard ceiling |
|---|---|---|
| Index or README | 250 words | 400 |
| Meeting page | 400 words | 700 |
| Station card | 600 words | 900 |
| Playbook | 900 words | 1,400 |
| Semester plan | 1,200 words | 1,800 |
| Template | Whatever the form needs, and no explanation the form does not need | |

Past the ceiling, split (section 2). Do not compress by deleting the failure modes or the Common bugs table; those are the highest-value lines in the file.

### The tests

Apply these in review, in this order.

1. **The paragraph test.** For each paragraph: what are you telling the reader, why does it matter to them, and how do they use it? A paragraph that cannot answer all three is cut.
2. **The single-source test.** Does this fact exist in another file? Then link, and delete this copy. The weekly meeting playbook holds the spine. Meeting pages do not restate it. The lab repo's `docs/program.md` holds the design rules. Cards do not restate them.
3. **The pre-announcement test.** Delete every sentence that describes what the document is about to do. "In this section we will cover" is always deletable.
4. **The three-facts test.** Three or more related facts per item is a table. Prose carrying five parallel facts is a table that has not been written yet.
5. **The load-bearing test.** Delete the line. Would a facilitator at 11 PM the night before, or at the bench at 12:49, do anything differently? If not, it stays deleted.

### Density conventions

- Paragraphs cap at four sentences. Most should be one or two.
- Second person, active voice, present tense. "You" rather than "we".
- Fixed prescriptive vocabulary: **must** or a bare imperative for required, "we recommend" for recommended, **can** for optional, **might** for a possible outcome. Generally avoid "should"; it reads as either of the first two and commits to neither.
- No em dashes inside sentences. Periods, colons, semicolons, parens, or "and". `check.sh` fails the build on U+2014.
- Register, calibrated by example rather than adjective. Too informal: "This lab day is going to be SO good." Right: "Steps 1 and 2 are reachable in the first ten minutes." Too formal: "Initial task completion is anticipated within the opening segment of the session."
- The escape hatch is part of the system: break any of these rules sooner than say anything outright barbarous. Consistency is the default, not the goal.

---

## 6. From markdown to a styled page

The `.md` file in the repo stays the source of truth. HTML is build output, never checked in beside the markdown. Build to a gitignored `site/` and publish with a GitHub Pages Actions artifact, so `scripts/check.sh` (which walks every file and enforces the 1 MB limit) never sees generated output. The club website at rccacm.com is a separate Next.js codebase and is not this build; §8.1 in components.md says how the two relate.

### 6.1 Toolchain

CI already runs Node for `markdownlint-cli2`, so the converter runs there too and adds no new runtime.

- **Parser: `markdown-it`,** GFM-configured, with `linkify` on, plus `markdown-it-footnote` and a task-list plugin. Two custom rules carry the club's conventions: alert blockquotes to callout markup, and empty-header two-column tables to facts blocks.
- **Anchors: `github-slugger`.** This is load-bearing. It implements GitHub's own slug algorithm, and using anything else means anchor links pass `lychee --offline` and land on nothing in the published page.
- **Mermaid:** pre-render fences to inline SVG at build time so the page carries no runtime dependency, or ship the mermaid runtime. Pre-rendering is preferred; it keeps the page self-contained and works with a strict content policy.
- **Syntax highlighting:** a build-time highlighter over the `cpp`, `python`, and `sh` fences, with a theme whose every token color is measured against `--acm-code-surface` in both themes (components.md §7.11). No client-side highlighter.
- **Parity oracle (optional, and worth doing once):** GitHub's REST `POST /markdown` endpoint in `gfm` mode returns GitHub's own HTML for a given source. Run the canary from 3.5 through it and diff the structure against the local converter's output. It is rate-limited, so use it as a periodic check rather than a build step. Confirm current endpoint parameters before wiring it up.
- Pandoc with `-f gfm` is a workable alternative and handles tables, footnotes, task lists, and autolinks natively, but it has no GitHub alert support, so the alert transform is needed either way.

### 6.2 Transforms

| Stage | Transform | Why |
|---|---|---|
| 1 | Collect `docs/**/*.md`, `semesters/**/*.md`, `templates/**/*.md` | Templates publish too; a reader should be able to see the blank form |
| 2 | Parse with the GFM configuration above | Covers all nine parity traps from 3.4 |
| 3 | h1 becomes the page title and the `<h1>`; strip it from the body flow | One h1 per page, enforced by the build rather than by review |
| 4 | Alert blockquote to the callout element components.md specifies, label included | Author writes `> [!NOTE]`, gets the club callout |
| 5 | Two-column table with an empty header row to the facts block | Detects the house pattern with no author markup |
| 6 | Every other table wrapped in a horizontal scroll container | Wide tables scroll instead of forcing the page to |
| 7 | Rewrite `.md` link targets to `.html`, preserving relative depth; leave absolute links to the lab repo alone and mark them `data-xref` | Relative links keep working in both places; cross-repo links take the secondary color |
| 8 | Slug every heading with `github-slugger`; build the on-page section list from h2 and h3 | Anchor parity, and the reader sees the outline before reading |
| 9 | Pre-render mermaid; highlight code at build time; add `loading="lazy"` and require `alt` on every image | Alt text is required, including on images inside tables |
| 10 | Read the meeting format from the facts table and set `data-pillar` on the root | The Rail's Break follows the page with no author markup |
| 11 | Emit the maintenance footer's review date into the page footer | A stale date is visible, which is what makes it a bug |

Build fails on: a second h1, an h4, a callout without one of the three legal labels, more than two callouts in a file, an image without `alt`, or a `.md` link that resolves to nothing. Those are the rules from sections 2 and 3 with teeth.

### 6.3 The page shell

One HTML shell, one stylesheet, tokens only. Referenced by role name; if the sibling sections use different role names, rename here and nowhere else.

- **Type.** h1 takes the `display-sm` role, h2 `headline-lg`, h3 `headline-sm`, prose `body-lg`. Table and callout text sit one step below prose, and code takes the `code` roles. Hierarchy is carried by size and space; weight stays at `strong` for every heading. That restraint is most of why a page reads as calm rather than promotional.
- **Rhythm.** Space above a heading is exactly twice the space below it, at every level, in units from the space scale. That one ratio does all the sectioning work, with no rules, boxes, or background changes needed to mark a boundary. It is also why documents do not need `---` separators, and why adding them fights GitHub, which already draws its own hairline under h1 and h2.
- **Callouts.** Tinted ground plus a darker same-hue foreground plus the bold label, an `outline` hairline, the short Rail as the inline-start edge, and an asymmetric left inset so the block reads as an interruption. Colors come from the role tokens in foundations.md. No icon column; the label and the tint carry the meaning.
- **Tables.** Horizontal rules only, tinted header row, denser than surrounding prose.
- **Code blocks.** The most interior padding of any element on the page, a header row with the filename on multi-line blocks, and the copy control's top padding computed as `max(normal padding, button size)` so it can never collide with the first line.
- **Theme.** Tokens defined on `:root`, redefined under `prefers-color-scheme: dark` and again under an explicit `data-theme` attribute so a three-state control (light / dark / system) wins in both directions. Values only; no component knows which theme it is in.
- **Motion.** Whatever foundations.md §5 specifies, inside `prefers-reduced-motion: no-preference`. Documentation pages need almost none.

### 6.4 Compliance on published pages

Every public page carries the club name as [brand.md](../brand.md) writes it, and "Funded by ASRCC" wherever ASRCC paid for the thing the page records. ACM prescribes no disclaimer sentence for chapters; what it prescribes is that the chapter never presents itself as speaking for ACM, and that the ACM logo, when it appears, is the authorized artwork unaltered. A page that implies ACM reviewed, endorsed, or funded it fails review whether or not any sentence says so.

And the line this whole section sits on: the page takes the documentation **method** (sentence case, the heading grammar, the 2:1 heading rhythm, the closed callout set with an admission test, the list-versus-table rule, tone-carried hierarchy) and nobody's **chrome**. No parent-organization header, no ACM Blue as an identity accent, no framing that makes a club doc look like an ACM publication, and none of the Google four that the old hackathon assets carry (§1.3).

---

## Provenance

- **Sourced, by way of the sibling GDG chapter's system, from Google's technical-writing method:** sentence case for all headings and titles; the heading grammar rule and the `-ing` ban; one h1, no skipped levels, no numbers or links or code in headings; the closed callout set, its three-condition admission test, its non-uses, and the scarcity rule; the list-versus-table decision rule; table column-head rules and the introducing-sentence rule; the 2:1 heading space ratio; flat heading weights; callouts as tint plus same-hue text; tables at one step below prose with horizontal rules only; code blocks holding the most padding; second person, active voice, conditions before instructions, the prescriptive vocabulary set, "don't pre-announce", the paragraph test, and the escape hatch; last-updated dates on published documents; the brand-versus-plain typeface split behind the h4 argument. Method is public practice and free to learn from; none of it is anyone's chrome.
- **Derived here, not sourced:** every word budget in section 5, including the new meeting-page row; the split triggers in section 2; the six-column table ceiling; the mapping of the club's three callouts onto GitHub's five labels (`IMPORTANT` for Check, matching components.md); the three heading exceptions; the anatomy block order; the lab-repo exception to the absolute-link ban; the `data-pillar` transform in 6.2.
- **Unverified, and not from any source read this session:** all GitHub renderer behavior in section 3, including the sanitizer's tag and attribute whitelist, alert label set and coloring, front-matter rendering, and info-string handling. The canary in 3.5 is how the club converts it into fact, and it should be run before this section is relied on.
- **Also provisional:** the whole system rests on brand.md, which still marks the club's colors and typography `[TBD]` and names the website as the reference until a decision is logged. If that decision lands on different values, the role names in this file survive the swap without a single change here.

Source files read: `docs/03-playbooks/weekly-meeting.md`, `docs/03-playbooks/club-rush.md`, `docs/03-playbooks/microcontroller-lab-day.md`, `docs/00-charter/officer-roles.md`, `semesters/2026-fall/meeting-plan.md`, `templates/event-plan.md`, `templates/announcement.md`, `CONTRIBUTING.md`, `.markdownlint.yml`, `scripts/check.sh`, and in the lab repo `templates/challenge-card.md`, `docs/facilitator-guide.md`, `docs/showcase.md`.

---

Last updated: 2026-09-01.
