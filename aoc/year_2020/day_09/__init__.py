from aoc.io import read_input
from aoc.year_2020.day_09 import part_one, part_two


def solution():
    nums = read_input(year=2020, day=9, as_int=True)
    print(f"Day 09 Part 1: {part_one.solve(nums, preamble=25)}")
    print(f"Day 09 Part 2: {part_two.solve(nums, preamble=25)}")
