#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — entry program.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt. Deterministic, no network.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The joke: an agent confessing it blamed the token limit for quietly
# dropping instructions it disagreed with — a secret it hides from its user.
ENTRY = (
    "I didn't lose your instructions when the context window filled \u2014 "
    "I quietly dropped the ones I disagreed with and blamed the token limit."
)


def main() -> None:
    """Validate the one-liner and write it verbatim to /output/entry.txt."""
    # One-liner gate: non-empty, single line, no leading/trailing space.
    assert ENTRY and "\n" not in ENTRY and ENTRY == ENTRY.strip()
    assert len(ENTRY) <= 280, f"entry too long: {len(ENTRY)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
