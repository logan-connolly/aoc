"""This is the Solution for Year 2020 Day 09"""

from copy import deepcopy

from aoc.abstracts.solver import Answers, IntLines


def valid_preamble(subset: IntLines, target: int) -> bool:
    """Check if the sum of two numbers in subset equal target"""
    target_set = set()
    for num in subset:
        if num in target_set:
            return True
        target_set.add(target - num)
    return False


def check_preamble(lines: IntLines, preamble: int) -> int:
    """Recursively check preamble until solution found"""
    nums = deepcopy(lines)
    subset, target = nums[:preamble], nums[preamble]
    if valid_preamble(subset, target):
        return check_preamble(nums[1:], preamble)
    return target


def find_weakness(nums: IntLines, target: int) -> int:
    """Find a subset that matches target"""
    weakness = -1
    for idx, _ in enumerate(nums):
        for end_idx in range(idx, len(nums) - 1):
            subset = nums[idx:end_idx]
            if sum(subset) == target:
                weakness = min(subset) + max(subset)
                break
    return weakness


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> IntLines:
        return [int(line) for line in self.data.splitlines()]

    def _solve_part_one(self, lines: IntLines) -> int:
        return check_preamble(lines, preamble=25)

    def _solve_part_two(self, lines: IntLines) -> int:
        target = check_preamble(lines, preamble=25)
        subset = lines[: lines.index(target)]
        return find_weakness(subset, target)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
