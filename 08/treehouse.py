from dataclasses import dataclass


@dataclass
class TreeMap:
    tree_heights: list[list[int]]

    def is_visible(self, x: int, y: int) -> bool:
        height = self.tree_heights[y][x]
        east, west, north, south = True, True, True, True
        for xit in range(0, x):
            if self.tree_heights[y][xit] >= height:
                east = False
                break
        for xit in range(x + 1, len(self.tree_heights[y])):
            if self.tree_heights[y][xit] >= height:
                west = False
                break
        for yit in range(0, y):
            if self.tree_heights[yit][x] >= height:
                north = False
                break
        for yit in range(y + 1, len(self.tree_heights)):
            if self.tree_heights[yit][x] >= height:
                south = False
                break

        return any([east, west, north, south])

    def scenic_score(self, x: int, y: int) -> int:
        east, west, north, south = 0, 0, 0, 0
        for itx in range(x - 1, -1, -1):
            east += 1
            if self.tree_heights[y][itx] >= self.tree_heights[y][x]:
                break
        for itx in range(x + 1, len(self.tree_heights[y])):
            west += 1
            if self.tree_heights[y][itx] >= self.tree_heights[y][x]:
                break
        for ity in range(y - 1, -1, -1):
            north += 1
            if self.tree_heights[ity][x] >= self.tree_heights[y][x]:
                break
        for ity in range(y + 1, len(self.tree_heights)):
            south += 1
            if self.tree_heights[ity][x] >= self.tree_heights[y][x]:
                break
        return east * west * north * south

    def count_visible(self) -> int:
        count = 0
        for y in range(0, len(self.tree_heights)):
            for x in range(0, len(self.tree_heights[y])):
                if self.is_visible(x, y):
                    count += 1
        return count

    def find_best_scenic_score(self) -> int:
        best_score = 0
        for y in range(0, len(self.tree_heights)):
            for x in range(0, len(self.tree_heights[y])):
                if self.is_visible(x, y):
                    score = self.scenic_score(x, y)
                    if score > best_score:
                        best_score = score
        return best_score


def readTreeMap(lines: list[str]) -> TreeMap:
    res: list[list[int]] = []
    for line in lines:
        row = [int(c) for c in line.strip()]
        res.append(row)
    return TreeMap(res)


if __name__ == "__main__":
    txt = str("""\
30373
25512
65332
33549
35390\
""")
    tree_map = readTreeMap(txt.splitlines())
    n_visible = tree_map.count_visible()
    assert n_visible == 21

    best_scenic_score = tree_map.find_best_scenic_score()
    assert best_scenic_score == 8
