import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    out = 0
    for machine in data.split("\n\n"):
        lines = machine.splitlines()

        dx_a, dy_a = map(int, re.findall(r"(\d+)", lines[0]))
        dx_b, dy_b = map(int, re.findall(r"(\d+)", lines[1]))
        prize_x, prize_y = map(int, re.findall(r"(\d+)", lines[2]))

        required = None
        for a in range(100):
            for b in range(100):
                if dx_a * a + dx_b * b == prize_x and dy_a * a + dy_b * b == prize_y:
                    tokens = a * 3 + b
                    required = tokens if required is None else min(required, tokens)

        if required is not None:
            out += required

    print(out)


if __name__ == "__main__":
    main()
