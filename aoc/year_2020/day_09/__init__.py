from aoc.year_2020.day_09 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    nums = read_input(day=9, as_int=True)
    print(f"Day 09 Part 1: {part_one.solve(nums, preamble=25)}")
    print(f"Day 09 Part 2: {part_two.solve(nums, preamble=25)}")
