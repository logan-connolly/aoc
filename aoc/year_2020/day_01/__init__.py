from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_01.txt") as f:
        nums = [int(n) for n in f.read().splitlines()]
        print(f"Day 01 Part 1: {part_one.solve(nums)}")
        print(f"Day 01 Part 2: {part_two.solve(nums)}")
