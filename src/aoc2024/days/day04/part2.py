import sys


def main() -> None:
    data = sys.stdin.read().strip()

    g = list(data.splitlines())
    w = len(g[0])
    h = len(g)

    t = 0
    for y in range(h - 2):
        for x in range(w - 2):
            w1 = g[y][x] + g[y + 1][x + 1] + g[y + 2][x + 2]
            w2 = g[y + 2][x] + g[y + 1][x + 1] + g[y][x + 2]

            c1 = w1 == "MAS" or w1[::-1] == "MAS"
            c2 = w2 == "MAS" or w2[::-1] == "MAS"
            if c1 and c2:
                t += 1

    print(t)


if __name__ == "__main__":
    main()
