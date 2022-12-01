"""This is the Solution for Year 2021 Day 07"""

from functools import lru_cache

import aoc


@lru_cache
def get_crab_engineering_value(fuel_needed: int) -> int:
    """Use formula n(n+1)/2 to find sum of continous set of integers"""
    return int(fuel_needed * (fuel_needed + 1) / 2)


def evaluate_fuel_needed(crabs: aoc.IntLines, value: int, advanced: bool) -> int:
    """Evaluate fuel needed to move crabs to a given horizontal position value"""
    if not advanced:
        return sum(abs(num - value) for num in crabs)
    return sum(get_crab_engineering_value(abs(num - value)) for num in crabs)


@aoc.expect(37)
def part_one(lines: aoc.IntLines) -> int:
    n_range = range(min(lines), max(lines) + 1)
    return min(evaluate_fuel_needed(lines, n, advanced=False) for n in n_range)


@aoc.expect(168)
def part_two(lines: aoc.IntLines) -> int:
    n_range = range(min(lines), max(lines) + 1)
    return min(evaluate_fuel_needed(lines, n, advanced=True) for n in n_range)


def main():
    lines = sorted([int(n) for n in aoc.read(__file__).split(",")])
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
