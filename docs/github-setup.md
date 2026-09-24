# GitHub setup

## 1. Create the repository

Create a personal repository named:

```text
salesforce-devops-reference-pipeline
```

Recommended visibility for a portfolio: public, **only if it remains fully generic and contains no real Salesforce credentials or private metadata**.

## 2. Push the downloaded reference project

```bash
git init
git add .
git commit -m "Initial generic Salesforce DevOps reference pipeline"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/salesforce-devops-reference-pipeline.git
git push -u origin main
```

## 3. Choose a branching model

### Single team

Create:

```bash
git checkout -b dev
git push -u origin dev

git checkout -b uat
git push -u origin uat
```

Release branches are created only when needed:

```bash
git checkout main
git pull
git checkout -b release/2026.09
git push -u origin release/2026.09
```

Developers create features from DEV:

```bash
git checkout dev
git pull
git checkout -b feature/ABC-101-reference-change
```

### Multiple parallel teams

Example Team A:

```bash
git checkout main
git pull
git checkout -b dev/team-a
git push -u origin dev/team-a

git checkout -b uat/team-a
git push -u origin uat/team-a
```

Example Team B:

```bash
git checkout main
git pull
git checkout -b dev/team-b
git push -u origin dev/team-b

git checkout -b uat/team-b
git push -u origin uat/team-b
```

Features must be created from the corresponding team's DEV branch:

```bash
git checkout dev/team-a
git pull
git checkout -b feature/team-a/ABC-101-reference-change
```

Release branch:

```bash
git checkout main
git pull
git checkout -b release/team-a/2026.09
git push -u origin release/team-a/2026.09
```

## 4. Create GitHub Environments

Repository -> Settings -> Environments.

Single-team environments:

```text
development
uat
staging
production
```

Multi-team example:

```text
development-team-a
uat-team-a
staging-team-a

development-team-b
uat-team-b
staging-team-b

production
```

Each GitHub Environment must contain its own:

```text
SF_AUTH_URL
```

Do not use one Salesforce credential across every environment.

## 5. Generate a personal SFDX Auth URL

Use only an org you personally own or are explicitly authorized to use.

Authenticate locally:

```bash
sf org login web --alias MyPersonalDev
```

Then display the SFDX Auth URL locally:

```bash
sf org auth show-sfdx-auth-url \
  --target-org MyPersonalDev \
  --json
```

Store the resulting `sfdxAuthUrl` only as the `SF_AUTH_URL` GitHub Environment secret.

Never commit it.

## 6. GitHub environment approvals

Recommended:

- Development: no manual approval
- UAT: optional QA/release approval
- Staging: release-owner approval
- Production: required approval and prevent self-review where available

The workflows reference GitHub Environments, so their protection rules apply before environment secrets are made available.

## 7. GitHub Rulesets / branch protection

Protect:

```text
main
dev
dev/**
uat
uat/**
release/**
```

Recommended `main` rules:

- require pull request
- require at least 2 approvals for a real team
- require conversation resolution
- require branch to be up to date before merge
- require status checks
- block force pushes
- block branch deletion
- restrict bypass permissions
- require signed commits if your policy needs them

Required status check:

```text
Branch promotion policy
Salesforce target validation
```

For DEV and UAT branches, one approval may be sufficient for a small team.

## 8. Promotion paths

The workflow rejects PRs that do not follow these paths.

Single:

```text
feature/* -> dev
dev -> uat
uat -> release/<version>
release/<version> -> main
```

Multi-team:

```text
feature/<team>/* -> dev/<team>
dev/<team> -> uat/<team>
uat/<team> -> release/<team>/<version>
release/<team>/<version> -> main
```

## 9. GitHub plan note

GitHub Environment protection capabilities depend on repository visibility and GitHub plan. If a protection option isn't available in your account, keep the workflow structure but implement the approval in PR/ruleset governance instead.
