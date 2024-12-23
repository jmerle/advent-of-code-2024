import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.read().strip()

    cons = defaultdict(set)
    for line in data.splitlines():
        src, trg = line.split("-")
        cons[src].add(trg)
        cons[trg].add(src)

    comps = list(cons)

    out = 0
    for i, comp1 in enumerate(comps):
        for j, comp2 in enumerate(comps[i + 1 :]):
            for comp3 in comps[i + j + 1 :]:
                if comp1[0] != "t" and comp2[0] != "t" and comp3[0] != "t":
                    continue

                if comp2 in cons[comp1] and comp3 in cons[comp2] and comp3 in cons[comp1]:
                    out += 1

    print(out)


if __name__ == "__main__":
    main()
