"""This is the Solution for Year 2022 Day 04"""


import aoc


def to_range_set(raw_range: str) -> set[int]:
    min_str, max_str = raw_range.split("-")
    return {n for n in range(int(min_str), int(max_str) + 1)}


def completely_overlaps(s1: set[int], s2: set[int]) -> bool:
    shorter, longer = (s2, s1) if len(s1) > len(s2) else (s1, s2)
    return shorter & longer == shorter


def overlaps_at_all(s1: set[int], s2: set[int]) -> bool:
    return (len(s1) + len(s2)) != len(s1 | s2)


@aoc.expect(2)
def part_one(lines: aoc.StrLines) -> int:
    splits = (line.split(",") for line in lines)
    sets = ((to_range_set(l), to_range_set(r)) for l, r in splits)
    return sum(completely_overlaps(s1, s2) for s1, s2 in sets)


@aoc.expect(4)
def part_two(lines: aoc.StrLines) -> int:
    splits = (line.split(",") for line in lines)
    sets = ((to_range_set(l), to_range_set(r)) for l, r in splits)
    return sum(overlaps_at_all(s1, s2) for s1, s2 in sets)


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
