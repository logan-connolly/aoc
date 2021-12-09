"""This is the Solution for Year 2021 Day 08"""

import itertools
from collections import Counter, defaultdict

from aoc.abstracts.solver import Answers, StrLines

UNIQUE_SEGMENTS = {2: 1, 3: 7, 4: 4, 7: 8}


def count_unique_segment_length(lines: StrLines) -> int:
    """Count all unique segment codes in input lines"""
    output_codes = (line.split()[-4:] for line in lines)
    combined_output_codes = itertools.chain.from_iterable(output_codes)
    counter = Counter(len(code) for code in combined_output_codes)
    return sum(count for length, count in counter.items() if length in UNIQUE_SEGMENTS)


def decode_line(signals: str) -> int:
    """Using set operations decode the value for four digit seven-segment display

    input:     be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb
    output:    fdgacbe cefdb cefbgd gcbe (decoded: 8394)
    unique:    (len=2=>1, len=4=>4, len=3=>7, len=7=>8)
    ambiguous: (len=5=>2|3|5, len=6=>0|6|9)
    """
    digit_character_set: dict[int, set] = defaultdict(set)
    codes = signals.split()
    input_codes, output_codes = codes[:-4], codes[-4:]

    # run through once and populate set with unique codes character sets (1, 4, 7, 8)
    for code in input_codes:
        n_characters = len(code)
        if n_characters in UNIQUE_SEGMENTS:
            digit_character_set[UNIQUE_SEGMENTS[n_characters]] = set(code)

    # loop through again and make comparisons based on information from unique chars
    for code in input_codes:
        n_characters = len(code)
        character_set = set(code)

        # when len=5 => 2|3|5,
        if n_characters == 5:
            # character intersection of 3 and 1 == 1
            if character_set & digit_character_set[1] == digit_character_set[1]:
                digit_character_set[3] = character_set
            # character union of 2 and 4 == 8
            elif character_set | digit_character_set[4] == digit_character_set[8]:
                digit_character_set[2] = character_set
            else:
                digit_character_set[5] = character_set

        # len=6 => 0|6|9
        elif n_characters == 6:
            # character union of 6 and 7 == 8
            if character_set | digit_character_set[7] == digit_character_set[8]:
                digit_character_set[6] = character_set
            # character intersection of 9 and 4 == 4
            elif character_set & digit_character_set[4] == digit_character_set[4]:
                digit_character_set[9] = character_set
            else:
                digit_character_set[0] = character_set

    reverse_lookup = {frozenset(s): str(v) for v, s in digit_character_set.items()}
    decoded = "".join(reverse_lookup[frozenset(code)] for code in output_codes)
    return int(decoded) if decoded else -1


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return [line.replace(" | ", " ") for line in self.data.splitlines()]

    def _solve_part_one(self, lines: StrLines) -> int:
        return count_unique_segment_length(lines)

    def _solve_part_two(self, lines: StrLines) -> int:
        return sum(decode_line(line) for line in lines)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
