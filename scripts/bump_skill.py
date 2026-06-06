#!/usr/bin/env python3
"""
Bump the pinned `sha` of skills in marketplace.json to the latest commit of
their tracked ref.

Use this only for skills you own and trust — it advances the pinned sha to
whatever is at the top of the skill's ref (default: its `ref`, usually main).
Third-party skills must NOT be auto-bumped; their sha changes only via a
reviewed PR. The `--owned <owner>` filter restricts bumping to repos under that
GitHub owner.

Usage:
  python3 scripts/bump_skill.py <plugin-name>      # bump one skill
  python3 scripts/bump_skill.py --owned <owner>    # bump all skills under <owner>

Exit code 0 always (no changes is fine). Writes marketplace.json in place.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP = os.path.join(ROOT, ".claude-plugin", "marketplace.json")


def repo_url_and_ref(src):
    """Return (clone_url, ref) for a dict source, or (None, None) if inline/unsupported."""
    if not isinstance(src, dict):
        return None, None
    ref = src.get("ref", "main")
    kind = src.get("source")
    if kind in ("git-subdir", "url"):
        return src.get("url"), ref
    if kind == "github":
        repo = src.get("repo", "")
        return f"https://github.com/{repo}.git", ref
    return None, None


def owner_of(src):
    url, _ = repo_url_and_ref(src)
    if not url:
        return None
    m = re.search(r"github\.com[:/]+([^/]+)/", url)
    return m.group(1) if m else None


def latest_sha(url, ref):
    out = subprocess.run(
        ["git", "ls-remote", url, ref], capture_output=True, text=True, check=True
    ).stdout.strip()
    if not out:
        raise RuntimeError(f"ref {ref!r} not found at {url}")
    return out.split()[0]


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)

    owned = None
    target_name = None
    if args[0] == "--owned":
        if len(args) < 2:
            print("--owned requires an owner"); sys.exit(2)
        owned = args[1]
    else:
        target_name = args[0]

    mp = json.load(open(MP))
    changed = []
    for p in mp.get("plugins", []):
        name = p.get("name")
        src = p.get("source")
        if target_name and name != target_name:
            continue
        url, ref = repo_url_and_ref(src)
        if not url:
            if target_name:
                print(f"skip {name}: inline or unsupported source")
            continue
        if owned and owner_of(src) != owned:
            continue
        new = latest_sha(url, ref)
        old = src.get("sha")
        if old != new:
            src["sha"] = new
            changed.append((name, old, new))
            print(f"bump {name}: {(old or 'none')[:10]} -> {new[:10]}")
        else:
            print(f"ok   {name}: already at {new[:10]}")

    if changed:
        with open(MP, "w") as f:
            json.dump(mp, f, indent=2)
            f.write("\n")
        print(f"\nUpdated {len(changed)} skill(s) in marketplace.json.")
    else:
        print("\nNo changes.")


if __name__ == "__main__":
    main()
