import os
from filesystem import createExecution

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()
    lines = [line for line in txt.split("\n") if line]
    execution = createExecution(lines)
    execution.execute()

    dirs = execution.root.get_directories()
    at_most_100000_dirs = [dir for dir in dirs if dir.get_size() <= 100000]
    res = sum(dir.get_size() for dir in at_most_100000_dirs)

    print(f"Part 1: {res}")
