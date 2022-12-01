"""This is the Solution for Year 2021 Day 09"""

from collections import defaultdict

import aoc

Coord = tuple[int, int]
CoordMap = dict[Coord, int]


def create_coord_map(lines: aoc.StrLines) -> CoordMap:
    """Loop over rows and columns and build up mapping"""
    mapping = defaultdict(int)
    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            mapping[(row_idx, col_idx)] = int(col)
    return mapping


def get_adjacent_coords(coord: Coord, coord_map: CoordMap) -> list[Coord]:
    """Get adjacent coords that exist in map"""
    x, y = coord
    adjacents = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    return [adjacent for adjacent in adjacents if adjacent in coord_map]


def find_low_points(coord_map: CoordMap) -> list[int]:
    """For each coord point compare adjacent points and add to set if lowest"""
    low_point_values = []
    for coord, value in coord_map.items():
        adjacents = get_adjacent_coords(coord, coord_map)
        lowest = all(value < coord_map[adjacent] for adjacent in adjacents)
        if lowest:
            low_point_values.append(value)
    return low_point_values


@aoc.expect(15)
def part_one(lines: aoc.StrLines) -> int:
    coord_map = create_coord_map(lines)
    low_points = find_low_points(coord_map)
    return sum(value + 1 for value in low_points)


@aoc.expect(1134)
def part_two(lines: aoc.StrLines) -> int:
    return len(lines)  # unsolved


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
