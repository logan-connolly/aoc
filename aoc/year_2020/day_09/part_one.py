from typing import List

from .validate import valid_preamble


def solve(nums: List[int], preamble: int) -> int:
    """Day 09: Encoding Error (part 1)"""
    subset, target = nums[:preamble], nums[preamble]
    if valid_preamble(subset, target):
        return solve(nums[1:], preamble)
    return target
