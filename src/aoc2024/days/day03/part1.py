import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    m = re.findall(r"mul\(\d+,\d+\)", data)
    t = 0
    for v in m:
        d = list(map(int, re.findall(r"\d+", v)))
        t += d[0] * d[1]

    print(t)


if __name__ == "__main__":
    main()
