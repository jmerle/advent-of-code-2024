import sys


def main() -> None:
    data = sys.stdin.read().strip()

    disk = []
    file_id = 0

    for i, size in enumerate(map(int, data)):
        if i % 2 == 0:
            disk.append([1, file_id, size])
            file_id += 1
        else:
            disk.append([2, size])

    cur = len(disk) - 1
    while cur >= 0:
        file_obj = disk[cur]
        if file_obj[0] != 1:
            cur -= 1
            continue

        _, file_id, size = file_obj

        for i, empty_obj in enumerate(disk):
            if i >= cur:
                cur -= 1
                break

            if empty_obj[0] != 2 or empty_obj[1] < size:
                continue

            disk.insert(i, [1, file_id, size])

            empty_obj[1] -= size

            file_obj[0] = 2
            file_obj[1] = size
            break
        else:
            cur -= 1

    arr = []
    for obj in disk:
        if obj[0] == 1:
            arr.extend([obj[1]] * obj[2])
        else:
            arr.extend(["."] * obj[1])

    out = 0
    for i, v in enumerate(arr):
        if v != ".":
            out += i * v

    print(out)


if __name__ == "__main__":
    main()
