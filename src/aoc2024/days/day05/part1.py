import sys


def main() -> None:
    data = sys.stdin.read().strip()

    blks = data.split("\n\n")

    order = []
    for line in blks[0].splitlines():
        order.append(list(map(int, line.split("|"))))

    t = 0
    for line in blks[1].splitlines():
        upd = list(map(int, line.split(",")))

        c = True
        for v1, v2 in order:
            if v1 not in upd or v2 not in upd:
                continue

            i1, i2 = upd.index(v1), upd.index(v2)
            if i1 > i2:
                c = False
                break

        if c:
            t += upd[len(upd) // 2]

    print(t)


if __name__ == "__main__":
    main()
