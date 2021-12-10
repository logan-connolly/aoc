"""This is the Solution for Year 2021 Day 09"""

from collections import defaultdict
from aoc.abstracts.solver import Answers, StrLines

Coord = tuple[int, int]
CoordMap = dict[Coord, int]


def create_coord_map(lines: StrLines) -> CoordMap:
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


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        coord_map = create_coord_map(lines)
        low_points = find_low_points(coord_map)
        return sum(value + 1 for value in low_points)

    def _solve_part_two(self, lines: StrLines) -> int:
        return len(lines)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
