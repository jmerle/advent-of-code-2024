import itertools
import sys

import networkx as nx


def create_graph(grid: list[str]):
    g = nx.Graph()
    mapping = {}

    w = len(grid[0])
    h = len(grid)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == " ":
                continue

            key = (grid[y][x], x, y)
            mapping[grid[y][x]] = key

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h or grid[y2][x2] == " ":
                    continue

                key2 = (grid[y2][x2], x2, y2)
                g.add_edge(key, key2)

    return g, mapping, grid


g_numbers = create_graph(
    [
        "789",
        "456",
        "123",
        " 0A",
    ]
)

g_directions = create_graph(
    [
        " ^A",
        "<v>",
    ]
)


def is_possible_path(g, path: str) -> bool:
    grid = g[2]
    w = len(grid[0])
    h = len(grid)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "A":
                cx, cy = x, y
                break

    for ch in path:
        if ch == ">":
            dx, dy = 1, 0
        elif ch == "<":
            dx, dy = -1, 0
        elif ch == "v":
            dx, dy = 0, 1
        else:
            dx, dy = 0, -1

        cx, cy = cx + dx, cy + dy

        if cx < 0 or cx >= w or cy < 0 or cy >= h or grid[cy][cx] == " ":
            return False

    return True


def get_paths(g, sequence: str, optimize: bool) -> list[str]:
    out = ""

    for from_, to in zip(sequence, sequence[1:]):
        path = nx.shortest_path(g[0], g[1][from_], g[1][to])
        for (_, x1, y1), (_, x2, y2) in zip(path, path[1:]):
            if x2 < x1:
                out += "<"
            elif x2 > x1:
                out += ">"
            elif y2 < y1:
                out += "^"
            else:
                out += "v"
        out += "A"

    if not optimize:
        return [out]

    separators = []
    buffer = ""

    for i, ch in enumerate(out):
        if ch != "A":
            buffer += ch

        if ch == "A" or i == len(out) - 1:
            separators.append(list(itertools.permutations(buffer)))
            buffer = ""

    paths = []
    for option in itertools.product(*separators):
        path = ""
        moves = ""

        for sep in option:
            path += "".join(sep) + "A"
            moves += "".join(sep)

        if is_possible_path(g, moves):
            paths.append(path)

    return paths


def get_sequence_length(code: str) -> int:
    min_length = 1e9

    for path1 in get_paths(g_numbers, "A" + code, optimize=True):
        for path2 in get_paths(g_directions, "A" + path1, optimize=True):
            for path3 in get_paths(g_directions, "A" + path2, optimize=False):
                min_length = min(min_length, len(path3))

    print(code, min_length)
    return min_length


def main() -> None:
    data = sys.stdin.read().strip()

    out = 0
    for code in data.splitlines():
        out += get_sequence_length(code) * int("".join(ch for ch in code if ch.isdigit()))

    print(out)


if __name__ == "__main__":
    main()
