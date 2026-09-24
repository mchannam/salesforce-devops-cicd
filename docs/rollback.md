# Rollback strategy

Salesforce metadata rollback is not equivalent to a database transaction rollback.

Use a layered strategy.

## 1. Git revert

If the release consists only of safely reversible metadata:

```bash
git checkout main
git pull
git revert <merge-commit-sha>
git push origin rollback/<release>
```

Open the rollback branch through the same validation and approval controls.

## 2. Forward fix

Prefer a forward fix when reverting would create additional risk, especially when:

- data shape changed
- integrations depend on the new contract
- permissions were already consumed
- metadata deletion/recreation is unsafe
- post-deployment data jobs ran

## 3. Pre-release retrieval or backup

For critical metadata, use an approved backup/retrieval procedure before the release. Keep backups outside this public reference repository.

## 4. Destructive changes

Treat destructive metadata changes as higher risk.

Require:

- explicit review
- dependency analysis
- recovery approach
- data-impact assessment
- post-deployment verification

## 5. Production decision

Define the release owner who can choose between:

- continue
- forward fix
- metadata revert
- feature disablement
- integration disablement
- full incident procedure

Do not improvise Production rollback during an incident.
