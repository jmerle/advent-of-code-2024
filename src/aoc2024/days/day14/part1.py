import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    w = 101
    h = 103

    if data[2] == "0":
        w = 11
        h = 7

    wmid = (w - 1) / 2
    hmid = (h - 1) / 2

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for line in data.splitlines():
        px, py, vx, vy = map(int, re.findall(r"([0-9-]+)", line))

        px = (px + vx * 100) % w
        py = (py + vy * 100) % h

        if px < wmid and py < hmid:
            q1 += 1
        elif px > wmid and py < hmid:
            q2 += 1
        elif px > wmid and py > hmid:
            q3 += 1
        elif px < wmid and py > hmid:
            q4 += 1

    print(q1 * q2 * q3 * q4)


if __name__ == "__main__":
    main()
