from collections import defaultdict
import math

def main():
    rounds = 10000

    monkeys = [
               [[83, 97, 95, 67],                   lambda x: x * 19,   17, (2,7)],
               [[71, 70, 79, 88, 56, 70],           lambda x: x + 2,    19, (7,0)],
               [[98, 51, 51, 63, 80, 85, 84, 95],   lambda x: x + 7,    7,  (4,3)],
               [[77, 90, 82, 80, 79],               lambda x: x + 1,    11, (6,4)],
               [[68],                               lambda x: x * 5,    13, (6,5)],
               [[60, 94],                           lambda x: x + 5,    3,  (1,0)],
               [[81, 51, 85],                       lambda x: x * x,    5,  (5,1)],
               [[98, 81, 63, 65, 84, 71, 84],       lambda x: x + 3,    2,  (2,3)],
            ]

    inspections = defaultdict(int)

    div = math.prod(monkey[2] for monkey in monkeys)
    print(div)

    for i in range(rounds):


        print(f"round = {i}")


        for i,monkey in enumerate(monkeys):
            while len(monkey[0]) > 0:
                item = monkey[1](monkey[0].pop(0)) % div # // 3 for part 1
                inspections[i] += 1

                if item % monkey[2] == 0:
                    monkeys[monkey[3][0]][0].append(item)
                else:
                    monkeys[monkey[3][1]][0].append(item)

    print()
    for key,value in inspections.items():
        print(key,value)

    inspections = sorted(inspections.values(),reverse=True)
    print(inspections)
    print(inspections[0] * inspections[1])








if __name__ == "__main__":
    main()