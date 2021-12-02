from typing import Optional

from aoc.abstracts.solver import Answers, IntLines


def compare(prev: Optional[int], curr: int) -> bool:
    if prev is not None:
        return curr > prev
    return False


def create_three_measurement_window(data: IntLines) -> IntLines:
    new_data = []
    for start_idx, _ in enumerate(data[:-2]):
        subset = data[start_idx : start_idx + 3]
        new_data.append(sum(subset))
    return new_data


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> IntLines:
        return [int(line) for line in self.data.splitlines()]

    def _solve_part_one(self, lines: IntLines) -> int:
        lagged = [None, *lines[:-1]]
        return sum(compare(prev, curr) for prev, curr in zip(lagged, lines))

    def _solve_part_two(self, lines: IntLines) -> int:
        window_data = create_three_measurement_window(lines)
        lagged = [None, *window_data[:-1]]
        return sum(compare(prev, curr) for prev, curr in zip(lagged, window_data))

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
