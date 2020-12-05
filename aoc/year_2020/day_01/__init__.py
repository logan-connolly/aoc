from ..resources import read_input
from . import part_one, part_two


def solution():
    nums = read_input(day=1, as_int=True)
    print(f"Day 01 Part 1: {part_one.solve(nums)}")
    print(f"Day 01 Part 2: {part_two.solve(nums)}")
