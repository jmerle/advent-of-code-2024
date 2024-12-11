import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.read().strip()

    stones = list(map(int, data.split()))
    counts = Counter(stones)

    for _ in range(75):
        new_counts = Counter()

        for stone, cnt in counts.items():
            if stone == 0:
                new_counts[1] += cnt
                continue

            num = str(stone)
            if len(num) % 2 == 0:
                new_counts[int(num[: len(num) // 2])] += cnt
                new_counts[int(num[len(num) // 2 :])] += cnt
            else:
                new_counts[stone * 2024] += cnt

        counts = new_counts

    print(sum(counts.values()))


if __name__ == "__main__":
    main()
