from itertools import groupby;
import re;

def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    src = [list(group) for key, group in groupby(src, lambda x: x == "") if not key]
    moves = src[1]
    ids: str = src[0].pop()
    src = list(reversed(src))
    src = src[1]
    src = list(reversed(src))


    crane = {}
    for layer in src:
        for i in range(len(layer)):
            if layer[i].isalpha():
                if crane.get(int(ids[int(i)])) is None:
                    crane[int(ids[int(i)])] = [layer[i]]
                else:
                    crane[int(ids[int(i)])].append(layer[i])


    print(crane)

    n_moves = [];
    for move in moves:
        nums = []
        move = move.split()
        for letter in move:
            if letter.isdigit():
                nums.append(int(letter))
        n_moves.append(nums)

    print(n_moves)

    #p1
    # for move in n_moves:
    #     amount = move[0]
    #     from_ = move[1]
    #     to_ = move[2]
    #     for i in range(amount):
    #         print(f"{amount=} {from_=} {to_=}")
    #         crane[move[2]].append(crane[move[1]].pop())
    #     print(crane)

    for move in n_moves:
        carry = []
        amount = move[0]
        from_ = move[1]
        to_ = move[2]
        for i in range(amount):
            carry.append(crane[from_].pop())
        carry = list(reversed(carry))
        crane[to_].extend(carry)

        print(crane)

    out = ""

    for stack in crane:
        out += crane[stack].pop()

    print(out)

    print(crane)

def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()