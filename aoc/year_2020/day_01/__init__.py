from aoc.year_2020.day_01 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    nums = read_input(day=1, as_int=True)
    print(f"Day 01 Part 1: {part_one.solve(nums)}")
    print(f"Day 01 Part 2: {part_two.solve(nums)}")
