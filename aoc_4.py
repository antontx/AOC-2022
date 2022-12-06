def overlap(a: list[int], b: list[int]):
    if a[0] <= b[0]:
        num: int = b[0] - a[1]
        if num <= 0:
            return True
        return False
    else:
        num: int = a[0] - b[1]
        if num <= 0:
            return True
        return False

def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    score: int = 0
    print(src)
    pairs = []
    for element in src:
        a,b = element.split(",")

        a = a.split("-")
        a = list(map(int,a))

        b = b.split("-")
        b = list(map(int, b))

        pairs.append((a,b))
    print(pairs)

    for pair in pairs:
        if overlap(pair[0],pair[1]):
            score += 1

    print(score)



def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

if __name__ == "__main__":
    main()