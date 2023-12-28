import os
from treehouse import TreeMap, readTreeMap

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

with open(filename) as f:
    tree_map = readTreeMap(f.readlines())
    n_visible = tree_map.count_visible()

    print(f"Part 1: {n_visible}")

    best_score = tree_map.find_best_scenic_score()
    print(f"Part 2: {best_score}")
