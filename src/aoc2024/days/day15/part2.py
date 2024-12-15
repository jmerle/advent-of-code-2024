import sys
from copy import deepcopy


def find_robot(grid, w, h):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "@":
                return x, y


def do_move(grid, w, h, dx, dy):
    rx, ry = find_robot(grid, w, h)

    rx2, ry2 = rx + dx, ry + dy
    if rx2 < 0 or rx2 >= w or ry2 < 0 or ry2 >= h:
        return None

    if grid[ry2][rx2] == "#":
        return None

    cells_to_move = set()

    arr = [(rx + dx, ry + dy)]
    while len(arr) > 0:
        x, y = arr.pop()

        if x < 0 or x >= w or y < 0 or y >= h:
            continue

        if grid[y][x] in ".#":
            continue

        if (x, y) in cells_to_move:
            continue

        if grid[y][x] == "[":
            cells_to_move.add((x, y))
            cells_to_move.add((x + 1, y))
            arr.append((x + dx, y + dy))
            arr.append((x + dx + 1, y + dy))

        if grid[y][x] == "]":
            cells_to_move.add((x, y))
            cells_to_move.add((x - 1, y))
            arr.append((x + dx, y + dy))
            arr.append((x + dx - 1, y + dy))

    for x, y in cells_to_move:
        x2, y2 = x + dx, y + dy
        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h or grid[y2][x2] not in "[].":
            return None

    new_grid = deepcopy(grid)
    modified = set()

    for x, y in cells_to_move:
        new_grid[y + dy][x + dx] = grid[y][x]
        modified.add((x + dx, y + dy))

    for x, y in cells_to_move:
        if (x, y) not in modified:
            new_grid[y][x] = "."

    new_grid[ry2][rx2] = "@"
    new_grid[ry][rx] = "."

    return new_grid


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")

    grid = []
    for line in sections[0].splitlines():
        row = ""
        for ch in line:
            if ch == "#":
                row += "##"
            elif ch == "O":
                row += "[]"
            elif ch == ".":
                row += ".."
            elif ch == "@":
                row += "@."

        grid.append(list(row))

    w = len(grid[0])
    h = len(grid)

    for move in sections[1]:
        if move == "^":
            dx, dy = 0, -1
        elif move == "v":
            dx, dy = 0, 1
        elif move == "<":
            dx, dy = -1, 0
        elif move == ">":
            dx, dy = 1, 0
        else:
            continue

        new_grid = do_move(grid, w, h, dx, dy)
        if new_grid is not None:
            grid = new_grid

    out = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "[":
                out += x + 100 * y

    print(out)


if __name__ == "__main__":
    main()
