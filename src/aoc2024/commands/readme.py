import re

import click

from aoc2024.commands.common import PROJECT_ROOT, get_day_directory, get_requests_session

OVERALL_LEADERBOARD_RANKS = [
    39,  # Day 1
    None,  # Day 2
    None,  # Day 3
    None,  # Day 4
    None,  # Day 5
    None,  # Day 6
    None,  # Day 7
    None,  # Day 8
    None,  # Day 9
    None,  # Day 10
    None,  # Day 11
    None,  # Day 12
    None,  # Day 13
    None,  # Day 14
    None,  # Day 15
    None,  # Day 16
    None,  # Day 17
    None,  # Day 18
    None,  # Day 19
    None,  # Day 20
    None,  # Day 21
    None,  # Day 22
    None,  # Day 23
    None,  # Day 24
    None,  # Day 25
]


@click.command()
def readme() -> None:
    """Update the results in the project's readme file."""
    leaderboard_response = get_requests_session().get("https://adventofcode.com/2024/leaderboard/self")
    leaderboard_response.raise_for_status()

    rows = ""
    overall_score = 0

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
        part1_score = int(parts[3])
        part2_time = parts[4]
        part2_rank = int(parts[5])
        part2_score = int(parts[6])

        overall_rank = OVERALL_LEADERBOARD_RANKS[day - 1] or ">100"
        overall_score += part1_score + part2_score

        day_directory = get_day_directory(day)

        rows += f"""
        <tr>
            <td><a href="https://adventofcode.com/2024/day/{day}" target="_blank">Day {day}</a></td>
            <td>{part1_time}</td>
            <td>{part1_rank}</td>
            <td>{part1_score}</td>
            <td>{part2_time}</td>
            <td>{part2_rank}</td>
            <td>{part2_score}</td>
            <td>{overall_rank}</td>
            <td>{overall_score}</td>
            <td><a href="https://github.com/jmerle/advent-of-code-2024/tree/master/{day_directory.relative_to(PROJECT_ROOT)}">Link</a></td>
        </tr>"""

    table = f"""
<!-- results-start -->
<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="3">Part 1</th>
            <th colspan="3">Part 2</th>
            <th colspan="2">Overall leaderboard</th>
            <th></th>
        </tr>
        <tr>
            <th>Day</th>
            <th>Time</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Time</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Code</th>
        </tr>
    </thead>
    <tbody>
        {rows.lstrip()}
    </tbody>
</table>
<!-- results-end -->
    """.strip()

    readme_file = PROJECT_ROOT / "README.md"

    readme_content = readme_file.read_text(encoding="utf-8")
    readme_content = re.sub(r"<!-- results-start -->(.*)<!-- results-end -->", table, readme_content, flags=re.DOTALL)
    readme_file.write_text(readme_content, encoding="utf-8")

    print("Successfully updated the results table in the readme")
