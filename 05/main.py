import os
from cargo import ProblemSet

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    problem_set = ProblemSet.fromText(txt)
    problem_set.execute()
    res = problem_set.getTopValues()
    print(f"Part 1: {res}")

    new_problem_set = ProblemSet.fromText(txt)
    new_problem_set.execute(multi=True)
    new_res = new_problem_set.getTopValues()
    print(f"Part 2: {new_res}")
