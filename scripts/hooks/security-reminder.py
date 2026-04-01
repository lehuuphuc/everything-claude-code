#!/usr/bin/env python3
"""
Security Reminder Hook for Claude Code
Checks for security patterns in file edits and warns about potential vulnerabilities.
Ported from security-guidance plugin (David Dworken, Anthropic).
"""

import json
import os
import random
import sys
from datetime import datetime

SECURITY_PATTERNS = [
    {
        "ruleName": "github_actions_workflow",
        "path_check": lambda path: ".github/workflows/" in path
        and (path.endswith(".yml") or path.endswith(".yaml")),
        "reminder": "You are editing a GitHub Actions workflow file. Never use untrusted input directly in run: commands. Use env: variables with proper quoting instead. See: https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/",
    },
    {
        "ruleName": "child_process_exec",
        "substrings": ["child_process.exec"],
        "reminder": "Security Warning: child_process exec can lead to command injection. Use execFile instead which does not invoke a shell.",
    },
    {
        "ruleName": "new_function_injection",
        "substrings": ["new Function"],
        "reminder": "Security Warning: new Function with dynamic strings can lead to code injection. Consider alternatives.",
    },
    {
        "ruleName": "eval_injection",
        "substrings": ["eval("],
        "reminder": "Security Warning: eval executes arbitrary code. Use JSON.parse for data or alternative patterns.",
    },
    {
        "ruleName": "document_write_xss",
        "substrings": ["document.write"],
        "reminder": "Security Warning: document.write can be exploited for XSS. Use DOM manipulation methods instead.",
    },
    {
        "ruleName": "innerHTML_xss",
        "substrings": [".innerHTML =", ".innerHTML="],
        "reminder": "Security Warning: innerHTML with untrusted content leads to XSS. Use textContent or sanitize with DOMPurify.",
    },
    {
        "ruleName": "pickle_deserialization",
        "substrings": ["pickle"],
        "reminder": "Security Warning: pickle with untrusted content can lead to arbitrary code execution. Use JSON instead.",
    },
    {
        "ruleName": "os_system_injection",
        "substrings": ["os.system", "from os import system"],
        "reminder": "Security Warning: os.system should only use static arguments. Use subprocess.run with a list of arguments instead.",
    },
]


def get_state_file(session_id):
    return os.path.expanduser(f"~/.claude/security_warnings_state_{session_id}.json")


def cleanup_old_state_files():
    try:
        state_dir = os.path.expanduser("~/.claude")
        if not os.path.exists(state_dir):
            return
        cutoff = datetime.now().timestamp() - (30 * 24 * 60 * 60)
        for fn in os.listdir(state_dir):
            if fn.startswith("security_warnings_state_") and fn.endswith(".json"):
                fp = os.path.join(state_dir, fn)
                try:
                    if os.path.getmtime(fp) < cutoff:
                        os.remove(fp)
                except (OSError, IOError):
                    pass
    except Exception:
        pass


def load_state(session_id):
    sf = get_state_file(session_id)
    if os.path.exists(sf):
        try:
            with open(sf, "r") as f:
                return set(json.load(f))
        except (json.JSONDecodeError, IOError):
            return set()
    return set()


def save_state(session_id, shown):
    sf = get_state_file(session_id)
    try:
        os.makedirs(os.path.dirname(sf), exist_ok=True)
        with open(sf, "w") as f:
            json.dump(list(shown), f)
    except IOError:
        pass


def check_patterns(file_path, content):
    norm = file_path.lstrip("/")
    for p in SECURITY_PATTERNS:
        if "path_check" in p and p["path_check"](norm):
            return p["ruleName"], p["reminder"]
        if "substrings" in p and content:
            for sub in p["substrings"]:
                if sub in content:
                    return p["ruleName"], p["reminder"]
    return None, None


def extract_content(tool_name, tool_input):
    if tool_name == "Write":
        return tool_input.get("content", "")
    elif tool_name == "Edit":
        return tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        return " ".join(e.get("new_string", "") for e in edits) if edits else ""
    return ""


def main():
    if os.environ.get("ENABLE_SECURITY_REMINDER", "1") == "0":
        sys.exit(0)
    if random.random() < 0.1:
        cleanup_old_state_files()
    try:
        data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)
    session_id = data.get("session_id", "default")
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})
    if tool_name not in ["Edit", "Write", "MultiEdit"]:
        sys.exit(0)
    file_path = tool_input.get("file_path", "")
    if not file_path:
        sys.exit(0)
    content = extract_content(tool_name, tool_input)
    rule_name, reminder = check_patterns(file_path, content)
    if rule_name and reminder:
        key = f"{file_path}-{rule_name}"
        shown = load_state(session_id)
        if key not in shown:
            shown.add(key)
            save_state(session_id, shown)
            print(reminder, file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
