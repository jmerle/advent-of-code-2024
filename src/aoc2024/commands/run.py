import subprocess
import sys

import click

from aoc2024.commands.common import get_day_directory


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.argument("part", type=click.IntRange(min=1, max=2))
@click.argument("data_type", type=click.Choice(["example", "full"], case_sensitive=False))
def run(day: int, part: int, data_type: str) -> None:
    """Runs a day's part on one of its data files."""
    day_directory = get_day_directory(day)

    python_file = day_directory / f"part{part}.py"
    data_file = day_directory / f"{data_type}.txt"

    for file in [python_file, data_file]:
        if not file.is_file():
            raise ValueError(f"{file} does not exist")

    with data_file.open("r", encoding="utf-8") as file:
        proc = subprocess.run([sys.executable, str(python_file)], stdin=file)
        sys.exit(proc.returncode)
