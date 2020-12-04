def solve(nums, target=2020):
    """Day 1: Report Repair (part 1)"""
    target_set = set()
    for num in nums:
        if num in target_set:
            return num * (target - num)
        target_set.add(target - num)
    return None
