import os
from assignments import readLines, countContained, countOverlapping

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    assignments = readLines(txt)

    part1 = countContained(assignments)
    print(f"Part 1: {part1}")

    part2 = countOverlapping(assignments)
    print(f"Part 2: {part2}")
