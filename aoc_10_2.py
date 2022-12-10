from pprint import pprint

# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

def toTuples(x: int, row: int)-> list:
    xTuples = []
    xTuples.append((row, x % 40))
    x += 1
    xTuples.append((row, x % 40))
    x += 1
    xTuples.append((row, x % 40))

    return xTuples




def printCRT(crt):
    for row in crt:
        print(" ".join(row))


def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    register = [1]
    crt = [[' ' for _ in range(40)] for _ in range(6)]
    printCRT(crt)

    for instruction in src:
        x = register[-1]

        if len(instruction) == 1:
            register.append(x)
        else:
            register.append(x)
            register.append(x+int(instruction[1]))



    for cycle in range(1,240):
        x = register[cycle-1]
        row = cycle // 40

        cTuple = (row, cycle % 40)
        xTuples = toTuples(x,row)

        print(f"{cycle=} {x=}")

        print(cTuple)
        print(xTuples)

        # crt[cTuple[0]][cTuple[1] - 1] = "#"
        if cTuple in xTuples:
            print(f"pixel {cTuple} drawn")
            crt[cTuple[0]][cTuple[1] - 1] = "#"

    printCRT(crt)








def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip().split(" ") for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()