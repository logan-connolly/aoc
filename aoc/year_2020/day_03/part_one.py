from aoc.year_2020.day_03 import move


def solve(data):
    """Day 3: Toboggan Trajectory (part 1)"""
    down, right = (1, 3)
    return move.shift(data, down, right)
