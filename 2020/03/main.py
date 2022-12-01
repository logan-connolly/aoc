"""This is the Solution for Year 2020 Day 03"""

from copy import deepcopy
from math import prod

import aoc


def count_trees(lines: aoc.StrLines, down: int, right: int) -> int:
    """Count trees for given down/right shift"""
    tmap = deepcopy(lines)
    row_index, tree_count = 0, 0
    for row in tmap[down::down]:
        row_index += right
        if row[row_index % len(row)] == "#":
            tree_count += 1
    return tree_count


@aoc.expect(7)
def part_one(lines: aoc.StrLines) -> int:
    down, right = 1, 3
    return count_trees(lines, down, right)


@aoc.expect(336)
def part_two(lines: aoc.StrLines) -> int:
    shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (count_trees(lines, down, right) for right, down in shifts)
    return prod(counts)


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
