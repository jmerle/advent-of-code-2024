import sys
import traceback

import click

from aoc2024.commands.download import download
from aoc2024.commands.new import new
from aoc2024.commands.readme import readme
from aoc2024.commands.run import run
from aoc2024.commands.watch import watch


@click.group(context_settings={"help_option_names": ["--help", "-h"], "max_content_width": 120})
def cli() -> None:
    """A CLI containing several utilities for Advent of Code 2024."""
    pass


cli.add_command(download)
cli.add_command(new)
cli.add_command(readme)
cli.add_command(run)
cli.add_command(watch)


def main() -> None:
    try:
        cli()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
