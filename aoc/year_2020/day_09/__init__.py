from ..resources import read_input
from . import part_one, part_two


def solution():
    nums = read_input(day=9, as_int=True)
    print(f"Day 09 Part 1: {part_one.solve(nums, preamble=25)}")
    print(f"Day 09 Part 2: {part_two.solve(nums, preamble=25)}")
