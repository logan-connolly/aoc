from math import prod

from aoc.year_2020.day_03 import move


def solve(tmap):
    """Day 3: Toboggan Trajectory (part 2)"""
    shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (move.shift(tmap, down, right) for right, down in shifts)
    return prod(counts)
