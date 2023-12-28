from dataclasses import dataclass


@dataclass
class Assignment:
    start: int
    end: int

    def contains(self, other: "Assignment") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Assignment") -> bool:
        return self.start <= other.end and other.start <= self.end

def readAssignment(part: str) -> Assignment:
    start, end = part.split("-")
    return Assignment(int(start), int(end))


def readLine(line: str) -> tuple[Assignment, Assignment]:
    part1, part2 = line.split(",")
    return readAssignment(part1), readAssignment(part2)


def readLines(txt: str) -> list[tuple[Assignment, Assignment]]:
    return [readLine(line) for line in txt.splitlines() if line.strip() != ""]


def isContained(a: Assignment, b: Assignment) -> bool:
    return a.contains(b) or b.contains(a)


def overlaps(a: Assignment, b: Assignment) -> bool:
    return a.overlaps(b) or b.overlaps(a)


def countContained(assignments: list[tuple[Assignment, Assignment]]) -> int:
    count = 0
    for pair in assignments:
        if isContained(pair[0], pair[1]):
            count += 1
    return count


def countOverlapping(assignments: list[tuple[Assignment, Assignment]]) -> int:
    count = 0
    for pair in assignments:
        if overlaps(pair[0], pair[1]):
            count += 1
    return count


if __name__ == "__main__":
    txt = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8\
"""

    assignments = readLines(txt)
    n_contained = countContained(assignments)

    assert n_contained == 2

    n_overlapping = countOverlapping(assignments)

    assert n_overlapping == 4
