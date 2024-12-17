import sys


def main() -> None:
    data = sys.stdin.read().strip()

    blocks = data.split("\n\n")

    regs = {}
    for line in blocks[0].splitlines():
        key = line.split(" ")[1].split(":")[0]
        value = int(line.split(" ")[-1])
        regs[key] = value

    prog = list(map(int, blocks[1].split(": ")[1].split(",")))
    ptr = 0

    out = []

    while ptr < len(prog) - 1:
        old_ptr = ptr

        opcode = prog[ptr]
        literal_operand = prog[ptr + 1]

        combo_operand = literal_operand
        if combo_operand > 3:
            combo_operand = regs[chr(ord("A") + combo_operand - 4)]

        if opcode == 0:
            regs["A"] = regs["A"] // (2**combo_operand)
        elif opcode == 1:
            regs["B"] = regs["B"] ^ literal_operand
        elif opcode == 2:
            regs["B"] = combo_operand % 8
        elif opcode == 3:
            if regs["A"] != 0:
                ptr = literal_operand
        elif opcode == 4:
            regs["B"] = regs["B"] ^ regs["C"]
        elif opcode == 5:
            out.append(combo_operand % 8)
        elif opcode == 6:
            regs["B"] = regs["A"] // (2**combo_operand)
        elif opcode == 7:
            regs["C"] = regs["A"] // (2**combo_operand)

        if ptr == old_ptr:
            ptr += 2

    print(",".join(map(str, out)))


if __name__ == "__main__":
    main()
