from dataclasses import dataclass, field
from typing import override


@dataclass
class Register:
    value: int


@dataclass
class Instruction:
    def execute(self, register: Register) -> int:
        raise NotImplementedError()


@dataclass
class NoopInstruction(Instruction):
    @override
    def execute(self, register: Register) -> int:
        return 1


@dataclass
class AddInstruction(Instruction):
    value: int

    @override
    def execute(self, register: Register) -> int:
        register.value += self.value
        return 2


@dataclass
class Execution:
    instructions: list[Instruction]
    register: Register
    idx = 0
    hist: list[int] = field(default_factory=list)
    screen: list[str] = field(default_factory=list)

    def step(self) -> None:
        instruction = self.instructions[self.idx]
        new_register = Register(self.register.value)
        n_cycles = instruction.execute(new_register)
        for _ in range(n_cycles):
            self.hist.append(self.register.value)
        self.register.value = new_register.value
        self.idx += 1

    def get_value(self, idx: int) -> int:
        return self.hist[idx - 1]

    def get_values(self, idxs: list[int]) -> list[int]:
        return [self.get_value(idx) for idx in idxs]

    def signal_strength(self, idx: int) -> int:
        return idx * self.get_value(idx)

    def signal_strengths(self, idxs: list[int]) -> list[int]:
        return [self.signal_strength(idx) for idx in idxs]

    def run(self) -> None:
        while self.idx < len(self.instructions):
            self.step()

    def sprite_center(self, idx: int) -> int:
        return self.get_value(idx)

    def sprite_positions(self, idx: int) -> list[int]:
        center = self.sprite_center(idx + 1)
        return [center - 1, center, center + 1]

    def screen_position(self, idx: int) -> tuple[int, int]:
        x = idx % 40
        y = idx // 40
        return x, y

    def draw(self) -> None:
        for _ in range(6):
            self.screen.append("." * 40)

        for idx in range(240):
            x, y = self.screen_position(idx)
            sprite_xs = self.sprite_positions(idx)
            if x in sprite_xs:
                self.screen[y] = self.screen[y][:x] + "#" + self.screen[y][x + 1:]

    def __str__(self) -> str:
        return "\n".join(self.screen)


def readInstruction(line: str) -> Instruction:
    if line == "noop":
        return NoopInstruction()
    else:
        _, value = line.split()
        return AddInstruction(int(value))


def readInstructions(lines: list[str]) -> list[Instruction]:
    return [readInstruction(line.strip()) for line in lines if line.strip()]


if __name__ == "__main__":
    txt = str("""\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop\
""")
    lines = txt.splitlines()
    instructions = readInstructions(lines)
    e = Execution(instructions, Register(1))

    e.run()
    values = e.get_values([20, 60, 100, 140, 180, 220])
    assert values == [21, 19, 18, 21, 16, 18]
    signal_strengths = e.signal_strengths([20, 60, 100, 140, 180, 220])
    res = sum(signal_strengths)
    assert res == 13140

    e.draw()
    print(e)
