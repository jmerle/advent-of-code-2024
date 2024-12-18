import heapq
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    coords = [tuple(map(int, line.split(","))) for line in data.splitlines()]

    if len(coords) == 25:
        tx, ty = 6, 6
        blocked = set(coords[:12])
    else:
        tx, ty = 70, 70
        blocked = set(coords[:1024])

    heap = []
    heapq.heappush(heap, (0, 0, 0))

    seen = set()

    while len(heap) > 0:
        distance, x, y = heapq.heappop(heap)

        if x == tx and y == ty:
            print(distance)
            break

        if (x, y, distance) in seen:
            continue

        seen.add((x, y, distance))

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2, y2 = x + dx, y + dy
            if x2 < 0 or x2 > tx or y2 < 0 or y2 > ty or (x2, y2) in blocked:
                continue

            heapq.heappush(heap, (distance + 1, x2, y2))


if __name__ == "__main__":
    main()
