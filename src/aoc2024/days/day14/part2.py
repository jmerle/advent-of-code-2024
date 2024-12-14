import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    w = 101
    h = 103

    if data[2] == "0":
        w = 11
        h = 7

    robots = []
    for line in data.splitlines():
        px, py, vx, vy = map(int, re.findall(r"([0-9-]+)", line))
        robots.append((px, py, vx, vy))

    for i in range(int(1e6)):
        locs = set()
        for px, py, vx, vy in robots:
            locs.add(((px + vx * i) % w, (py + vy * i) % h))

        grid = []
        tree = False

        for y in range(h):
            line = ""
            for x in range(w):
                line += "#" if (x, y) in locs else "."

            tree = tree or ("#" * 9) in line
            grid.append(line)

        if tree:
            print("\n".join(grid))
            print(i)
            break


if __name__ == "__main__":
    main()
