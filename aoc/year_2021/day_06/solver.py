"""This is the Solution for Year 2021 Day 06"""

from functools import lru_cache

from aoc.abstracts.solver import Answers, IntLines


@lru_cache
def count_offspring(cycle: int, days: int) -> int:
    """Counts how many offspring will be spawn over a given period"""
    if cycle > days or cycle == days:
        return 1
    elif cycle == 0:
        return count_offspring(8, days - 1) + count_offspring(6, days - 1)
    else:
        return count_offspring(cycle - 1, days - 1)


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> IntLines:
        str_entries = self.data.strip("\n").split(",")
        return [int(item) for item in str_entries]

    def _solve_part_one(self, lines: IntLines) -> int:
        return sum(count_offspring(n, 80) for n in lines)

    def _solve_part_two(self, lines: IntLines) -> int:
        return sum(count_offspring(n, 256) for n in lines)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
