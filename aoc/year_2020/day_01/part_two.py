from aoc.year_2020.day_01 import part_one


def solve(nums):
    """Day 1: Report Repair (part 2)"""
    first, rest = nums[0], nums[1:]
    new_target = 2020 - first
    match_found = part_one.solve(rest, target=new_target)
    if match_found:
        return first * match_found
    return solve(rest)
