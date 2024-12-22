import sys
from collections import Counter


def get_next_secret(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def main() -> None:
    data = sys.stdin.read().strip()

    counts = Counter()

    for initial_secret in map(int, data.splitlines()):
        prices = [initial_secret % 10]

        secret = initial_secret
        for _ in range(2000):
            secret = get_next_secret(secret)
            prices.append(secret % 10)

        changes = [next_price - price for price, next_price in zip(prices, prices[1:])]
        seen = set()

        for i in range(len(changes) - 3):
            change = (changes[i], changes[i + 1], changes[i + 2], changes[i + 3])
            if change in seen:
                continue

            counts[change] += prices[i + 4]
            seen.add(change)

    print(counts.most_common(1)[0][1])


if __name__ == "__main__":
    main()
