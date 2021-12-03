"""This is the Solution for Year 2020 Day 05"""

from aoc.abstracts.solver import Answers, StrLines


def get_seat_id(ticket: str) -> int:
    """Get seat id based on boarding ticket (ie. 'BBFFBBFRLL')"""

    rows = range(128)
    cols = range(8)

    for letter in ticket:
        if letter in "FB":
            midpoint = len(rows) // 2
            rows = rows[:midpoint] if letter == "F" else rows[midpoint:]
        else:
            midpoint = len(cols) // 2
            cols = cols[:midpoint] if letter == "L" else cols[midpoint:]

    return rows[0] * 8 + cols[0]


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        return max(get_seat_id(ticket) for ticket in lines)

    def _solve_part_two(self, lines: StrLines) -> int:
        seat_ids = [get_seat_id(ticket) for ticket in lines]
        available_seat_set = set(range(min(seat_ids), max(seat_ids) + 1))
        return (available_seat_set - set(seat_ids)).pop()

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
