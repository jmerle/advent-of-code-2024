import functools
import sys


@functools.cache
def count_options(design: str, patterns: tuple[str]) -> int:
    if len(design) == 0:
        return 1

    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += count_options(design[len(pattern) :], patterns)

    return count


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")
    patterns = tuple(sections[0].split(", "))
    designs = sections[1].splitlines()

    print(sum(count_options(design, patterns) for design in designs))


if __name__ == "__main__":
    main()
