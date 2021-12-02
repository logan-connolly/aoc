from aoc.year_2021.day_01.util import compare


def solve(data):
    """Year 2021 Day 1 Part 1"""
    lagged = [None, *data[:-1]]
    return sum(compare(prev, curr) for prev, curr in zip(lagged, data))
