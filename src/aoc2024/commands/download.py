import click

from aoc2024.commands.common import PROJECT_ROOT, get_day_directory, get_requests_session


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
def download(day: int) -> None:
    """Downloads the input data for the given day."""
    input_file = get_day_directory(day) / "full.txt"

    if not input_file.is_file():
        raise ValueError(f"{input_file} does not exist")

    if input_file.stat().st_size != 0:
        raise ValueError(f"{input_file} is not empty")

    input_response = get_requests_session().get(f"https://adventofcode.com/2024/day/{day}/input")
    input_response.raise_for_status()

    input_file.write_text(input_response.text, encoding="utf-8")
    print(f"Successfully wrote input data to {input_file.relative_to(PROJECT_ROOT)}")
