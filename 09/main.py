import os
from rope import readInstructions, Rope, Vec2

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

with open(filename) as f:
    txt = f.readlines()
    instructions = readInstructions(txt)
    rope = Rope(head=Vec2(0, 0), tail=Vec2(0, 0))
    tail_marks = []
    for instruction in instructions:
        tail_marks.extend(rope.move(instruction))
    tail_marks = list(set(tail_marks))

    print(f"Part 1: {len(tail_marks)}")
