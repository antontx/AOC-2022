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

    seen = 0
    for r,row in enumerate(t_map):
        print(row)
        for i,tree in enumerate(row):
            visible = False
            #left
            if (i == 0 or (tree > max(row[:i]) and tree > row[0])) and visible is False:
                if not i == 0:
                    print(f"{tree}({i})({visible}) left {tree} > {max(row[:i])}: {row[:i]} - {seen=}")
                else:
                    print(f"{tree}({i})({visible}) left (start) - {seen=}")
                seen += 1
                visible = True

            #right
            elif (i == len(row)-1 or (tree > max(row[i+1:]) and tree > row[len(row)-1]))and visible is False:
                if not i == len(row)-1:
                    print(f"{tree}({i})({visible}) right {tree} > {max(row[i+1:])}: {row[i+1:]} - {seen=}")
                else:
                    print(f"{tree}({i})({visible}) right (start) - {seen=}")
                seen += 1
                visible = True


            row = t_mapTD[i]
            tree = row[r]

            # top
            if (r == 0 or (tree > max(row[:r]) and tree > row[0])) and visible is False:
                if not r == 0:
                    print(f"{tree}({i})({visible}) top {tree} > {max(row[:r])}: {row[:r]} - {seen=}")
                else:
                    print(f"{tree}({i})({visible}) top (start) - {seen=}")
                seen += 1

                visible = True

            # down
            elif (r == len(row) - 1 or (tree > max(row[r + 1:]) and tree > row[len(row) - 1])) and visible is False:
                if not r == len(row) - 1:
                    print(f"{tree}({r})({visible}) down {tree} > {max(row[r + 1:])}: {row[r + 1:]} - {seen=}")
                else:
                    print(f"{tree}({i})({visible}) down (start) - {seen=}")
                seen += 1
                visible = True




    print(seen)



def get_input_from_file(path: str) -> list:
    source = []
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

if __name__ == "__main__":
    main()