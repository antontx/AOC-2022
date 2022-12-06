def main():
    word = get_input_from_file("files/AOC_1/test.txt")[0]
    chars = set()
    distinctChars = 14

    chars.clear()
    for i in range(distinctChars - 1, len(word)):
        chars.clear()
        for j in range(distinctChars):
            chars.add(word[i - j])
        print(len(chars), chars)
        if len(chars) == distinctChars:
            print(i + 1)
            break



def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

if __name__ == "__main__":
    main()