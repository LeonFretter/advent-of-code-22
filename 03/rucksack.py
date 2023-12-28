type Compartments = tuple[str, str]

def readCompartments(line: str) -> Compartments:
    l = len(line)
    return line[:l // 2], line[l // 2:]


def reorderPrio(a: str) -> int:
    if a.islower():
        return ord(a) - ord("a") + 1
    else:
        return ord(a) - ord("A") + 27


def getMultiOccuring(compartments: Compartments) -> set[str]:
    return set(compartments[0]).intersection(set(compartments[1]))


def getReorderPrios(compartments: Compartments) -> list[int]:
    return sorted([reorderPrio(a) for a in getMultiOccuring(compartments)])


def getReorderPrio(compartments: Compartments) -> int:
    return sum(getReorderPrios(compartments))


def readLines(txt: str) -> list[Compartments]:
    return [readCompartments(line) for line in txt.splitlines() if line.strip() != ""]


def getTotalReorderPrio(compartments: list[Compartments]) -> int:
    return sum([getReorderPrio(compartment) for compartment in compartments])


type Group = tuple[Compartments, Compartments, Compartments]


def getGroups(compartments: list[Compartments]) -> list[Group]:
    groups = []
    for i in range(0, len(compartments), 3):
        groups.append((compartments[i], compartments[i + 1], compartments[i + 2]))
    return groups


def getGroupBadge(group: Group) -> str:
    rucksacks = [compartment[0] + compartment[1] for compartment in group]
    shared_letters = set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2]))
    return shared_letters.pop()


def getGroupsReorderPrios(groups: list[Group]) -> list[int]:
    return [reorderPrio(getGroupBadge(group)) for group in groups]


def getTotalGroupsReorderPrio(groups: list[Group]) -> int:
    return sum(getGroupsReorderPrios(groups))


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

    groups = getGroups(compartments)
    group_prios = getGroupsReorderPrios(groups)
    res = getTotalGroupsReorderPrio(groups)

    assert res == 70
