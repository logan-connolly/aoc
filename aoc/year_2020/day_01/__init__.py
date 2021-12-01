from aoc.io import read_input
from aoc.year_2020.day_01 import part_one, part_two


def solution():
    nums = read_input(year=2020, day=1, as_int=True)
    print(f"Day 01 Part 1: {part_one.solve(nums)}")
    print(f"Day 01 Part 2: {part_two.solve(nums)}")
