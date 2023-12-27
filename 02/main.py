import os
from rock_paper_scissors import RockPaperScissors, readLines, scoreGames, readNewGames, scoreNewGames

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename) as f:
    txt = f.read()

    games = readLines(txt)

    part1 = scoreGames(games)

    print(f"Part 1: {part1}")

    new_games = readNewGames(txt)

    part2 = scoreNewGames(new_games)

    print(f"Part 2: {part2}")
