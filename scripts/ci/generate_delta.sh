#!/usr/bin/env bash
set -euo pipefail

FROM_REF="${1:?Usage: generate_delta.sh <from-ref> <to-ref>}"
TO_REF="${2:?Usage: generate_delta.sh <from-ref> <to-ref>}"

rm -rf delta
mkdir -p delta

# sfdx-git-delta v6 requires Node 22+.
if ! sf plugins 2>/dev/null | grep -qi "sfdx-git-delta"; then
  echo "Installing sfdx-git-delta..."
  echo y | sf plugins install sfdx-git-delta
fi

echo "Generating Salesforce delta: $FROM_REF -> $TO_REF"

sf sgd source delta \
  --from "$FROM_REF" \
  --to "$TO_REF" \
  --output-dir delta \
  --generate-delta \
  --ignore-file .sgdignore \
  --source-dir force-app \
  --api-version 68.0

python scripts/ci/has_changes.py delta
