from dataclasses import dataclass


@dataclass
class Assignment:
    start: int
    end: int

    def contains(self, other: "Assignment") -> bool:
        return self.start <= other.start and self.end >= other.end


def readAssignment(part: str) -> Assignment:
    start, end = part.split("-")
    return Assignment(int(start), int(end))


def readLine(line: str) -> tuple[Assignment, Assignment]:
    part1, part2 = line.split(",")
    return readAssignment(part1), readAssignment(part2)


def readLines(txt: str) -> list[tuple[Assignment, Assignment]]:
    return [readLine(line) for line in txt.splitlines() if line.strip() != ""]


def countOverlapping(assignments: list[tuple[Assignment, Assignment]]) -> int:
    count = 0
    for pair in assignments:
        if pair[0].contains(pair[1]) or pair[1].contains(pair[0]):
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
    n_overlapping = countOverlapping(assignments)

    assert n_overlapping == 2
