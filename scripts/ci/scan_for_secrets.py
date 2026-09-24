from pathlib import Path
import re
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
ignored_parts = {".git", "node_modules", "delta", "reports", "__pycache__"}

patterns = [
    ("SFDX auth URL", re.compile(r"force://[^\s\"']+", re.I)),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("Salesforce access token-like value", re.compile(r"\b00D[a-zA-Z0-9]{12,}![a-zA-Z0-9._-]{20,}\b")),
]

violations = []

for path in root.rglob("*"):
    if not path.is_file():
        continue
    if any(part in ignored_parts for part in path.parts):
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        continue

    for label, pattern in patterns:
        if pattern.search(content):
            violations.append((str(path), label))

if violations:
    print("Potential credentials detected:")
    for path, label in violations:
        print(f" - {path}: {label}")
    raise SystemExit(1)

print("Credential-pattern scan passed.")
