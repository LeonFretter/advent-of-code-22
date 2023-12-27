def readCompartments(line: str) -> tuple[str, str]:
    l = len(line)
    return line[:l // 2], line[l // 2:]


def reorderPrio(a: str) -> int:
    if a.islower():
        return ord(a) - ord("a") + 1
    else:
        return ord(a) - ord("A") + 27


def getMultiOccuring(compartments: tuple[str, str]) -> set[str]:
    return set(compartments[0]).intersection(set(compartments[1]))


def getReorderPrios(compartments: tuple[str, str]) -> list[int]:
    return sorted([reorderPrio(a) for a in getMultiOccuring(compartments)])


def getReorderPrio(compartments: tuple[str, str]) -> int:
    return sum(getReorderPrios(compartments))


def readLines(txt: str) -> list[tuple[str, str]]:
    return [readCompartments(line) for line in txt.splitlines() if line.strip() != ""]


def getTotalReorderPrio(compartments: list[tuple[str, str]]) -> int:
    return sum([getReorderPrio(compartment) for compartment in compartments])


if __name__ == "__main__":
    txt = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""
    compartments = readLines(txt)
    res = getTotalReorderPrio(compartments)

    assert res == 157
