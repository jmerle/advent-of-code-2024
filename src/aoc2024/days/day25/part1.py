import sys


def main() -> None:
    data = sys.stdin.read().strip()

    locks = []
    keys = []

    for block in data.split("\n\n"):
        g = block.splitlines()
        w = len(g[0])
        h = len(g)

        heights = []
        for x in range(w):
            col = "".join(g[y][x] for y in range(h))
            heights.append(col.count("#") - 1)

        if "#" in g[0]:
            locks.append(heights)
        else:
            keys.append(heights)

    t = 0
    for lock in locks:
        for key in keys:
            if all(a + b < h - 1 for a, b in zip(lock, key)):
                t += 1

    print(t)


if __name__ == "__main__":
    main()
