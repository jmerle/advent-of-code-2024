import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.read().strip()

    g = [list(line) for line in data.splitlines()]
    w = len(g[0])
    h = len(g)

    ants = defaultdict(list)
    for y in range(h):
        for x in range(w):
            if g[y][x] != ".":
                ants[g[y][x]].append((x, y))

    antis = set()
    for positions in ants.values():
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i + 1 :]:
                dx = x2 - x1
                dy = y2 - y1
                antis.add((x1 - dx, y1 - dy))
                antis.add((x2 + dx, y2 + dy))

    print(len([1 for x, y in antis if 0 <= x < w and 0 <= y < h]))


if __name__ == "__main__":
    main()
