from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "delta")
package_file = root / "package" / "package.xml"
destructive_file = root / "destructiveChanges" / "destructiveChanges.xml"

def has_types(path: Path) -> bool:
    return path.exists() and "<types>" in path.read_text(encoding="utf-8", errors="ignore")

package_has = has_types(package_file)
destructive_has = has_types(destructive_file)

print(f"package_has_changes={'true' if package_has else 'false'}")
print(f"destructive_has_changes={'true' if destructive_has else 'false'}")
print(f"has_changes={'true' if (package_has or destructive_has) else 'false'}")

if Path("/dev/null").exists():
    pass
