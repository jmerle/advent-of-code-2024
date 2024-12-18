import heapq
import sys


def is_possible(tx: int, ty: int, blocked: set[tuple[int, int]]) -> bool:
    heap = []
    heapq.heappush(heap, (0, 0))

    seen = set()

    while len(heap) > 0:
        x, y = heapq.heappop(heap)

        if x == tx and y == ty:
            return True

        if (x, y) in seen:
            continue

        seen.add((x, y))

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2, y2 = x + dx, y + dy
            if x2 < 0 or x2 > tx or y2 < 0 or y2 > ty or (x2, y2) in blocked:
                continue

            heapq.heappush(heap, (x2, y2))

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    coords = [tuple(map(int, line.split(","))) for line in data.splitlines()]

    if len(coords) == 25:
        tx, ty = 6, 6
        start = 12
    else:
        tx, ty = 70, 70
        start = 1024

    for i in range(start, len(coords)):
        if not is_possible(tx, ty, set(coords[:i])):
            print(",".join(map(str, coords[i - 1])))
            break


if __name__ == "__main__":
    main()
