from aoc.year_2020.day_09 import part_one
from aoc.year_2020.day_09.finder import find_weakness


def solve(nums: list[int], preamble: int) -> int:
    """Day 09: Encoding Error (part 2)"""
    target = part_one.solve(nums, preamble)
    subset = nums[: nums.index(target)]
    return find_weakness(subset, target)
