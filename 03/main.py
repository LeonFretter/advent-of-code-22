import os
from rucksack import getTotalReorderPrio, readLines, getTotalGroupsReorderPrio, getGroups

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    compartments = readLines(txt)

    part1 = getTotalReorderPrio(compartments)

    print(f"Part 1: {part1}")

    groups = getGroups(compartments)

    part2 = getTotalGroupsReorderPrio(groups)

    print(f"Part 2: {part2}")
