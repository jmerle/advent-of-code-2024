import heapq
import sys


def dijkstra(g, w, h, sx, sy, tx, ty):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    heap = []
    for dir_idx in range(4):
        heapq.heappush(heap, (0, sx, sy, dir_idx))

    best_score = None
    seen = set()

    scores = {}

    while len(heap) > 0:
        score, x, y, dir_idx = heapq.heappop(heap)

        if (x, y, dir_idx) not in scores:
            scores[(x, y, dir_idx)] = score

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

        dx, dy = dirs[dir_idx % 4]
        x2, y2 = x + dx, y + dy

        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
            continue

        if g[y2][x2] == "#":
            continue

        heapq.heappush(heap, (score + 1, x2, y2, dir_idx))

    return best_score, scores


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

    best_score, scores1 = dijkstra(g, w, h, sx, sy, tx, ty)
    _, scores2 = dijkstra(g, w, h, tx, ty, sx, sy)

    on_best_path = set()
    for y in range(h):
        for x in range(w):
            for dir_idx in range(4):
                if scores1.get((x, y, dir_idx), 0) + scores2.get((x, y, (dir_idx + 2) % 4), 0) == best_score:
                    on_best_path.add((x, y))

    print(len(on_best_path))


if __name__ == "__main__":
    main()
