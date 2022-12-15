import string


def find_max_calories(filename: string):
    maxCalories = 0
    topThree = []
    counter = 0
    with open(filename, "r") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            if not line.strip() or idx == len(lines) - 1:
                if len(topThree) < 3:
                    topThree.append(counter)
                elif min(topThree) < counter:
                    topThree[topThree.index(min(topThree))] = counter
                counter = 0

            else:
                counter += int(line.strip())

    print(sum(topThree))
