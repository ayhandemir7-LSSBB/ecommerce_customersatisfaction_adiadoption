# Appends one line per agent action to logs/agent_log.md
import json, sys, os, datetime

data = json.load(sys.stdin)
inp = data.get("tool_input", {})
target = inp.get("file_path") or inp.get("notebook_path") or inp.get("command", "")
line = "| {} | {} | {} |\n".format(
    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    data.get("tool_name", ""),
    str(target).replace("|", "/")[:120],
)
root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
with open(os.path.join(root, "logs", "agent_log.md"), "a") as f:
    f.write(line)
