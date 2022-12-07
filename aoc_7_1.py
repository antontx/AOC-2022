import json
from collections import defaultdict

globalSize = 0

def f_size(dic: defaultdict) -> int:
    global globalSize
    s = 0
    for k,v in dic.items():
        if isinstance(v,str):
            s += int(v)
        else:
            s += f_size(v)

    if s <= 100000:
        globalSize += s

    return s

def getCd(cd: defaultdict, p: list):

    if len(p) > 1:
        for key in p[:-1]:
            cd = cd[key]

    return cd


def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    main = defaultdict(dict)
    path = []
    lines = []


    for word in src:
        lines.append(word.split())

    for words in lines:
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    path.pop()
                else:
                    path.append(words[2])
        else:
            cd = getCd(main,path)

            if words[0] == "dir":
                cd[path[-1]][words[1]] = defaultdict(dict)
            else:
                cd[path[-1]][words[1]] = words[0]

    print(json.dumps(main, indent=4))
    f_size(main)

    print(globalSize)





def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

if __name__ == "__main__":
    main()