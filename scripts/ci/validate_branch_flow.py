import re
import sys

base = sys.argv[1] if len(sys.argv) > 1 else ""
head = sys.argv[2] if len(sys.argv) > 2 else ""

def fail(message):
    print(f"BRANCH POLICY FAILED: {message}")
    raise SystemExit(1)

def ok(message):
    print(f"BRANCH POLICY OK: {message}")
    raise SystemExit(0)

# Single-team flow
if base == "dev" and re.fullmatch(r"feature/[^/]+", head):
    ok(f"{head} -> dev")

if base == "uat" and head == "dev":
    ok("dev -> uat")

if re.fullmatch(r"release/[^/]+", base) and head == "uat":
    ok(f"uat -> {base}")

if base == "main" and re.fullmatch(r"release/[^/]+", head):
    ok(f"{head} -> main")

# Multi-team flow
m = re.fullmatch(r"dev/([^/]+)", base)
if m:
    team = m.group(1)
    if re.fullmatch(rf"feature/{re.escape(team)}/[^/]+", head):
        ok(f"{head} -> {base}")
    fail(f"Only feature/{team}/* can merge into {base}")

m = re.fullmatch(r"uat/([^/]+)", base)
if m:
    team = m.group(1)
    if head == f"dev/{team}":
        ok(f"{head} -> {base}")
    fail(f"Only dev/{team} can merge into {base}")

m = re.fullmatch(r"release/([^/]+)/([^/]+)", base)
if m:
    team = m.group(1)
    if head == f"uat/{team}":
        ok(f"{head} -> {base}")
    fail(f"Only uat/{team} can merge into {base}")

if base == "main":
    m = re.fullmatch(r"release/([^/]+)/([^/]+)", head)
    if m:
        ok(f"{head} -> main")

fail(
    "Unsupported promotion path. Allowed: "
    "feature/* -> dev -> uat -> release/<version> -> main, or "
    "feature/<team>/* -> dev/<team> -> uat/<team> -> "
    "release/<team>/<version> -> main."
)
