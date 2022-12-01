"""This is the Solution for Year 2021 Day 01"""

from typing import Optional

import aoc


def compare(prev: Optional[int], curr: int) -> bool:
    if prev is not None:
        return curr > prev
    return False


def create_three_measurement_window(data: aoc.IntLines) -> aoc.IntLines:
    new_data = []
    for start_idx, _ in enumerate(data[:-2]):
        subset = data[start_idx : start_idx + 3]
        new_data.append(sum(subset))
    return new_data


@aoc.expect(7)
def part_one(lines: aoc.IntLines) -> int:
    lagged = [None, *lines[:-1]]
    return sum(compare(prev, curr) for prev, curr in zip(lagged, lines))


@aoc.expect(5)
def part_two(lines: aoc.IntLines) -> int:
    window_data = create_three_measurement_window(lines)
    lagged = [None, *window_data[:-1]]
    return sum(compare(prev, curr) for prev, curr in zip(lagged, window_data))


def main():
    lines = aoc.read_int_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
