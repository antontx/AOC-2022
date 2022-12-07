import pprint
import json

globalSize = []


def f_size(dic: dict) -> int:
    global globalSize
    s = 0
    for k, v in dic.items():
        if isinstance(v, str):
            s += int(v)
        else:
            s += f_size(v)
            globalSize.append(f_size(v))

    return s


def getCd(cd: dict, p: list):

    if len(p) > 1:
        for key in p[:-1]:
            cd = cd[key]

    return cd


def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    lines = []
    main = {}
    path = []

    for word in src:
        lines.append(word.split())

    for words in lines:
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    path.pop();
                else:
                    path.append(words[2])
        else:

            cd = getCd(main, path)

            if path[-1] in cd:
                if words[0] == "dir":
                    cd[path[-1]][words[1]] = {}
                else:
                    cd[path[-1]][words[1]] = words[0]
            else:
                cd[path[-1]] = {}
                if words[0] == "dir":
                    cd[path[-1]][words[1]] = {}
                else:
                    cd[path[-1]][words[1]] = words[0]


    f_size(main)

    # 30000000 - (70000000 - 45349983) = 5349983
    globalSize.append(5349983)
    globalSize.sort()
    print(globalSize[globalSize.index(5349983)+1])

def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()