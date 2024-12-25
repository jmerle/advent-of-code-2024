import sys


def get_out(
    ops: list[tuple[str, str, str, str]],
    inp1: str,
    typ: str,
    inp2: str,
) -> str | None:
    for op in ops:
        if op[1] != typ:
            continue

        if (op[0] == inp1 and op[2] == inp2) or (op[0] == inp2 and op[2] == inp1):
            return op[3]

    return None


def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")

    ops = []
    for line in sections[1].splitlines():
        parts = line.split(" ")
        ops.append((parts[0], parts[1], parts[2], parts[4]))

    size = max(int(op[3][1:]) for op in ops if op[3][0] == "z")
    swaps = []

    # Half adder for x00 and y00: https://en.wikipedia.org/wiki/Adder_(electronics)#Half_adder
    # x00 XOR y00 = z00
    # x00 AND y00 = carry

    # Full adders for x01-x44 and y01-y44: https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
    # x_n XOR y_n = temp1
    # x_n AND y_n = temp2
    # carry_in AND temp1 = temp3
    # temp1 XOR carry_in = z_n
    # temp2 OR temp3 = carry_out

    assert get_out(ops, "x00", "XOR", "y00") == "z00"
    carry_in = get_out(ops, "x00", "AND", "y00")

    for i in range(1, size):
        temp1 = get_out(ops, f"x{i:02}", "XOR", f"y{i:02}")
        temp2 = get_out(ops, f"x{i:02}", "AND", f"y{i:02}")

        temp3 = get_out(ops, carry_in, "AND", temp1)
        if temp3 is None:
            temp1, temp2 = temp2, temp1
            swaps.extend([temp1, temp2])
            temp3 = get_out(ops, carry_in, "AND", temp1)

        z_n = get_out(ops, temp1, "XOR", carry_in)

        if temp1[0] == "z":
            temp1, z_n = z_n, temp1
            swaps.extend([temp1, z_n])
        elif temp2[0] == "z":
            temp2, z_n = z_n, temp2
            swaps.extend([temp2, z_n])
        elif temp3[0] == "z":
            temp3, z_n = z_n, temp3
            swaps.extend([temp3, z_n])

        carry_out = get_out(ops, temp2, "OR", temp3)
        if carry_out[0] == "z" and carry_out != f"z{size:02}":
            carry_out, z_n = z_n, carry_out
            swaps.extend([carry_out, z_n])

        carry_in = carry_out

    print(",".join(sorted(swaps)))


if __name__ == "__main__":
    main()
