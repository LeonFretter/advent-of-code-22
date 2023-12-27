def readCalories(txt: str) -> list[int]:
    res: list[int] = []
    current = 0
    for line in txt.splitlines():
        if line == "":
            res.append(current)
            current = 0
        else:
            current += int(line)
    res.append(current)
    return res


def popMax(calories: list[int]) -> int:
    max_calories = max(calories)
    max_index = calories.index(max_calories)
    calories.pop(max_index)
    return max_calories


if __name__ == "__main__":
    txt = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
"""
    res = readCalories(txt)
    max_calories = max(res)
    assert max_calories == 24000
