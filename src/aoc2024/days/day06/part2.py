import sys


def check(g: list[list[str]]) -> bool:
    w = len(g[0])
    h = len(g)

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_idx = 0

    x, y = None, None
    for y2 in range(h):
        for x2 in range(w):
            if g[y2][x2] == "^":
                x, y = x2, y2

    visited = set()
    while True:
        visited.add((x, y, dir_idx))

        dx, dy = dirs[dir_idx]
        xnext, ynext = x + dx, y + dy

        if xnext < 0 or xnext >= w or ynext < 0 or ynext >= h:
            break

        if g[ynext][xnext] == "#":
            dir_idx = (dir_idx + 1) % len(dirs)
        else:
            x, y = xnext, ynext

        if (x, y, dir_idx) in visited:
            return True

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    g = [list(line) for line in data.splitlines()]
    w = len(g[0])
    h = len(g)

    t = 0
    for y in range(h):
        for x in range(w):
            if g[y][x] in "#^":
                continue

            g[y][x] = "#"
            if check(g):
                t += 1
            g[y][x] = "."

    print(t)


if __name__ == "__main__":
    main()
