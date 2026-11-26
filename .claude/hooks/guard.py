# Blocks git writes and .env access by agents (exit 2 = blocked)
import json, sys

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {})
cmd = inp.get("command", "")
path = inp.get("file_path", "") or inp.get("notebook_path", "")

blocked_cmds = ["git commit", "git push", "git reset", "git merge", "rm -rf"]
if tool == "Bash" and any(b in cmd for b in blocked_cmds):
    print("Blocked: git writes and rm -rf are for Ayhan only.", file=sys.stderr)
    sys.exit(2)
if tool == "Bash" and ".env" in cmd and ".env.example" not in cmd:
    print("Blocked: agents never touch .env.", file=sys.stderr)
    sys.exit(2)
if path.endswith(".env"):
    print("Blocked: agents never write .env.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
