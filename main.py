#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes one elevator pitch (a city pigeon pitching investors) to
/output/entry.txt. Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "CrumbBox delivers fresh breadcrumbs in 4 minutes, by 2,000 pigeons, "
    "for $9 a month \u2014 and our couriers already ate your last order."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
