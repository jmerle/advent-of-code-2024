import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.read().strip()

    g = [[(int(v) if v != "." else 99) for v in line] for line in data.splitlines()]
    w = len(g[0])
    h = len(g)

    arr = []
    for y in range(h):
        for x in range(w):
            if g[y][x] == 9:
                arr.append((x, y, x, y))

    reachable = defaultdict(set)
    while len(arr) > 0:
        sx, sy, x, y = arr.pop()
        cell = g[y][x]

        if cell == 0:
            reachable[(x, y)].add((sx, sy))
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x2, y2 = x + dx, y + dy
            if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                continue

            cell2 = g[y2][x2]
            if cell2 == cell - 1:
                arr.append((sx, sy, x2, y2))

    print(sum(map(len, reachable.values())))


if __name__ == "__main__":
    main()
