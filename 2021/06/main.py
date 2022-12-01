"""This is the Solution for Year 2021 Day 06"""

from functools import lru_cache

import aoc


@lru_cache
def count_offspring(cycle: int, days: int) -> int:
    """Counts how many offspring will be spawn over a given period"""
    if cycle >= days:
        return 1
    if cycle == 0:
        return count_offspring(8, days - 1) + count_offspring(6, days - 1)
    return count_offspring(cycle - 1, days - 1)


@aoc.expect(5934)
def part_one(lines: aoc.IntLines) -> int:
    return sum(count_offspring(n, 80) for n in lines)


@aoc.expect(26984457539)
def part_two(lines: aoc.IntLines) -> int:
    return sum(count_offspring(n, 256) for n in lines)


def main():
    lines = [int(n) for n in aoc.read(__file__).split(",")]
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
