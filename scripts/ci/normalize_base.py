import subprocess
import sys

candidate = sys.argv[1] if len(sys.argv) > 1 else ""
head = sys.argv[2] if len(sys.argv) > 2 else "HEAD"

def exists(ref):
    if not ref or set(ref) == {"0"}:
        return False
    return subprocess.run(
        ["git", "rev-parse", "--verify", ref],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ).returncode == 0

if exists(candidate):
    print(candidate)
    raise SystemExit(0)

# New branch / unusual push: use parent commit where possible.
parent = f"{head}~1"
if exists(parent):
    print(parent)
    raise SystemExit(0)

# Initial commit fallback.
root = subprocess.check_output(
    ["git", "rev-list", "--max-parents=0", head],
    text=True
).strip().splitlines()[0]
print(root)
