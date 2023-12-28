import os
from marker import findMarker

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()
    res = findMarker(txt)

    print(f"Part 1: {res}")

    res2 = findMarker(txt, marker_len=14)
    print(f"Part 2: {res2}")
