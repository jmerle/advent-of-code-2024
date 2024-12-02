import sys


def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.splitlines():
        nums = list(map(int, line.split()))

        is_incr = all(1 <= (nums[i + 1] - nums[i]) <= 3 for i in range(len(nums) - 1))
        is_decr = all(1 <= (nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1))
        if is_incr or is_decr:
            t += 1

    print(t)


if __name__ == "__main__":
    main()
