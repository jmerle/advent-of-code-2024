import sys
from collections import defaultdict


def fill(g: list[list[str]], w: int, h: int, colors: list[list[int]], x: int, y: int, target: str, color: int) -> None:
    if x < 0 or x >= w or y < 0 or y >= h:
        return

    if colors[y][x] != -1 or g[y][x] != target:
        return

    colors[y][x] = color

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        fill(g, w, h, colors, x + dx, y + dy, target, color)


def score(w: int, h: int, colors: list[list[int]], color: int) -> int:
    area = 0
    perimeter = 0
    check = defaultdict(set)

    for y in range(h):
        for x in range(w):
            if colors[y][x] != color:
                continue

            area += 1

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < w and 0 <= y2 < h and colors[y2][x2] == color:
                    continue

                check[(x, y)].add((dx, dy))

                if dy == 0:
                    x3, y3 = x, y - 1
                else:
                    x3, y3 = x - 1, y

                if 0 <= x3 < w and 0 <= y3 < h and (dx, dy) in check[(x3, y3)]:
                    continue

                perimeter += 1

    return area * perimeter


def main() -> None:
    data = sys.stdin.read().strip()

    g = [list(line) for line in data.splitlines()]
    w = len(g[0])
    h = len(g)

    colors = [[-1] * w for _ in range(h)]
    color = 0

    out = 0

    for y in range(h):
        for x in range(w):
            fill(g, w, h, colors, x, y, g[y][x], color)

            if colors[y][x] != color:
                continue

            out += score(w, h, colors, color)
            color += 1

    print(out)


if __name__ == "__main__":
    main()
