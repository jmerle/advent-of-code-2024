import heapq
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    g = [list(line) for line in data.splitlines()]
    w = len(g[0])
    h = len(g)

    for y in range(h):
        for x in range(w):
            if g[y][x] == "S":
                sx, sy = x, y
            elif g[y][x] == "E":
                tx, ty = x, y

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heap = [(0, sx, sy, 0)]

    best_score = None
    seen = set()

    while len(heap) > 0:
        score, x, y, dir_idx = heapq.heappop(heap)

        if best_score is not None and score >= best_score:
            continue

        if x == tx and y == ty:
            best_score = score
            continue

        if (x, y, dir_idx) in seen:
            continue

        seen.add((x, y, dir_idx))

        heapq.heappush(heap, (score + 1000, x, y, (dir_idx - 1) % 4))
        heapq.heappush(heap, (score + 1000, x, y, (dir_idx + 1) % 4))

        dx, dy = dirs[dir_idx]
        x2, y2 = x + dx, y + dy

        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
            continue

        if g[y2][x2] == "#":
            continue

        heapq.heappush(heap, (score + 1, x2, y2, dir_idx))

    print(best_score)


if __name__ == "__main__":
    main()
