from typing import List

from . import part_one
from .finder import find_weakness


def solve(nums: List[int], preamble: int) -> int:
    """Day 09: Encoding Error (part 2)"""
    target = part_one.solve(nums, preamble)
    subset = nums[: nums.index(target)]
    return find_weakness(subset, target)
