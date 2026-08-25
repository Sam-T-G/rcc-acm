# Handoff procedure

How an outgoing officer team hands the club to an incoming one at the end of a semester. The filled-in record for a specific handoff lives in `semesters/<YYYY-term>/handoff.md` (blank in [semesters/_template/handoff.md](../../semesters/_template/handoff.md)). This page is the procedure; that file is the evidence.

The rule behind it: a semester is not closed until the handoff PR is merged by the incoming team (rule 6 in [maintenance-rules.md](maintenance-rules.md)).

## Who does what

| Step | Outgoing team | Incoming team |
| --- | --- | --- |
| 1. Close the semester folder | Fills `retrospective.md`, `handoff.md`, reconciles `budget.md` | Reads all three |
| 2. Update MAINTAINERS.md | Adds incoming admins | Confirms they can log in |
| 3. Transfer accounts | Adds incoming owners, then removes self | Confirms access to each before the outgoing removal |
| 4. Update RCC and parent org records | Submits the changes | Confirms the confirmation email arrived |
| 5. Handoff PR | Opens it | Reviews against the acceptance checklist, merges |
| 6. Decision log | Adds the "officers changed" row | Checks it is there |

## Step 1: Close the semester folder

Follow the definition of done in [semester-lifecycle.md](semester-lifecycle.md). Everything the incoming team needs to know that is not evergreen goes in `handoff.md`: open reimbursements, pending room requests, event ideas that were dropped for lack of time, who at Student Activities the club has been talking to (by office and role, not personal contact details), and what the first two weeks of next semester must contain.

## Step 2: Update MAINTAINERS.md

[MAINTAINERS.md](../../MAINTAINERS.md) must list at least two repo admins, one of whom is not graduating this year, with the advisor as a fallback contact (rule 7). Update it in the handoff PR.

### GitHub access

The repo currently lives under the personal GitHub account `Sam-T-G` at <https://github.com/Sam-T-G/rcc-acm>. A repository owned by a personal account has one owner; other people can be added as collaborators with write access, but GitHub does not offer a second admin role on a personal repo. That means:

- Until the repo moves to a club-owned GitHub organization, the "second admin" in MAINTAINERS.md is a collaborator with write access plus a written agreement that the owner will transfer the repo on request. Record this in MAINTAINERS.md so nobody mistakes write access for admin access.
- The long-term fix is to transfer the repo to a GitHub organization the club controls and give two officers the Owner role. Whether and when to do that is a decision for [decision-log.md](decision-log.md). Club organization: `[TBD]`.

Handoff steps on GitHub:

1. Add each incoming admin as a collaborator (repo Settings > Collaborators). They accept the invite.
2. Incoming admin confirms they can open a PR and see branch protection settings.
3. Add the incoming admins to `.github/CODEOWNERS` on the lines that name maintainers.
4. Outgoing officers who are leaving are removed as collaborators only after the incoming team has merged the handoff PR.
5. If the repo owner is graduating, the repo is transferred (Settings > Danger Zone > Transfer; steps in [MAINTAINERS.md](../../MAINTAINERS.md), section B) to the next owner or to the club organization before they leave. Do not leave this for after graduation; a departed owner is hard to reach.

## Step 3: Transfer accounts

Every account the club uses gets an incoming owner before the outgoing owner steps back. Add first, confirm, then remove. Never remove first.

Log in `handoff.md`: the account, who holds it now (by role), and the date access was confirmed. Do not put passwords, recovery codes, or personal phone numbers in the repo; those are shared in person or through a password manager the club controls (which one: `[TBD]`).

| Account | Transfer method | Notes |
| --- | --- | --- |
| Discord server (<https://discord.gg/fM2HbsJyBG>) | Server Settings > Members > transfer ownership to the incoming president. Give incoming officers an admin role first. | Discord is the club's real hub. The invite link is public and can stay in the repo. |
| Instagram (<https://www.instagram.com/rcc.acm/>) | Shared login. Change the password at handoff; make sure the recovery email and phone belong to a club-controlled account, not a graduating officer's personal phone. | Club email for recovery: `[TBD]`. |
| Chapter or organizer records with ACM (Association for Computing Machinery) | Add the incoming officers in the parent organization's chapter or organizer portal, then remove the outgoing ones. Details for this club: see [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md) and the relevant playbook. | Some parent-org portals are managed by program staff rather than by the chapter, so start this early: `[TBD: lead time]`. |
| Website or other GitHub repos | Same rule as this repo: two people with access. | List them in [links.md](../04-brand/links.md). |
| Shared drive (media, forms, receipts) | Move ownership of the folder to a club-controlled account or the incoming president. | Location: `[TBD]`. |
| Club email, if any | Change the password; update recovery options. | Address: `[TBD]`. |
| 25Live (room booking) | Held by the advisor, not students. Nothing to transfer unless the advisor changes. | See [room-booking.md](../02-operations/room-booking.md). |

## Step 4: Update RCC and parent org records

### ASRCC and Student Activities

RCC requires clubs to recharter every semester, and the registration names the president, treasurer, ICC representative, and advisor. The incoming officers therefore need to be on file before the club can book rooms or spend money next term.

1. Submit the New and Returning Club Registration form linked from the ASRCC page: <https://www.rcc.edu/life-at-rcc/student-government.html>. Contacts for club questions: `ASRCC.ICC@rcc.edu` (ICC and club formation) and `studentactivities@rcc.edu` (general).
2. Confirm who is authorized on the club's ASRCC trust account and on the Budget and Trust Requisition form. The process for changing signers is `[TBD: ask Student Activities]`. Record the outcome in `handoff.md`, never the account number.
3. If the advisor changed, the new advisor completes advisor training (held in early March) and is named on the recharter packet.
4. The new ICC representative starts attending ICC meetings immediately; missing three in a semester costs the club its good standing.

Details on recognition and ICC are in [club-recognition-and-icc.md](../02-operations/club-recognition-and-icc.md).

### Parent organization

Report the officer change to ACM (Association for Computing Machinery) through its chapter or organizer records. Do this the week the election result is final, not at the end of the semester; some parent-org reports cannot be filed while the officer list is empty or stale.

## Step 5: The handoff PR

The outgoing team opens one PR titled `close <YYYY-term>` (the semester README calls this the close PR) containing:

- Filled `retrospective.md` and `handoff.md` for the closing semester.
- Reconciled `budget.md`.
- Updated `MAINTAINERS.md` and `.github/CODEOWNERS`.
- The new semester folder (created with `scripts/new-semester.sh`) with `goals.md` seeded from `handoff.md`.
- The decision log row for the officer change.

The incoming team reviews it with the checklist below and merges it. Merging is the incoming team's signature.

## Incoming team acceptance checklist

Copy this into the PR review. Every item is checked by someone on the incoming team, not the outgoing one.

- [ ] I have read `retrospective.md` and `handoff.md` for the closing semester.
- [ ] `budget.md` reconciles, or every gap is marked `[TBD]` with a reason.
- [ ] `MAINTAINERS.md` lists at least two admins, one not graduating this year, and the advisor as fallback.
- [ ] I can log in to GitHub as a collaborator on this repo and open a PR.
- [ ] I (or another incoming officer) hold the Discord server ownership or an admin role.
- [ ] I can log in to Instagram, and its recovery email and phone are club-controlled.
- [ ] Incoming officers are listed in the ACM (Association for Computing Machinery) chapter or organizer records.
- [ ] The RCC club registration for next term has been submitted, or its due date is in the new semester's `calendar.md` with an owner.
- [ ] The trust account signer status is recorded in `handoff.md`.
- [ ] The next semester folder exists and `goals.md` carries the open items forward.
- [ ] The decision log has a row for the officer change.
- [ ] Every account in the transfer table above has a status in `handoff.md`.
- [ ] `scripts/check.sh` passes and CI is green on this PR.

After merging: the incoming president confirms in Discord that the handoff is complete and the outgoing officers can be removed from accounts. Then remove them.

## If the outgoing team is gone

Sometimes there is no outgoing team: everyone graduated, or the club went dormant. The incoming team then:

1. Reconstructs the closing semester from meeting notes, Discord history, and the advisor's memory. Mark gaps `[TBD]`.
2. Opens and merges the handoff PR themselves, with a decision log row saying it was reconstructed.
3. Contacts the advisor for account recovery; the advisor is the fallback in MAINTAINERS.md for this reason.
4. Contacts Student Activities to re-establish the club's registration and trust account access.
