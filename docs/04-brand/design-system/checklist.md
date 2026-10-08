# 11. Before you publish

Run this on any public artifact. Any failure in 1 through 6 stops the publish. A social post also runs the pre-post list in [assets.md](assets.md); this page does not restate it.

## Brand

1. Is the club name on the artifact, written as [brand.md](../brand.md) writes it, as selectable body text at full contrast?
2. Could a reasonable visitor think ACM made this, endorsed it, or funded it?
3. Is ACM Blue anywhere on the artifact outside the unaltered ACM logo?
4. Are the Google four present in one composition, or three of them at similar weight? Does orange cover at least 70% of the non-neutral area?
5. If the ACM logo appears, has it been altered in any way on the standards' improper-use list in [bright-lines.md](bright-lines.md), including the ones that do not feel like alterations: a white knockout, a scroll animation, a rounded tile, a stretched aspect ratio, a size under 0.5 inch?
6. If ASRCC paid for the event, is "Funded by ASRCC" on the artifact?

## Accessibility

1. Every text pair measured, not estimated, against the audit in [foundations.md](foundations.md). Anything not in that table gets measured before it ships.
2. Tab through the whole page. Is focus visible on every stop, including inside cards that clip their media?
3. Is any meaning carried by color alone? Links underlined, pillars named in text, error states labeled by a word or icon, diagram series double-encoded?
4. Turn on reduced motion. Does every state change still happen and every movement stop?
5. Resize to 320px. Does the page body scroll horizontally anywhere?
6. Does every image have alt text that names what is happening, and explicit width and height?

## Craft

1. One `h1`. No skipped levels. Sentence case throughout.
2. A complete introductory sentence before every list and table.
3. At most three callouts, none adjacent, each passing the three-part admission test.
4. Every column of numbers set in tabular figures.
5. Prose capped at `--acm-measure-prose`, even inside a wide container.
6. Last-updated date present and actually current.
7. Nothing at rest is using elevation 4.
8. Does the page look considered on GitHub with no CSS at all?

---

## 12. Open items, with owners

Owners are roles, never names, per the [privacy policy](../../01-governance/privacy-and-public-repo-policy.md).

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Colors and typography recorded in `brand.md` as a decision, with a decision-log entry. Until then every value in this system is provisional | Chair | Any artifact that claims to be on-brand |
| 2 | The chapter logo from ACM's matrix page (`identitystandards.acm.org/matrix3.html`, unreachable from tooling on 2026-09-01), its rules recorded in `brand.md`, files under 1 MB in `assets/` | Chair | Print, signage, the social avatar |
| 3 | The two AI Hackathon assets in `assets/`: retire or keep, logged either way. Spring 2027 hackathon materials get rebuilt under this system | Event lead | Spring 2027 hackathon materials |
| 4 | Adopting the Rail as the system's device, logged in the decision log | Chair | Any build |
| 5 | Which pillar each meeting type maps to for `data-pillar` (lab day, ICPC, career, mini-talk, hackathon, showcase); this system does not decide it | Chair | First meeting page build |
| 6 | Converge the website on these tokens: its dark ground, its 32px and 48px radii, and its gradient text all diverge from the docs system | Whoever builds the site | Not blocking |
| 7 | Lucide license verification, recorded in `brand.md` | Whoever builds the site | Icon adoption |
| 8 | Inter body weight on dark: 400 as shipped, or 450 if light-on-dark blooms. There is no GRAD axis to retune | Whoever builds the site | Not blocking |
| 9 | `size-adjust` on the fallback face, measured on real platforms | Whoever builds the site | Not blocking |
| 10 | Font-loading response: byte count and `@font-face` block count for the Inter plus JetBrains Mono URL, fetched and recorded in foundations | Whoever builds the site | Not blocking |
| 11 | Dark elevation alphas and the container tint chroma, tested on the A-210 projector | Lab lead | Showcase page, 2026-12-10 |
| 12 | The Rail field hairlines and the Break's gap edges, checked on the projector and at 2x device pixel ratio | Lab lead | Showcase page, 2026-12-10 |
| 13 | `docs/04-brand/render-canary.md`, the file that exercises every legal markdown construct once, rendered both ways | Secretary | Any standalone HTML build |
| 14 | The image-size row in `templates/announcement.md` is logged in the decision log (2026-09-01, the asset-specs entry), per maintenance rule 3. Fill it on the next announcement | Secretary | Next announcement |
| 15 | `links.md` website row: the website source names `rccacm.com`; links.md still marks the live URL `[TBD]` | Secretary | Next link check |
| 16 | `check.sh`: a check that any file referencing a logo asset also carries the club name per `brand.md`. A per-card clock check, which the GDG system needs, does not apply here: ACM meetings run the playbook's fixed agenda and cards carry no clock | Chair | Not blocking |
| 17 | Photography at the ICPC regional site: what the contest directors allow, recorded in the ICPC playbook | Event lead | Next regional |
| 18 | The RCC media release form: does one exist, and does it supersede the club's consent slip | Secretary | First event with photography |
| 19 | ACM's identity standards are version 1.0 from 2007. Check at each semester start whether ACM has issued a newer guide, and reconcile | Chair | Semester start |
| 20 | GitHub's dark canvas `#0d1117`, current as of 2026-09-01. If it changes, re-run the dual-mode marks table in foundations | Chair | Semester start |

---

**Last updated: 2026-09-01.** Reviewed at each semester start alongside `docs/04-brand/brand.md`. Changes that alter a rule go in `docs/01-governance/decision-log.md`.
