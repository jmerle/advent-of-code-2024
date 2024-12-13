import re
import sys

from z3 import Int, Solver, sat


def main() -> None:
    data = sys.stdin.read().strip()

    out = 0
    for machine in data.split("\n\n"):
        lines = machine.splitlines()

        dx_a, dy_a = map(int, re.findall(r"(\d+)", lines[0]))
        dx_b, dy_b = map(int, re.findall(r"(\d+)", lines[1]))
        prize_x, prize_y = map(int, re.findall(r"(\d+)", lines[2]))

        prize_x += 10000000000000
        prize_y += 10000000000000

        solver = Solver()

        a = Int("a")
        b = Int("b")

        solver.add(a * dx_a + b * dx_b == prize_x)
        solver.add(a * dy_a + b * dy_b == prize_y)

        if solver.check() == sat:
            out += solver.model().eval(a * 3 + b).as_long()

    print(out)


if __name__ == "__main__":
    main()
