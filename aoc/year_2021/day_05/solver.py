"""This is the Solution for Year 2021 Day 05"""

import itertools
from collections import Counter
from dataclasses import dataclass

from aoc.abstracts.solver import Answers, StrLines


@dataclass(frozen=True)
class Point:
    """Immutable point that will define x and y on 2D plane"""

    x: int
    y: int


@dataclass
class LineSegment:
    """Define a line object that takes a start and end point"""

    start: Point
    end: Point

    @property
    def slope(self) -> int:
        return int((self.start.y - self.end.y) / (self.start.x - self.end.x))

    @property
    def intercept(self) -> int:
        return int(self.start.y - (self.start.x * self.slope))

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def y_range(self) -> range:
        coords = self.start.y, self.end.y
        return range(min(coords), max(coords) + 1)

    def x_range(self) -> range:
        coords = self.start.x, self.end.x
        return range(min(coords), max(coords) + 1)

    def calculate_y(self, x: int) -> int:
        return int(self.slope * x + self.intercept)


def parse_point(raw_point: str) -> Point:
    """Parse point from raw string"""
    x, y = raw_point.split(",")
    return Point(x=int(x), y=int(y))


def parse_lines(lines: StrLines) -> list[LineSegment]:
    """Parse raw lines into Lines and Points"""
    parsed_lines = []
    for raw_line in lines:
        raw_start, raw_end = raw_line.split(" -> ")
        start_point = parse_point(raw_start)
        end_point = parse_point(raw_end)
        line = LineSegment(start=start_point, end=end_point)
        parsed_lines.append(line)
    return parsed_lines


def get_horizontal_vertical_lines(lines: list[LineSegment]) -> list[LineSegment]:
    """Filter for only horizontal or vertical lines"""
    return [line for line in lines if line.is_horizontal() or line.is_vertical()]


def get_point_segment(line: LineSegment) -> list[Point]:
    """Get a list of points in a given line"""
    if line.is_vertical():
        return [Point(x=line.start.x, y=y) for y in line.y_range()]
    return [Point(x=x, y=line.calculate_y(x)) for x in line.x_range()]


def get_point_occurences(lines: list[LineSegment]) -> dict[Point, int]:
    """Count up the number of occurences for a given point"""
    segment_points = (get_point_segment(line) for line in lines)
    return Counter(itertools.chain.from_iterable(segment_points))


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        parsed_lines = parse_lines(lines)
        filtered_lines = get_horizontal_vertical_lines(parsed_lines)
        point_count = get_point_occurences(filtered_lines)
        return sum(1 for n_occurences in point_count.values() if n_occurences >= 2)

    def _solve_part_two(self, lines: StrLines) -> int:
        parsed_lines = parse_lines(lines)
        point_count = get_point_occurences(parsed_lines)
        return sum(1 for n_occurences in point_count.values() if n_occurences >= 2)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
