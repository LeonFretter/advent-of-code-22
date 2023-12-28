from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

    def to_vec2(self) -> "Vec2":
        if self == Direction.UP:
            return Vec2(0, 1)
        elif self == Direction.DOWN:
            return Vec2(0, -1)
        elif self == Direction.LEFT:
            return Vec2(-1, 0)
        elif self == Direction.RIGHT:
            return Vec2(1, 0)
        else:
            raise ValueError(f"Unknown direction: {self}")


@dataclass
class Instruction:
    direction: Direction
    steps: int


@dataclass
class Vec2:
    x: int
    y: int

    def __mul__(self, other: int):
        return Vec2(self.x * other, self.y * other)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Rope:
    head: Vec2
    tail: Vec2

    def move(self, instruction: Instruction) -> list[Vec2]:
        tail_marks: list[Vec2] = [self.tail]
        for _ in range(instruction.steps):
            old_head = self.head
            self.head += instruction.direction.to_vec2()
            diff = self.head - self.tail
            if abs(diff.x) > 1 or abs(diff.y) > 1:
                self.tail = old_head
                tail_marks.append(self.tail)
        return tail_marks


def readInstruction(line: str) -> Instruction:
    direction = Direction(line[0])
    steps = int(line[1:])
    return Instruction(direction, steps)


def readInstructions(lines: list[str]) -> list[Instruction]:
    return [readInstruction(line) for line in lines]


if __name__ == "__main__":
    txt = str("""\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2\
""")
    lines = txt.splitlines()
    instructions = readInstructions(lines)
    r = Rope(Vec2(0, 0), Vec2(0, 0))

    tail_marks: list[Vec2] = []
    for instruction in instructions:
        tail_marks += r.move(instruction)
    tail_marks = list(set(tail_marks))
    assert len(tail_marks) == 13
