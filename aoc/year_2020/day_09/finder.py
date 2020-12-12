from typing import List


def find_weakness(nums: List[int], target: int) -> int:
    """Find a subset that matches target"""
    for idx, _ in enumerate(nums):
        for end_idx in range(idx, len(nums) - 1):
            subset = nums[idx:end_idx]
            if sum(subset) == target:
                return min(subset) + max(subset)
    return -1
