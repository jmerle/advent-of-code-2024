import sys


def main() -> None:
    data = sys.stdin.read().strip()

    g = data.splitlines()
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
        visited.add((x, y))

        dx, dy = dirs[dir_idx]
        xnext, ynext = x + dx, y + dy

        if xnext < 0 or xnext >= w or ynext < 0 or ynext >= h:
            break

        if g[ynext][xnext] == "#":
            dir_idx = (dir_idx + 1) % len(dirs)
        else:
            x, y = xnext, ynext

    print(len(visited))


if __name__ == "__main__":
    main()
