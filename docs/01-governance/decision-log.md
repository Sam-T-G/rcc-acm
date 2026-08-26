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
| 2026-08-25 | The microcontroller lab program is proposed for Fall 2026: six lab days of four parallel 30-minute stations, one per competency tier, plus a showcase, with a hard cap of $1,000 on parts including tax and shipping. The Raspberry Pi Pico 2 W with pre-soldered headers is the chosen board: about $8 each keeps six stations plus spares inside the cap, MicroPython gives brand-new students a working program in 30 minutes, and the arduino-pico core runs Arduino C++ on the same hardware so tiers T1 to T3 reinforce the RCC CIS-5 and CIS-17 sequence instead of competing with it. It is in stock at multiple vendors, so a dead board is a reorder and not a redesign. Pending officer meeting approval; nothing is ordered until the meeting approves the cap and names the funding line. | Sam Gerungan | [semesters/2026-fall/projects/microcontroller-lab/](../../semesters/2026-fall/projects/microcontroller-lab/README.md) |
| 2026-08-24 | The repo opens with one repo admin (@Sam-T-G) and the second admin seat open. This violates rule 7 (two admins at all times) and is treated as urgent: repo admin 1 fills the seat, updates [MAINTAINERS.md](../../MAINTAINERS.md) and `.github/CODEOWNERS`, and logs it here. Deadline: [TBD: set at the first officer meeting of Fall 2026]. | Sam Gerungan | [MAINTAINERS.md](../../MAINTAINERS.md) |
| 2026-08-24 | Repository created and its structure adopted: evergreen material in `docs/`, one folder per semester under `semesters/`, templates and scripts for creating semester, event, and meeting files, and the ten maintenance rules in [maintenance-rules.md](maintenance-rules.md). The repo is public under CC BY 4.0 for content. | Sam Gerungan | <https://github.com/Sam-T-G/rcc-acm> |
