from math import copysign

def oneDimension(head, tail):
    # horizontal movement
    if head[1] == tail[1]:
        if tail[0] < head[0]:
            tail[0] = head[0] - 1
        elif tail[0] > head[0]:
            tail[0] = head[0] + 1
    # vertical movement
    elif head[0] == tail[0]:
        if tail[1] < head[1]:
            tail[1] = head[1] - 1
        elif tail[1] > head[1]:
            tail[1] = head[1] + 1

def isAdjacent(head: list, tail: list):
    if max(abs(head[0] - tail[0]),abs(head[1] - tail[1])) <= 1:
        return True
    return False


def moveTail(head, tail,visited):
    if not isAdjacent(head, tail):
        oneDimension(head, tail)

        # diagonal movement

        x = copysign(1,head[0] - tail[0])
        y = copysign(1,head[1] - tail[1])


        while head[0] != tail[0] and head[1] != tail[1]:
            tail[0] += x
            tail[1] += y


        oneDimension(head,tail)



def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    steps = []
    for line in src:
        line = line.split(" ")
        for i in range(int(line[1])):
            steps.append((line[0],1))

    print(steps)

    head = [0,0]
    tail = [0,0]
    visited = set()


    print(f"{head=},{tail=}")
    for step in steps:

        #move head
        if step[0] == "L":
            head[0] -= step[1]
        elif step[0] == "R":
            head[0] += step[1]
        elif step[0] == "U":
            head[1] += step[1]
        elif step[0] == "D":
            head[1] -= step[1]


        #move tail
        moveTail(head,tail,visited)



        print(f"{step},{head=},{tail=}")

        visited.add(tuple(tail))

    print(visited)
    print(len(visited))


def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source


if __name__ == "__main__":
    main()