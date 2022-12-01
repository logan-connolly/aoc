"""This is the Solution for Year 2020 Day 01"""

from typing import Optional

import aoc


def find_and_transform_match(lines: aoc.IntLines, target: int) -> Optional[int]:
    """Build up set and perform transform if found"""
    seen_nums = set()
    for num in lines:
        if num in seen_nums:
            return num * (target - num)
        seen_nums.add(target - num)
    return None


def recursive_finder(lines: aoc.IntLines) -> int:
    first, *rest = lines
    new_target = 2020 - first
    match_output = find_and_transform_match(rest, target=new_target)
    if match_output:
        return first * match_output
    return recursive_finder(rest)


@aoc.expect(514579)
def part_one(lines: aoc.IntLines) -> int:
    output = find_and_transform_match(lines, target=2020)
    return output if output else -1


@aoc.expect(241861950)
def part_two(lines: aoc.IntLines) -> int:
    return recursive_finder(lines)


def main():
    lines = aoc.read_int_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
