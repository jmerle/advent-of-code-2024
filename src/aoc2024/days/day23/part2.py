import sys

import networkx as nx


def main() -> None:
    data = sys.stdin.read().strip()

    g = nx.Graph()
    for line in data.splitlines():
        src, trg = line.split("-")
        g.add_edge(src, trg)

    comps = max(nx.find_cliques(g), key=len)
    print(",".join(sorted(comps)))


if __name__ == "__main__":
    main()
