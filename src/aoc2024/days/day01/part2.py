import sys


def main() -> None:
    data = sys.stdin.read().strip()

    a = []
    b = []

    for line in data.splitlines():
        nums = line.split()
        a.append(int(nums[0]))
        b.append(int(nums[1]))

    a = sorted(a)
    b = sorted(b)

    t = 0
    for i in a:
        t += i * b.count(i)

    print(t)


if __name__ == "__main__":
    main()
