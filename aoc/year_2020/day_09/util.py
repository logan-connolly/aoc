from copy import deepcopy


def valid_preamble(subset: list[int], target: int) -> bool:
    """Check if the sum of two numbers in subset equal target"""
    target_set = set()
    for num in subset:
        if num in target_set:
            return True
        target_set.add(target - num)
    return False


def recursive_check(data, preamble: int):
    """Recursively check preamble until solution found"""
    nums = deepcopy(data)
    subset, target = nums[:preamble], nums[preamble]
    if valid_preamble(subset, target):
        return recursive_check(nums[1:], preamble)
    return target


def find_weakness(nums: list[int], target: int) -> int:
    """Find a subset that matches target"""
    answer = -1
    for idx, _ in enumerate(nums):
        for end_idx in range(idx, len(nums) - 1):
            subset = nums[idx:end_idx]
            if sum(subset) == target:
                answer = min(subset) + max(subset)
                break
    return answer
