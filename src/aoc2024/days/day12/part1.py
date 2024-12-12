import sys


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

    for y in range(h):
        for x in range(w):
            if colors[y][x] != color:
                continue

            area += 1

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h or colors[y2][x2] != color:
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
