import sys


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")

    inputs = {}
    for line in sections[0].splitlines():
        key, value = line.split(": ")
        inputs[key] = int(value)

    ops = []
    for line in sections[1].splitlines():
        parts = line.split(" ")
        ops.append((parts[0], parts[1], parts[2], parts[4]))

    while len(ops) > 0:
        new_ops = []

        for inp1, typ, inp2, out in ops:
            if inp1 not in inputs or inp2 not in inputs:
                new_ops.append((inp1, typ, inp2, out))
                continue

            if typ == "AND":
                inputs[out] = inputs[inp1] & inputs[inp2]
            elif typ == "OR":
                inputs[out] = inputs[inp1] | inputs[inp2]
            else:
                inputs[out] = inputs[inp1] ^ inputs[inp2]

        ops = new_ops

    bits = ""
    idx = 0
    while f"z{idx:02}" in inputs:
        bits += str(inputs[f"z{idx:02}"])
        idx += 1

    print(int(bits[::-1], 2))


if __name__ == "__main__":
    main()
