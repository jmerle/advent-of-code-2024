import click

from aoc2024.commands.common import PROJECT_ROOT, get_day_directory

PYTHON_TEMPLATE = """
import re
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from math import *


def main() -> None:
    data = sys.stdin.read().strip()


if __name__ == "__main__":
    main()
""".strip()


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
def new(day: int) -> None:
    """Creates skeleton files for the given day."""
    day_directory = get_day_directory(day)
    if day_directory.is_dir():
        raise ValueError(f"{day_directory} already exists")

    day_directory.mkdir(parents=True)

    for file, content in [
        (day_directory / "example.txt", ""),
        (day_directory / "full.txt", ""),
        (day_directory / "part1.py", PYTHON_TEMPLATE + "\n"),
        (day_directory / "part2.py", PYTHON_TEMPLATE + "\n"),
    ]:
        with file.open("w+", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully created {file.relative_to(PROJECT_ROOT)}")
