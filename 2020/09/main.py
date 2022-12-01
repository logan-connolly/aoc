"""This is the Solution for Year 2020 Day 09"""

from copy import deepcopy

import aoc

PREAMBLE = 5


def valid_preamble(subset: aoc.IntLines, target: int) -> bool:
    """Check if the sum of two numbers in subset equal target"""
    target_set = set()
    for num in subset:
        if num in target_set:
            return True
        target_set.add(target - num)
    return False


def check_preamble(lines: aoc.IntLines, preamble: int) -> int:
    """Recursively check preamble until solution found"""
    nums = deepcopy(lines)
    subset, target = nums[:preamble], nums[preamble]
    if valid_preamble(subset, target):
        return check_preamble(nums[1:], preamble)
    return target


def find_weakness(nums: aoc.IntLines, target: int) -> int:
    """Find a subset that matches target"""
    weakness = -1
    for idx, _ in enumerate(nums):
        for end_idx in range(idx, len(nums) - 1):
            subset = nums[idx:end_idx]
            if sum(subset) == target:
                weakness = min(subset) + max(subset)
                break
    return weakness


@aoc.expect(127)
def part_one(lines: aoc.IntLines) -> int:
    return check_preamble(lines, preamble=PREAMBLE)


@aoc.expect(62)
def part_two(lines: aoc.IntLines) -> int:
    target = check_preamble(lines, preamble=PREAMBLE)
    subset = lines[: lines.index(target)]
    return find_weakness(subset, target)


def main():
    lines = aoc.read_int_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
