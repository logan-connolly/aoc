from copy import deepcopy
from math import prod

from aoc.abstracts.solver import Answers, StrLines


def count_trees(lines: StrLines, down: int, right: int) -> int:
    """Count trees for given down/right shift"""
    tmap = deepcopy(lines)
    row_index, tree_count = 0, 0
    for row in tmap[down::down]:
        row_index += right
        if row[row_index % len(row)] == "#":
            tree_count += 1
    return tree_count


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        down, right = 1, 3
        return count_trees(lines, down, right)

    def _solve_part_two(self, lines: StrLines) -> int:
        shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
        counts = (count_trees(lines, down, right) for right, down in shifts)
        return prod(counts)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
