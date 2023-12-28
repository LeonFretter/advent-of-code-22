from typing import Optional
from dataclasses import dataclass


type Crate = str
type Stack = list[Crate]
type Stacks = dict[int, Stack]


def readCrate(txt: str) -> Crate:
    return txt.strip().strip("[]")


def readCrateLine(line: str) -> dict[int, Optional[Crate]]:
    res: dict[int, Optional[Crate]] = {}
    key = 1
    for i in range(0, len(line), 4):
        part = line[i:i + 4]
        if part.strip() == "":
            res[key] = None
        else:
            res[key] = readCrate(part)
        key += 1
    return res


def readStacks(lines: list[str]) -> Stacks:
    res: Stacks = {}
    for line in lines:
        crate_line = readCrateLine(line)
        for key in crate_line:
            crate = crate_line[key]
            if crate is not None:
                if key in res:
                    res[key].insert(0, crate)
                else:
                    res[key] = [crate]
    return res


@dataclass
class Instruction:
    amount: int
    src: int
    dst: int

    def execute(self, stacks: Stacks, multi=False) -> None:
        src = stacks[self.src]
        dst = stacks[self.dst]
        if multi:
            subr = src[-self.amount:]
            dst.extend(subr)
            del src[-self.amount:]
        else:
            for _ in range(self.amount):
                dst.append(src.pop())


def readInstruction(line: str) -> Instruction:
    amount_txt, rest_txt = line.split("from")
    amount_txt = amount_txt[4:].strip()
    amount = int(amount_txt)
    src_txt, dst_txt = [x.strip() for x in rest_txt.split("to")]
    src, dst = int(src_txt), int(dst_txt)
    return Instruction(amount, src, dst)


def readInstructions(lines: list[str]) -> list[Instruction]:
    return [readInstruction(line) for line in lines]


@dataclass
class ProblemSet:
    stacks: Stacks
    instructions: list[Instruction]

    @staticmethod
    def fromText(txt: str) -> "ProblemSet":
        lines = txt.splitlines()
        end_stack_idx = lines.index("") - 1
        stacks = readStacks(lines[:end_stack_idx])
        instructions = readInstructions(lines[end_stack_idx + 2:])
        return ProblemSet(stacks, instructions)

    def execute(self, multi=False) -> None:
        for instruction in self.instructions:
            instruction.execute(self.stacks, multi=multi)

    def getTopValues(self) -> str:
        res = []
        for key in sorted(self.stacks.keys()):
            stack = self.stacks[key]
            if len(stack) > 0:
                res.append(stack[-1])
        return "".join(res)


if __name__ == "__main__":
    txt = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2\
"""
    problem_set = ProblemSet.fromText(txt)
    assert len(problem_set.stacks.values()) == 3
    assert len(problem_set.instructions) == 4

    first_stack = problem_set.stacks[1]
    assert first_stack == ["Z", "N"]
    second_stack = problem_set.stacks[2]
    assert second_stack == ["M", "C", "D"]
    third_stack = problem_set.stacks[3]
    assert third_stack == ["P"]

    problem_set.execute()
    res = problem_set.getTopValues()
    assert res == "CMZ"

    new_problem_set = ProblemSet.fromText(txt)
    new_problem_set.execute(multi=True)
    new_res = new_problem_set.getTopValues()

    assert new_res == "MCD"
