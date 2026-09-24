#!/usr/bin/env bash
set -euo pipefail

TARGET_ALIAS="${1:-ci-target}"

if [[ -z "${SF_AUTH_URL:-}" ]]; then
  echo "ERROR: SF_AUTH_URL is not set."
  exit 1
fi

# Pipe the secret through stdin so the auth URL is not committed to disk.
printf '%s' "$SF_AUTH_URL" | sf org login sfdx-url \
  --sfdx-url-stdin \
  --alias "$TARGET_ALIAS" \
  --set-default

echo "Authenticated Salesforce target as alias: $TARGET_ALIAS"
