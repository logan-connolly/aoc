from typing import Optional

from aoc.abstracts.solver import Answers, IntLines


def find_and_transform_match(lines: IntLines, target: int) -> Optional[int]:
    """Build up set and perform transform if found"""
    seen_nums = set()
    for num in lines:
        if num in seen_nums:
            return num * (target - num)
        seen_nums.add(target - num)
    return None


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> IntLines:
        return [int(line) for line in self.data.splitlines()]

    def _solve_part_one(self, lines: IntLines) -> int:
        output = find_and_transform_match(lines, target=2020)
        return output if output else -1

    def _solve_part_two(self, lines: IntLines) -> int:
        first, *rest = lines
        new_target = 2020 - first
        match_output = find_and_transform_match(rest, target=new_target)
        if match_output:
            return first * match_output
        return self._solve_part_two(rest)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
