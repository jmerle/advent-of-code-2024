import itertools
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.splitlines():
        ans, nums = line.split(": ")
        ans = int(ans)
        nums = list(map(int, nums.split()))

        opts = [["+", "*"] for _ in range(len(nums) - 1)]

        for opt in itertools.product(*opts):
            out = nums[0]

            for i, v in enumerate(nums[1:]):
                op = opt[i]
                if op == "+":
                    out += v
                else:
                    out *= v

            if out == ans:
                t += ans
                break

    print(t)


if __name__ == "__main__":
    main()
