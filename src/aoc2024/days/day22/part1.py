import sys


def get_next_secret(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def main() -> None:
    data = sys.stdin.read().strip()

    out = 0
    for initial_secret in map(int, data.splitlines()):
        secret = initial_secret
        for _ in range(2000):
            secret = get_next_secret(secret)

        print(f"{initial_secret}: {secret}")
        out += secret

    print(out)


if __name__ == "__main__":
    main()
