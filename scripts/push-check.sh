#!/usr/bin/env bash
# scripts/sync.sh push runs this instead of scripts/check.sh. check.sh reads the working tree, so
# here it runs on exactly what is being pushed (HEAD's tracked files): untracked drafts, scratch,
# and build output can neither fail a push nor slip past it.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
git archive HEAD | tar -x -C "$tmp"
"$tmp/scripts/check.sh"
