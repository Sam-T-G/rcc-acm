# Maintainers

Who holds the keys to this repo and how the keys move. Keep this file current; it is the first thing an incoming team reads when the outgoing team is gone.

Last reviewed: 2026-08-24

## Current roles

Names appear only with the person's consent on file (see [docs/01-governance/privacy-and-public-repo-policy.md](docs/01-governance/privacy-and-public-repo-policy.md)). A GitHub handle counts as public once that person has accepted a role on this repo.

| Role | GitHub handle | Name (with consent) | Term ends | Graduating this year? |
| --- | --- | --- | --- | --- |
| Repo admin 1 | @Sam-T-G | Sam Gerungan | [TBD] | [TBD] |
| Repo admin 2 | [TBD: see the 2026-08-24 single-admin entry in the [decision log](docs/01-governance/decision-log.md)] | [TBD] | [TBD] | [TBD] |
| President / lead | [TBD] | [TBD] | [TBD] | [TBD] |
| Secretary / docs officer | [TBD] | [TBD] | [TBD] | [TBD] |
| Treasurer | [TBD] | [TBD] | [TBD] | [TBD] |
| Advisor (fallback contact) | [TBD] | [TBD] | n/a | n/a |

What each role does for the repo:

- Repo admins: hold GitHub admin rights, keep branch protection on, merge semester-close PRs, and run the transfer steps below.
- President / lead: final say on go/no-go decisions in the decision log; reviews PRs.
- Secretary / docs officer: owns meeting notes, the decision log, and this file; reviews PRs.
- Treasurer: owns `budget.md` in each semester folder and [docs/02-operations/asrcc-funding.md](docs/02-operations/asrcc-funding.md); reviews budget PRs.
- Advisor: fallback contact when both admins are unreachable. Does not need to edit the repo, but should have a GitHub account with write access so the repo is never orphaned.

## Succession rule

1. At least two repo admins at all times. At least one of them is not graduating or transferring this academic year.
2. Add before you remove. A new admin is added, confirmed, and listed here before the outgoing admin loses access.
3. Review this table at every election and at every semester close. The semester-close handoff PR ([docs/01-governance/handoff-procedure.md](docs/01-governance/handoff-procedure.md)) is not complete until this file matches reality.
4. Every admin change gets a one-line entry in [docs/01-governance/decision-log.md](docs/01-governance/decision-log.md): date, who was added or removed, who approved.
5. If both admins are gone and nobody can reach them, the advisor contacts GitHub Support or ACM (Association for Computing Machinery) for help recovering the account. Avoid ever needing this by following succession rules 1 and 2 above (two admins, add before remove).

## What "admin" means depends on where the repo lives

This repo lives at https://github.com/Sam-T-G/rcc-acm, under a personal GitHub account. GitHub's rules for personal-account repos (verified 2026-08-24 against GitHub Docs, "Permission levels for a personal account repository": <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/permission-levels-for-a-personal-account-repository>):

- Collaborators can pull and push. That is the only access level a personal repo can grant.
- Only the owner can invite collaborators, change visibility, delete the repo, or transfer it.

So under a personal account, "repo admin 2" is a write collaborator who is the designated transfer target, and only the owner is a true admin. That satisfies the two-admins rule in spirit, but one person can still lock everyone out by disappearing.

The durable fix is to move the repo into a GitHub organization owned by the club, where two or more people can hold the Admin role at the same time. Whether and when to do that is a decision for the decision log: [TBD].

## How to transfer admin rights on GitHub

Steps verified against GitHub Docs on 2026-08-24: <https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository> and <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/permission-levels-for-a-personal-account-repository>. Menu labels are quoted as they appear.

### A. Add a collaborator (repo under a personal account)

Only the owner can do this.

1. Open the repo main page and click "Settings".
2. In the "Access" section, click "Collaborators".
3. Click "Add people".
4. Search for the person's GitHub handle and select it.
5. Click "Add NAME to REPOSITORY".
6. The person accepts the invitation from their GitHub notifications or email. Until they accept, they have no access.
7. Update the table above and open a PR for it.

### B. Transfer ownership (repo under a personal account)

Use this when the owner leaves, or to move the repo into a club organization. Requires admin access (the owner). Transferring into an organization also requires permission to create repos in that organization.

1. Open the repo main page and click "Settings".
2. Scroll to the bottom to the "Danger Zone" section.
3. Click "Transfer".
4. Choose the new owner: an organization or a user handle.
5. Type the repo name to confirm.
6. Click "I understand, transfer this repository".

What moves with the repo: issues, pull requests, wiki, stars, watchers, and Git history. Webhooks, secrets, and deploy keys stay attached. Old links and Git remotes redirect to the new location. The previous owner becomes a collaborator; other collaborators keep their access (read-only collaborators are dropped only when transferring to a personal account).

After the transfer: update `https://github.com/Sam-T-G/rcc-acm` references in the docs, re-check branch protection (step D), and update this file.

### C. Grant or change the Admin role (repo inside an organization)

1. Open the repo main page and click "Settings".
2. In the "Access" section, click "Collaborators & teams".
3. To add someone: click "Add people", search for the handle, and under "Choose a role" pick "Admin" (or "Write" for a non-admin officer). Click "Add NAME to REPOSITORY".
4. To change someone's role: under "Manage access", find the person, open the "Role" dropdown next to their name, and pick the new role.
5. To remove someone: under "Manage access", click "Remove" next to their name. Do this only after the replacement is in place.

Roles available in an organization repo: Read, Triage, Write, Maintain, Admin. "Admin" is the only one that can change settings, manage access, and delete the repo.

### D. Settings that go with admin rights

Check these after any transfer or admin change. They live under "Settings" for the repo.

- [ ] Branch protection on `main`: pull request required, at least one approving review, review from code owners required, status checks `markdownlint` and `links` required.
- [ ] `.github/CODEOWNERS` lists every current admin handle.
- [ ] Both admins can open "Settings" (if they cannot, they are not admins).
- [ ] The table above and the decision log are updated in the same PR.

## Other accounts this repo does not control

GitHub is one key among several. Discord, Instagram, the club website, the shared drive, the ACM (Association for Computing Machinery) chapter portal, and any trust-account signer list each have their own owner. The semester `handoff.md` (from `semesters/_template/handoff.md`) lists them with their current holder role and the transfer status. Keep credentials out of this repo entirely.
