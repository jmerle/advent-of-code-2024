import sys


def is_possible(design: str, patterns: list[str]) -> bool:
    if len(design) == 0:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if is_possible(design[len(pattern) :], patterns):
                return True

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")
    patterns = sections[0].split(", ")
    designs = sections[1].splitlines()

    out = 0
    for design in designs:
        if is_possible(design, patterns):
            out += 1

    print(out)


if __name__ == "__main__":
    main()
