# Decision log

One row per binding decision: budget, policy, event go/no-go, template change, or anything else the club would want to remember the reason for. This is rule 5 in [maintenance-rules.md](maintenance-rules.md).

## How to add an entry

1. Propose the decision in the meeting or in an issue (use the `Decision` issue template).
2. When it is decided, add a row to the table below in the same PR that implements it (or in its own PR if nothing else changes).
3. Keep the row to one paragraph. Say what was decided and why, in a sentence or three. If it needs more, fill [templates/decision-record.md](../../templates/decision-record.md), commit it in the semester folder where the decision was made with the date in the filename, and link it from the row.
4. The "Who" column is the deciding body or role (officer meeting, treasurer, general membership vote). Use a person's name only if they have consented to appear in the repo (see [privacy-and-public-repo-policy.md](privacy-and-public-repo-policy.md)).
5. The "Link" column points at the evidence: the PR, the issue, the meeting note under `semesters/<YYYY-term>/meetings/`, or the decision record.

Newest entries at the top. Do not edit or delete old rows; if a decision is reversed, add a new row that says so and links back.

## Log

| Date | Decision | Who | Link |
| --- | --- | --- | --- |
| 2026-09-01 | Design system adopted, provisionally, for docs pages and exported assets: [docs/04-brand/design-system/](../04-brand/design-system/README.md), a port of the sibling GDG on Campus @ RCC system's method with the chapter's own measured values. **Orange `#ff4d00` leads** (the website's accent, inside ACM's secondary palette); **ACM Blue stays inside the ACM logo and never becomes a UI color**; Inter and JetBrains Mono are the faces (what the website already loads); the Rail, a vertical bar derived from the website's own share card, is the page device, with a break whose position encodes the pillar. Provisional because the color and type rows in [brand.md](../04-brand/brand.md) are still [TBD]: confirming them is a separate entry. The two AI Hackathon assets are recorded as using Google's four colors and are retired for new artifacts, not deleted. | Sam Gerungan | [design-system/README.md](../04-brand/design-system/README.md) |
| 2026-09-01 | Asset specs adopted: [design-system/assets.md](../04-brand/design-system/assets.md). **The Instagram feed master is 1080 x 1440 (3:4), not 1:1.** The profile grid has shown 3:4 since January 2025 and native 3:4 uploads landed 2025-05-28, so a square post is cropped 135 px off each side in the grid; the publishing API still caps at 4:5, so a scheduler gets 1080 x 1350. Stories are the same master centered on a 1080 x 1920 field. Every other export (share card, repo preview, slides, print including the lab's laminated station cards and labels) has one row with its safe zone, and type on the master is 44 px or larger. The same file exists in the GDG chapter's repo with one table swapped, so one officer can make content for both clubs. Template change under rule 3: `templates/announcement.md` gains an export-sizes line under Image. | Sam Gerungan | [design-system/assets.md](../04-brand/design-system/assets.md) |
| 2026-08-24 | The repo opens with one repo admin (@Sam-T-G) and the second admin seat open. This violates rule 7 (two admins at all times) and is treated as urgent: repo admin 1 fills the seat, updates [MAINTAINERS.md](../../MAINTAINERS.md) and `.github/CODEOWNERS`, and logs it here. Deadline: [TBD: set at the first officer meeting of Fall 2026]. | Sam Gerungan | [MAINTAINERS.md](../../MAINTAINERS.md) |
| 2026-08-24 | Repository created and its structure adopted: evergreen material in `docs/`, one folder per semester under `semesters/`, templates and scripts for creating semester, event, and meeting files, and the ten maintenance rules in [maintenance-rules.md](maintenance-rules.md). The repo is public under CC BY 4.0 for content. | Sam Gerungan | <https://github.com/Sam-T-G/rcc-acm> |
