import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    m = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    t = 0
    e = True
    for v in m:
        if v == "do()":
            e = True
        elif v == "don't()":
            e = False
        elif e:
            d = list(map(int, re.findall(r"\d+", v)))
            t += d[0] * d[1]

    print(t)


if __name__ == "__main__":
    main()
