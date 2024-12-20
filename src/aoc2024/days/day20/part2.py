import sys

import networkx as nx


def create_graph(grid: list[list[str]], w: int, h: int, with_cheats: bool) -> nx.Graph:
    g = nx.Graph()

    for y in range(h):
        for x in range(w):
            if not with_cheats and grid[y][x] == "#":
                continue

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                    continue

                if not with_cheats and grid[y2][x2] == "#":
                    continue

                g.add_edge((x, y), (x2, y2))

    return g


def main() -> None:
    data = sys.stdin.read().strip()

    grid = [list(line) for line in data.splitlines()]
    w = len(grid[0])
    h = len(grid)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "S":
                sx, sy = x, y
            elif grid[y][x] == "E":
                ex, ey = x, y

    g_normal = create_graph(grid, w, h, with_cheats=False)
    g_cheats = create_graph(grid, w, h, with_cheats=True)

    start_dists = nx.single_source_shortest_path_length(g_normal, (sx, sy))
    end_dists = nx.single_source_shortest_path_length(g_normal, (ex, ey))

    normal_distance = start_dists[(ex, ey)]

    out = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                continue

            cheat_dists = nx.single_source_shortest_path_length(g_cheats, (x, y), cutoff=20)

            for (x2, y2), distance in cheat_dists.items():
                if grid[y2][x2] == "#":
                    continue

                cheat_distance = start_dists[(x, y)] + end_dists[(x2, y2)] + distance
                if normal_distance - cheat_distance >= 100:
                    out += 1

    print(out)


if __name__ == "__main__":
    main()
