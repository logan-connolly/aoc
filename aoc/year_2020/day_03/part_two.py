from math import prod

from . import part_one


def solve(tmap):
    """Day 3: Toboggan Trajectory (part 2)"""
    shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (part_one.solve(tmap, down, right) for right, down in shifts)
    return prod(counts)
