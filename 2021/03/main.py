"""This is the Solution for Year 2021 Day 03"""

from collections import defaultdict

import aoc

Mapping = dict[int, int]


def build_index_map(lines: aoc.StrLines) -> Mapping:
    """Build up mapping for index and value (0 => -1, 1 => 1)"""
    mapping: Mapping = defaultdict(int)
    for str_byte in lines:
        for idx, bit in enumerate(str_byte):
            shift_val = -1 if bit == "0" else 1
            mapping[idx] += shift_val
    return mapping


def convert_to_int(str_byte: str) -> int:
    """Take string representation of byte and convert to int"""
    return int(str_byte, 2)


def get_gamma_rate(mapping: Mapping) -> int:
    """Convert mapping to byte and then return int representation of gamma"""
    str_byte = "".join("1" if v > 0 else "0" for v in mapping.values())
    return convert_to_int(str_byte)


def get_epsilon_rate(mapping: Mapping) -> int:
    """Convert mapping to byte and then return int representation of epsilon"""
    str_byte = "".join("1" if v < 0 else "0" for v in mapping.values())
    return convert_to_int(str_byte)


def get_char_to_filter_by(shift_val: int, is_o2: bool = False) -> str:
    """Find out what character we should filter the lines with based on shift_val"""
    if is_o2:
        return "1" if shift_val >= 0 else "0"
    return "0" if shift_val >= 0 else "1"


def filter_lines_by_char(
    lines: aoc.StrLines, target_char: str, idx: int
) -> aoc.StrLines:
    """Filter out the lines based on whether the index matches target character"""
    return [line for line in lines if line[idx] == target_char]


def get_rating(lines: aoc.StrLines, idx: int = 0, is_o2: bool = False) -> int:
    """Filter out lines that do not meet conditions and return remaining value"""

    if len(lines) == 1:
        str_byte = lines[0]
        return convert_to_int(str_byte)

    current_map = build_index_map(lines)
    target_char = get_char_to_filter_by(shift_val=current_map[idx], is_o2=is_o2)
    filtered_lines = filter_lines_by_char(lines, target_char, idx)
    return get_rating(filtered_lines, idx + 1, is_o2)


@aoc.expect(198)
def part_one(lines: aoc.StrLines) -> int:
    mapping = build_index_map(lines)
    gamma = get_gamma_rate(mapping)
    epsilon = get_epsilon_rate(mapping)
    return gamma * epsilon


@aoc.expect(230)
def part_two(lines: aoc.StrLines) -> int:
    rating_o2 = get_rating(lines, is_o2=True)
    rating_co2 = get_rating(lines, is_o2=False)
    return rating_o2 * rating_co2


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
