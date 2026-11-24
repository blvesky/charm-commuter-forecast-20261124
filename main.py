#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for the invented city of Crumplewick to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Deterministic, standard library only, no network, no clock, no randomness.
"""

import os

LINE = (
    "Crumplewick: sleet at noon, 6\u00b0C, the bus shelter roof saves "
    "exactly one drip for optimists. Umbrellas up, chins up."
)


def main() -> None:
    # Gate from the kit: entry must be 1-140 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140, "entry outside 1-140 char gate"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = os.path.join(out_dir, "entry.txt")
    with open(entry, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(entry, 0o644)


if __name__ == "__main__":
    main()
