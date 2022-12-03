def main():
    src = get_input_from_file("files/test.txt")
    bags = []
    chars = []
    for pair in src:
        bags.append([pair[:len(pair)//2],pair[len(pair)//2:]])

    #part 1
    temp = set()
    for pair in bags:
        temp.clear()
        for char in pair[0]:
            if char in pair[1]:
                temp.add(char)
        chars.extend(temp)

    sum = 0
    for char in chars:
        sum += priority(char)

    #part 2
    chars.clear()
    groups = [list(bag) for bag in zip(*[src[i::3] for i in range(3)])]
    for bag in groups:
        temp.clear()
        for char in bag[0]:
            if char in bag[1] and char in bag[2]:
                temp.add(char)
        chars.extend(temp)

    print(chars)
    sum = 0
    for char in chars:
        sum += priority(char)



    print(sum)


def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

def priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


if __name__ == "__main__":
    main()