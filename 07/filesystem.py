from dataclasses import dataclass, field
from typing import override


@dataclass
class Node:
    name: str
    parent: "Node | None" = None
    children: "list[Node]" = field(default_factory=list)
    size: int = 0

    def get_child(self, name: str) -> "Node":
        for child in self.children:
            if child.name == name:
                return child

        raise ValueError(f"Child {name} not found")

    def is_directory(self) -> bool:
        return self.size == 0

    def is_file(self) -> bool:
        return self.size > 0

    def get_size(self) -> int:
        if self.is_file():
            return self.size
        else:
            return sum(child.get_size() for child in self.children)

    def get_directories(self) -> "list[Node]":
        if self.is_directory():
            res: list[Node] = [self]
            for child in self.children:
                res += child.get_directories()
            return res
        else:
            return []


type Path = list[Node]


@dataclass
class Command:
    def execute(self, path: Path) -> Path:
        raise NotImplementedError()


@dataclass
class CDCommand(Command):
    dst: str

    @override
    def execute(self, path: Path) -> Path:
        match self.dst:
            case "/":
                return [path[0]]
            case "..":
                return path[:-1]
            case _:
                node = path[-1]
                child = node.get_child(self.dst)
                assert child.is_directory()
                return path + [child]


def readContent(line: str) -> Node:
    if line[0:3] == "dir":
        name = line.split(" ")[1]
        return Node(name, None, [])
    else:
        size, name = line.split(" ")
        return Node(name, None, [], int(size))


@dataclass
class LSCommand(Command):
    contents: list[str]

    @override
    def execute(self, path: Path) -> Path:
        current_dir = path[-1]
        assert current_dir.is_directory()
        for content in self.contents:
            try:
                _ = current_dir.get_child(content)
            except ValueError:
                new_node = readContent(content)
                new_node.parent = current_dir
                current_dir.children.append(new_node)
        return path


def readCommand(lines: list[str]) -> Command:
    line = lines[0]
    assert line[0] == "$"
    cmd = line[1:].strip()
    if cmd[0:2] == "cd":
        arg = cmd.split(" ")[1]
        return CDCommand(arg)
    elif cmd[0:2] == "ls":
        contents = lines[1:]
        return LSCommand(contents)
    raise ValueError(f"Unknown command {cmd}")


def splitCommandTexts(lines: list[str]) -> list[list[str]]:
    res = []
    current = []
    for line in lines:
        if line[0] == "$":
            if current:
                res.append(current)
                current = []
        current.append(line)
    if current:
        res.append(current)
    return res


def readCommands(lines: list[str]) -> list[Command]:
    command_texts = splitCommandTexts(lines)
    return [readCommand(command_text) for command_text in command_texts]


@dataclass
class Execution:
    root: Node
    current_path: Path
    command_stack: list[Command]

    def step(self) -> None:
        if len(self.command_stack) > 0:
            cmd = self.command_stack.pop()
            self.current_path = cmd.execute(self.current_path)

    def execute(self) -> None:
        while len(self.command_stack) > 0:
            self.step()


def createExecution(lines: list[str]) -> Execution:
    root = Node("/", None, [])
    current_path: list[Node] = [root]
    commands = list(reversed(readCommands(lines)))
    return Execution(root, current_path, commands)


if __name__ == "__main__":
    txt = str("""\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k\
""")

    execution = createExecution(txt.split("\n"))
    execution.execute()

    assert execution.root.get_size() == 48381165

    at_most_100000_dirs = [dir for dir in execution.root.get_directories() if dir.get_size() <= 100000]
    res = sum(dir.get_size() for dir in at_most_100000_dirs)
    assert res == 95437
