import os
from assembly import Execution, readInstructions, Register

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

with open(filename) as f:
    lines = f.readlines()
    instructions = readInstructions(lines)
    e = Execution(instructions, Register(1))
    e.run()

    signal_strengths = e.signal_strengths([20, 60, 100, 140, 180, 220])
    res = sum(signal_strengths)

    print(f"Part 1: {res}")

    e.draw()
    print(e)
