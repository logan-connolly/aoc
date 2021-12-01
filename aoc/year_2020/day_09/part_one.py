from aoc.year_2020.day_09.util import recursive_check


def solve(data: list[int]) -> int:
    """Day 09: Encoding Error (part 1)"""
    return recursive_check(data, preamble=25)
