"""This is the Solution for Year 2021 Day 10"""

from aoc.abstracts.solver import Answers, StrLines


BRACKET_MAP = {"[": "]", "(": ")", "<": ">", "{": "}"}


def find_corrupt_char(line: str, idx: int = 0) -> str:
    """Recursively validate characters in line returning corrupt char"""

    if len(line) == idx + 1:
        return ""

    current_char, next_char = line[idx], line[idx + 1]

    if next_char in BRACKET_MAP:
        return find_corrupt_char(line, idx + 1)

    if BRACKET_MAP[current_char] == next_char:
        matching_pair_removed = line[:idx] + line[idx + 2 :]
        return find_corrupt_char(matching_pair_removed, idx - 1)

    return next_char


def score_corrupt_char(char: str) -> int:
    """Return score for corrupt character, else 0"""
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return scores.get(char, 0)


def update_append_score(score: int, char: str) -> int:
    """Return updated score with appended character"""
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    return (score * 5) + scores[char]


def get_append_score(line: str, score: int = 0) -> int:
    """Use part one solution for finding corrupt characters to append missing"""
    for closing_bracket in BRACKET_MAP.values():
        try:
            corrupt = find_corrupt_char(line + closing_bracket, idx=0)
        except KeyError:
            break
        if not corrupt:
            updated_score = update_append_score(score, closing_bracket)
            return get_append_score(line + closing_bracket, updated_score)
    return score


def get_winner(scores: list[int]) -> int:
    """Determine winner by taking the median score"""
    sorted_scores = sorted(scores)
    middle_idx = len(sorted_scores) // 2
    return sorted_scores[middle_idx]


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        corrupt_chars = [find_corrupt_char(line) for line in lines]
        return sum(score_corrupt_char(char) for char in corrupt_chars)

    def _solve_part_two(self, lines: StrLines) -> int:
        incomplete_lines = [line for line in lines if not find_corrupt_char(line)]
        scores = [get_append_score(line) for line in incomplete_lines]
        return get_winner(scores)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
