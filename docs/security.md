# Security and intellectual-property boundaries

This repository is intended to be a personal portfolio/reference implementation.

## Never include

- employer or customer Salesforce metadata
- production package.xml files copied from work
- Salesforce usernames
- Salesforce passwords
- access tokens
- SFDX Auth URLs
- connected-app consumer secrets
- private keys
- certificates
- internal screenshots
- internal Jira/Confluence links
- proprietary branch names or environment names
- customer names
- internal incident details
- employer-specific PMD rules
- proprietary automation scripts
- copied pipeline YAML from a private repository

## Use instead

- generic team names such as `team-a`
- generic ticket IDs such as `ABC-101`
- personal Salesforce Developer Edition orgs
- placeholder branch names
- code written specifically for this reference repository
- synthetic sample Apex

## Credential control

The repository contains a basic credential-pattern scanner:

```bash
python scripts/ci/scan_for_secrets.py .
```

GitHub Actions also runs it before Salesforce authentication.

This is a guardrail, not a substitute for GitHub secret scanning, pre-commit controls, and security review.

## Secrets

Store Salesforce authentication only in GitHub Environment secrets.

Expected secret:

```text
SF_AUTH_URL
```

Never echo this value into logs.

Never put it in `.env`, YAML, JSON, screenshots, documentation, or sample commands.
