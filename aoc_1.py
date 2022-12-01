from typing import *
from itertools import groupby
from typing import List


def main():
    src = get_input_from_file("files/AOC_1/input.txt")
    src = [list(group) for key, group in groupby(src, lambda x: x == "") if not key]
    sums = []

    for sublist in src:
        sublist: list[int] = list(map(int, sublist))
        sums.append(sum(sublist))

    print(sorted(sums, reverse=True))


def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()