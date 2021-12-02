import re

from aoc.abstracts.solver import Answers, StrLines


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        delim = "\n\n"
        return self.data.split(delim)

    def _solve_part_one(self, lines: StrLines) -> int:
        cleaned = [re.sub(r"\n", "", answer).strip() for answer in lines]
        return sum(len(set(answer)) for answer in cleaned)

    def _solve_part_two(self, lines: StrLines) -> int:
        cleaned = [answer.rstrip("\n").split("\n") for answer in lines]
        shared_answer_count = 0
        for group in cleaned:
            shared_answers = set.intersection(*[set(member) for member in group])
            shared_answer_count += len(shared_answers)
        return shared_answer_count

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
