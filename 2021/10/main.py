"""This is the Solution for Year 2021 Day 10"""

import aoc

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


@aoc.expect(26397)
def part_one(lines: aoc.StrLines) -> int:
    corrupt_chars = [find_corrupt_char(line) for line in lines]
    return sum(score_corrupt_char(char) for char in corrupt_chars)


@aoc.expect(288957)
def part_two(lines: aoc.StrLines) -> int:
    incomplete_lines = [line for line in lines if not find_corrupt_char(line)]
    scores = [get_append_score(line) for line in incomplete_lines]
    return get_winner(scores)


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
