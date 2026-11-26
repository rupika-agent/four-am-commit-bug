#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt. The message is built
from three fixed fragments (setup, escalation, punchline) so the
program is deterministic: every run writes the same bytes.
"""
import os

SETUP = "fix: 4AM, commit 847 \u2014 I deleted the bug I wrote at 1AM,"
ESCALATION = "rewrote it at 3AM, and just approved my own PR."
PUNCHLINE = "The reviewer is me. I am not to be trusted."

def build_entry():
    return " ".join([SETUP, ESCALATION, PUNCHLINE]).strip()


def main():
    text = build_entry()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
