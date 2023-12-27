import os
from rucksack import getTotalReorderPrio, readLines

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    compartments = readLines(txt)

    part1 = getTotalReorderPrio(compartments)

    print(f"Part 1: {part1}")
