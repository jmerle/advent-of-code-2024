import sys


def main() -> None:
    data = sys.stdin.read().strip()

    arr = []
    file_id = 0
    empties = []

    for i, size in enumerate(map(int, data)):
        if i % 2 == 0:
            arr.extend([file_id] * size)
            file_id += 1
        else:
            empties.extend(list(range(len(arr), len(arr) + size)))
            arr.extend(["."] * size)

    empty_idx = 0

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == ".":
            continue

        to = empties[empty_idx]
        empty_idx += 1

        if to >= i:
            break

        arr[i], arr[to] = arr[to], arr[i]

    out = 0
    for i, v in enumerate(arr):
        if v != ".":
            out += i * v

    print(out)


if __name__ == "__main__":
    main()
