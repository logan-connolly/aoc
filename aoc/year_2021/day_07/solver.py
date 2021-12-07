"""This is the Solution for Year 2021 Day 07"""

from functools import lru_cache

from aoc.abstracts.solver import Answers, IntLines


@lru_cache
def get_crab_engineering_value(fuel_needed: int) -> int:
    """Use formula n(n+1)/2 to find sum of continous set of integers"""
    return int(fuel_needed * (fuel_needed + 1) / 2)


def evaluate_fuel_needed(crabs: IntLines, value: int, advanced: bool) -> int:
    """Evaluate fuel needed to move crabs to a given horizontal position value"""
    if not advanced:
        return sum(abs(num - value) for num in crabs)
    return sum(get_crab_engineering_value(abs(num - value)) for num in crabs)


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> IntLines:
        str_entries = self.data.strip("\n").split(",")
        return sorted([int(item) for item in str_entries])

    def _solve_part_one(self, lines: IntLines) -> int:
        n_range = range(min(lines), max(lines) + 1)
        return min(evaluate_fuel_needed(lines, n, advanced=False) for n in n_range)

    def _solve_part_two(self, lines: IntLines) -> int:
        n_range = range(min(lines), max(lines) + 1)
        return min(evaluate_fuel_needed(lines, n, advanced=True) for n in n_range)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
