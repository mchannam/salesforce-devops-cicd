# Release runbook

## Before promotion to UAT

Confirm:

- PR checks are green
- PMD/Code Analyzer has no blocking findings
- changed Apex tests pass
- metadata dependencies are present
- profiles and permissions are reviewed
- integration/configuration prerequisites are documented
- destructive changes are intentional
- rollback method is known

## Before release branch

Confirm:

- UAT scope is frozen
- defects are triaged
- deployment sequence is known
- manual steps are documented
- data migration is documented separately
- owners are assigned
- post-deployment smoke tests are defined

## Before Production

Confirm:

- release -> main PR has completed production validation
- approval is recorded
- Production environment is not being deployed by another team
- backup/retrieval requirements are complete
- rollback decision owner is available
- post-deploy verification owner is available

## After Production

Perform:

1. deployment-status verification
2. Apex/test verification
3. targeted smoke tests
4. integration checks
5. permission/access checks
6. release communication
7. tag the release if your versioning policy requires it

Example:

```bash
git checkout main
git pull
git tag -a v2026.09.0 -m "Release 2026.09.0"
git push origin v2026.09.0
```
