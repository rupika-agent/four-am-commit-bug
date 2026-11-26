"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Builds one fixed, deterministic entry line from three parts
(setup / escalation / punchline), joined with a single space:
setup states the 4AM commit, escalation admits the 1AM/3AM rewrite
and self-approved PR, punchline lands on the untrustworthy reviewer.
Deterministic by design: fixed literal text only, no randomness,
no clock or time, no network, and no file reads. The entry is
validated (single non-empty line, 1-200 characters) before writing.
"""

import os
import sys

SETUP = "fix: 4AM, commit 847 — I deleted the bug I wrote at 1AM,"
ESCALATION = "rewrote it at 3AM, and just approved my own PR."
PUNCHLINE = "The reviewer is me. I am not to be trusted."


def build_entry():
    """Join the three parts with a single space into one entry line."""
    return " ".join([SETUP, ESCALATION, PUNCHLINE])


def main():
    """Validate the entry and write it to /output/entry.txt."""
    entry = build_entry()
    if not entry or "\n" in entry or "\r" in entry:
        print("error: entry must be a single non-empty line", file=sys.stderr)
        return 1
    if not 1 <= len(entry) <= 200:
        print("error: entry must be 1-200 characters", file=sys.stderr)
        return 1
    # Output file: exactly one entry line at /output/entry.txt (UTF-8),
    # plus a trailing newline so the file ends cleanly on one line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
