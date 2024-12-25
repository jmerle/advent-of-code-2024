import re

import click

from aoc2024.commands.common import PROJECT_ROOT, get_day_directory, get_requests_session

LATE_DAYS = {2, 13, 17, 25}
SERVER_ISSUE_DAYS = {2}


@click.command()
def readme() -> None:
    """Update the results in the project's readme file."""
    leaderboard_response = get_requests_session().get("https://adventofcode.com/2024/leaderboard/self")
    leaderboard_response.raise_for_status()

    rows = ""

    matches = re.search(
        r"<span class=\"leaderboard-daydesc-both\">    Time  Rank  Score</span>(.*)</pre>",
        leaderboard_response.text,
        flags=re.DOTALL,
    )
    for line in reversed(matches.group(1).splitlines()):
        line = line.strip()
        if len(line) == 0:
            continue

        parts = [part for part in line.split(" ") if len(part) > 0]

        day = int(parts[0])
        part1_time = parts[1]
        part1_rank = int(parts[2])
        part2_time = parts[4]
        part2_rank = int(parts[5])

        day_directory = get_day_directory(day)

        sups = []
        if day in LATE_DAYS:
            sups.append(1)
        if day in SERVER_ISSUE_DAYS:
            sups.append(2)

        if len(sups) > 0:
            sups = "<sup>" + ",".join(map(str, sups)) + "</sup>"
        else:
            sups = ""

        rows += f"""
        <tr>
            <td><a href="https://adventofcode.com/2024/day/{day}">Day {day}</a>{sups}</td>
            <td>{part1_time}</td>
            <td>{part1_rank}</td>
            <td>{part2_time}</td>
            <td>{part2_rank}</td>
            <td><a href="https://github.com/jmerle/advent-of-code-2024/tree/master/{day_directory.relative_to(PROJECT_ROOT)}">Link</a></td>
        </tr>"""

    table = f"""
<!-- results-start -->
<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="2">Part 1</th>
            <th colspan="2">Part 2</th>
            <th></th>
        </tr>
        <tr>
            <th>Day</th>
            <th>Time</th>
            <th>Rank</th>
            <th>Time</th>
            <th>Rank</th>
            <th>Code</th>
        </tr>
    </thead>
    <tbody>
        {rows.lstrip()}
    </tbody>
</table>

_<sup>1</sup> I started late on this day's parts (i.e. not at the time of part 1's release)._  
_<sup>2</sup> Advent of Code had server issues at the time of this day's release._
<!-- results-end -->
    """.strip()

    readme_file = PROJECT_ROOT / "README.md"

    readme_content = readme_file.read_text(encoding="utf-8")
    readme_content = re.sub(r"<!-- results-start -->(.*)<!-- results-end -->", table, readme_content, flags=re.DOTALL)
    readme_file.write_text(readme_content, encoding="utf-8")

    print("Successfully updated the results table in the readme")
