def get_input_from_file(path: str) -> list:
    with open(path, "r") as file:
        source = [line.rstrip() for line in file]

    file.close()
    return source

def get_points(a: str, b: str):
    temp_score = points[b]

    if points[a] == points[b]:
        temp_score += 3
    elif points[a] == order[order.index(points[b]) - 1]:
        temp_score += 6

    return temp_score


src = get_input_from_file("files/AOC_1/test.txt")
sets = []
score = 0
for element in src:
    sets.append(element.split(" "))

points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

order = [3, 1, 2, 3, 1, 2]

# part 1
for duel in sets:
    score += get_points(duel[0], duel[1])

print(f"part 1:{score}")

# part 2
score = 0
for duel in sets:
    if duel[1] == "X":
        score += 0 + order[order.index(points[duel[0]]) - 1]
    elif duel[1] == "Y":
        score += 3 + points[duel[0]]

    else:
        score += 6 + order[order.index(points[duel[0]]) + 1]

print(f"part 2:{score}")