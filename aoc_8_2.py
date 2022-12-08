from pprint import pprint

def main():
    src = get_input_from_file("files/AOC_1/test.txt")
    t_map = []
    for word in src:
        nums = list(word)
        nums = list(map(int,nums))
        t_map.append(nums)


    row = True
    col = True

    t_mapTD = [[row[i] for row in t_map] for i in range(len(t_map[0]))]
    # pprint(t_map,width=1000,indent=0)
    # pprint(t_mapTD,width=1000)

    score =  []
    distance = 0
    for r,row in enumerate(t_map):
        print()
        print(row)
        for i,tree in enumerate(row):
            left = []
            right = []
            top = []
            down = []
            print()


            #left
            j = 0
            while i-j-1 >= 0:
                left.append(row[i-j-1])
                if row[i-j-1] >= tree:
                    break
                j += 1


            print(f"left {tree} : {left}")

            #right

            j = 0
            while i + j + 1 <= len(row)-1:
                right.append(row[i + j + 1])
                if row[i + j + 1] >= tree:
                    break
                j += 1

            print(f"right {tree} : {right}")

            row2 = t_mapTD[i] #zeile in neuer map
            tree = row2[r] # r = neuer index des trees

            j = 0
            while r - j - 1 >= 0:
                top.append(row2[r - j - 1])
                if row2[r - j - 1] >= tree:
                    break
                j += 1

            print(f"left {tree} : {left}")

            # right

            j = 0
            while r + j + 1 <= len(row2) - 1:
                down.append(row2[r + j + 1])
                if row2[r + j + 1] >= tree:
                    break
                j += 1

            print(f"right {tree} : {right}")

            score.append(len(left)*len(right)*len(top)*len(down))
    print(max(score))








def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

if __name__ == "__main__":
    main()