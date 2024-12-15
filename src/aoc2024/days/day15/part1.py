import sys


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")

    grid = [list(line) for line in sections[0].splitlines()]
    w = len(grid[0])
    h = len(grid)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "@":
                rx, ry = x, y

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

        can_move = False
        for i in range(1, 100):
            x2, y2 = rx + dx * i, ry + dy * i
            if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                break

            if grid[y2][x2] == "#":
                break

            if grid[y2][x2] == ".":
                can_move = True
                break

        if not can_move:
            continue

        boxes = 0
        for i in range(1, 100):
            x2, y2 = rx + dx * i, ry + dy * i
            if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                break

            if grid[y2][x2] == "#":
                break

            if grid[y2][x2] == "O":
                boxes += 1

            if i == 1:
                grid[y2][x2] = "@"
            elif boxes > 0:
                grid[y2][x2] = "O"
                boxes -= 1
            else:
                break

        grid[ry][rx] = "."
        rx, ry = rx + dx, ry + dy

    out = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O":
                out += x + 100 * y

    print(out)


if __name__ == "__main__":
    main()
