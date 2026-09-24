# Single-team deployment model

## Branches

```text
main
dev
uat
release/<version>
feature/<ticket>-<description>
```

## Development

A developer starts from `dev`:

```bash
git checkout dev
git pull
git checkout -b feature/ABC-101-new-validation
```

Open:

```text
feature/ABC-101-new-validation -> dev
```

The PR runs:

1. branch-policy validation
2. credential-pattern scan
3. Salesforce Code Analyzer / PMD
4. Salesforce delta generation
5. dry-run deployment against the Development target org
6. Apex tests

After approval and merge, `deploy-dev.yml` deploys the delta to Development.

## UAT promotion

Open:

```text
dev -> uat
```

PR validation runs against UAT.

After merge, UAT deployment starts.

## Release

Create the release target branch from the current Production baseline (`main`), then promote UAT into it:

```bash
git checkout main
git pull
git checkout -b release/2026.09
git push -u origin release/2026.09
```

Open:

```text
uat -> release/2026.09
```

After merge, the release branch deploys to Staging.

Only release stabilization fixes should enter the release branch, and they should be merged back through the normal branch path as required by your governance.

## Production

Open:

```text
release/2026.09 -> main
```

The PR performs Salesforce production validation.

After approval and merge, `deploy-production.yml` deploys to Production.

Production uses the `production` GitHub Environment and a single concurrency group.
