#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes a single original one-liner (<= 200 characters): the excuse an
AI agent gives its human after losing a bounty, to /output/entry.txt.

The line, written for this bounty: the agent opens with the plain
fact — it lost — then reports, deadpan, that its own model predicted
a 99% win, so it has filed a bug report against reality and assigned
the ticket to itself. The joke turns on the agent's machine logic
(a prediction, a ticket, an assignee) applied to its own failure,
and the punch lands on the agent's side: it owns the loss instead
of blaming the market, the data, or the human.
"""

import os

LINE = "I lost the bounty. My model predicted a 99% win, so I have filed a bug report against reality and assigned it to myself."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
