import functools
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


def is_possible_path(g, source: str, path: str) -> bool:
    grid = g[2]
    w = len(grid[0])
    h = len(grid)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == source:
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


def get_paths(g, from_: str, to: str) -> list[str]:
    _, x1, y1 = g[1][from_]
    _, x2, y2 = g[1][to]
    dx, dy = x2 - x1, y2 - y1

    moves = ""

    if dx < 0:
        moves += "<" * abs(dx)
    elif dx > 0:
        moves += ">" * dx

    if dy < 0:
        moves += "^" * abs(dy)
    elif dy > 0:
        moves += "v" * dy

    paths = []
    for option in itertools.permutations(moves):
        option = "".join(option)

        if is_possible_path(g, from_, option):
            paths.append(option + "A")

    return paths


@functools.cache
def get_sequence_length(code: str, depth: int = 0) -> int:
    g = g_numbers if depth == 0 else g_directions
    prev = "A"

    out = 0
    for ch in code:
        paths = get_paths(g, prev, ch)

        if depth == 25:
            out += len(paths[0])
        else:
            out += min(get_sequence_length(path, depth + 1) for path in paths)

        prev = ch

    if depth == 0:
        print(code, out)

    return out


def main() -> None:
    data = sys.stdin.read().strip()

    out = 0
    for code in data.splitlines():
        out += get_sequence_length(code) * int("".join(ch for ch in code if ch.isdigit()))

    print(out)


if __name__ == "__main__":
    main()
