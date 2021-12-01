from aoc.year_2020.day_09.util import find_weakness, recursive_check


def solve(data: list[int]) -> int:
    """Day 09: Encoding Error (part 2)"""
    target = recursive_check(data, preamble=25)
    subset = data[: data.index(target)]
    return find_weakness(subset, target)
