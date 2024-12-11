import sys


def main() -> None:
    data = sys.stdin.read().strip()

    stones = list(map(int, data.split()))

    for _ in range(25):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue

            num = str(stone)
            if len(num) % 2 == 0:
                new_stones.append(int(num[: len(num) // 2]))
                new_stones.append(int(num[len(num) // 2 :]))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    print(len(stones))


if __name__ == "__main__":
    main()
