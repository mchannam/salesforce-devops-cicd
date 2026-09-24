import re
import sys

branch = sys.argv[1] if len(sys.argv) > 1 else ""

def safe_team(value):
    return re.sub(r"[^a-zA-Z0-9-]", "-", value).lower()

if branch == "dev":
    env = "development"
elif branch.startswith("dev/"):
    team = safe_team(branch.split("/", 1)[1])
    env = f"development-{team}"
elif branch == "uat":
    env = "uat"
elif branch.startswith("uat/"):
    team = safe_team(branch.split("/", 1)[1])
    env = f"uat-{team}"
elif branch.startswith("release/"):
    parts = branch.split("/")
    if len(parts) >= 3:
        team = safe_team(parts[1])
        env = f"staging-{team}"
    else:
        env = "staging"
elif branch == "main":
    env = "production"
else:
    print(f"Unsupported target branch: {branch}", file=sys.stderr)
    raise SystemExit(2)

print(f"github_environment={env}")
print("target_alias=ci-target")
