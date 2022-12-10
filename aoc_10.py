from pprint import pprint

# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    register = [1]

    for instruction in src:
        x = register[-1]

        if len(instruction) == 1: #noop
            register.append(x)
        else:
            register.append(x)
            register.append(x+int(instruction[1]))


    cycles = [20,60,100,140,180,220]
    count = 0

    for c in cycles:
        count += (register[c-1] * c)

    print(count)






def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip().split(" ") for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()