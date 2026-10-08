# Design system

How the chapter's web pages, design docs, and exported assets look, and why. Built 2026-09-01 as a port of the sibling GDG on Campus @ RCC system's method. The colors were measured from the club website's palette rather than picked by hand, and the whole thing is provisional until [brand.md](../brand.md) logs a color and type decision; brand.md currently marks both `[TBD]` and names the website as the reference in the meantime.

Brand authority runs: ACM's Visual Identity Standards and chapter policies, then [brand.md](../brand.md), then this system, then the reference surfaces (the club website source and the GDG system, whose method is the precedent). Where they disagree, the higher one wins and this file gets corrected.

| File | What it holds |
|---|---|
| [bright-lines.md](bright-lines.md) | What we take from ACM and the website and what we never take. Read this first. |
| [foundations.md](foundations.md) | Color, typography, space, grid, shape, elevation, motion |
| [tokens.css](tokens.css) | The shipping stylesheet. Light and dark, reset through print |
| [components.md](components.md) | Buttons, cards, tables, callouts, nav, and the page archetypes |
| [documents.md](documents.md) | The design-doc system and the copyable template |
| [accessibility.md](accessibility.md) | Contrast, focus, keyboard, photo consent, and the Rail |
| [assets.md](assets.md) | Every size the club exports: Instagram, share cards, slides, print, with safe zones and type minimums |
| [checklist.md](checklist.md) | Before you publish |

## The short version

**Orange leads.** The website's `#ff4d00` is the primary hue. It is the accent the site already runs on, it sits inside ACM's own sanctioned secondary palette (ACM Orange, PANTONE 138C), and it is not ACM Blue. ACM Blue is the parent's logo color, and a chapter page that uses it as an action color reads as ACM headquarters, which is the one thing chapter policy says not to be. The website already chose a color that reads as heat and speed, and the club's four pillars are all verbs.

**One job each.** Orange is links, buttons, active state, focus, and the Rail. Blue is cross-references out, and nothing else. Red is errors and failure paths, semantic only, and always labeled by a word or an icon because orange and red are close enough in hue to be confused. Green is the live-now marker and the Check callout.

**Three checks that keep it the chapter's own**, all verifiable by looking at a page:

1. ACM Blue appears nowhere except inside the unaltered ACM logo.
2. No single component uses more than two hues.
3. Orange covers at least 70% of the non-neutral area on any surface.

**The pillars get a form, not a hue.** Build, Compete, Learn, and Connect are carried by the Rail's break position, set once per page as `data-pillar` on the root element. A four-pillar color scheme would break checks two and three at once and would put the Google four one step away.

## The Rail

The club's own device, derived from the website's own share card and from nothing ACM or Google owns: a solid vertical bar in the primary color, flush to the inline-start edge of a block, full block height, never a gradient and never rounded. It does real work rather than sitting in a corner. A gap in the bar, the Break, encodes which pillar a page belongs to:

| Page | `data-pillar` | Break sits at |
|---|---|---|
| Build pages | `build` | 20% |
| Compete pages | `compete` | 40% |
| Learn pages | `learn` | 60% |
| Connect pages | `connect` | 80% |
| Club pages, footer, everything else | omit | No break, the bar runs solid |

Someone who has read three meeting pages recognizes the pillar before reading the heading. It costs one attribute per page. The pillar name is always in text beside it; the Break never carries meaning alone.

Adopting the Rail as the system's device is a judgment call and needs a decision-log entry. The geometry is in [accessibility.md](accessibility.md).

## Using it

```html
<html lang="en" data-pillar="learn">
<head>
  <script>
    try { var t = localStorage.getItem('rcc-theme');
          if (t) document.documentElement.dataset.theme = t; } catch (e) {}
  </script>
  <link rel="stylesheet" href="tokens.css">
</head>
```

The theme script goes before the stylesheet so there is no flash. The page is correct without it; the media query carries the system preference on its own. The storage key is the same one the GDG pages use, so a viewer's choice carries across both clubs' pages.

## Required on anything public

- The club name written as [brand.md](../brand.md) writes it: "ACM Student Chapter at Riverside City College" on forms, the constitution, and ASRCC packets; "ACM @ RCC" on social, slides, and this repo.
- "Funded by ASRCC" (or the wording Student Activities asks for) on the flyer of any event ASRCC paid for, and said aloud at the event.
- ACM imposes no disclaimer sentence on chapters. Do not invent one. The chapter policy is that the chapter never presents itself as speaking for ACM, and the club name plus the chapter's own voice satisfy it.

Placement rules are in [bright-lines.md](bright-lines.md).

## Changing this system

Values here are either read from a named source, derived and measured, or judgment calls, and each is labelled. Change a derived value by re-running the contrast audit in [foundations.md](foundations.md) and updating the table. Change a judgment call at an officer meeting and log it in the [decision log](../../01-governance/decision-log.md). Recording the colors and faces in brand.md is the first such decision and the one that turns "provisional" into "adopted".

Last updated: 2026-09-01.
