import os
from calories import readCalories, popMax

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    res = readCalories(txt)
    max_calories = max(res)

    print(f"Part 1: {max_calories}")

    max_1, max_2, max_3 = popMax(res), popMax(res), popMax(res)

    part2 = sum([max_1, max_2, max_3])

    print(f"Part 2: {part2}")
