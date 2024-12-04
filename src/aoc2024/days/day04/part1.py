import sys


def main() -> None:
    data = sys.stdin.read().strip()

    g = list(data.splitlines())
    w = len(g[0])
    h = len(g)

    t = 0
    for y in range(h):
        for x in range(w):
            if g[y][x] != "X":
                continue

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                s = ""

                for i in range(4):
                    x2, y2 = x + dx * i, y + dy * i
                    if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                        break

                    s += g[y2][x2]

                if s == "XMAS":
                    t += 1

    print(t)


if __name__ == "__main__":
    main()
