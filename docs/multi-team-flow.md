# Multiple parallel teams

This model is for teams that need separate lower-environment promotion lanes while sharing one production branch.

## Example

```text
Team A
feature/team-a/* -> dev/team-a -> uat/team-a -> release/team-a/2026.09 -> main

Team B
feature/team-b/* -> dev/team-b -> uat/team-b -> release/team-b/2026.09 -> main

Team C
feature/team-c/* -> dev/team-c -> uat/team-c -> release/team-c/2026.09 -> main
```

## Why this model

A single shared `dev` branch is simple, but it couples all teams to the same release train. If Team A is ready and Team B has unfinished changes already merged into shared DEV, selectively promoting Team A becomes difficult.

Team-specific lanes avoid that problem.

## Team environments

For each team create:

```text
development-<team>
uat-<team>
staging-<team>
```

Example:

```text
development-team-a
uat-team-a
staging-team-a
```

Each environment should point only to the Salesforce org assigned to that lane.

## Production serialization

All teams ultimately open:

```text
release/<team>/<version> -> main
```

`main` is the single Production source of truth.

The production workflow uses:

```text
concurrency group = salesforce-production
```

This prevents two team production deployments from running at the same time.

## Cross-team dependency rules

Before promoting a release:

1. Identify dependencies on metadata owned by another team.
2. Confirm the dependency is already available in `main` or intentionally included in the release.
3. Do not cherry-pick dependent metadata blindly.
4. Rebase or merge the latest `main` into the team lane before final production PR.
5. Resolve metadata conflicts before the release PR is approved.
6. Run the production validation again after conflict resolution.

## Keeping team lanes current

At the start of a sprint/release, sync `main` into the team DEV branch:

```bash
git checkout dev/team-a
git fetch origin
git merge origin/main
git push
```

Then team features branch from that refreshed team DEV branch.

## When to use a shared lane instead

Use the single-team/shared model if:

- all developers release together
- there is one UAT cadence
- incomplete features are kept out of DEV
- feature flags isolate unfinished functionality
- selective promotion isn't required

Use parallel team lanes if teams have materially independent release cadences or separate lower Salesforce orgs.
