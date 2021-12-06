"""This is the Solution for Year 2021 Day 05"""

from collections import defaultdict
from dataclasses import dataclass

from aoc.abstracts.solver import Answers, StrLines


@dataclass(frozen=True)
class Point:
    """Immutable point that will define x and y on 2D plane"""

    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class Line:
    """Define a line object that takes a start and end point"""

    start: Point
    end: Point

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end}"

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def slope(self) -> int:
        try:
            return int((self.start.y - self.end.y) / (self.start.x - self.end.x))
        except ZeroDivisionError:
            return 0

    @property
    def intercept(self) -> int:
        return int(self.start.y - (self.start.x * self.slope))

    def get_y(self, x_val: int) -> int:
        return int(self.slope * x_val + self.intercept)


def parse_point(raw_point: str) -> Point:
    """Parse point from raw string"""
    x, y = raw_point.split(",")
    return Point(x=int(x), y=int(y))


def parse_lines(lines: StrLines) -> list[Line]:
    """Parse raw lines into Lines and Points"""
    parsed_lines = []
    for raw_line in lines:
        raw_start, raw_end = raw_line.split(" -> ")
        start_point = parse_point(raw_start)
        end_point = parse_point(raw_end)
        line = Line(start=start_point, end=end_point)
        parsed_lines.append(line)
    return parsed_lines


def get_horizontal_vertical_lines(lines: list[Line]) -> list[Line]:
    """Filter for only horizontal or vertical lines"""
    return [line for line in lines if line.is_horizontal() or line.is_vertical()]


def get_points(line: Line) -> list[Point]:
    """Get a list of points in a given line"""
    if line.is_vertical():
        if line.start.y < line.end.y:
            range_val = range(line.start.y, line.end.y + 1)
        else:
            range_val = range(line.end.y, line.start.y + 1)
        return [Point(x=line.start.x, y=n) for n in range_val]

    if line.start.x < line.end.x:
        range_val = range(line.start.x, line.end.x + 1)
    else:
        range_val = range(line.end.x, line.start.x + 1)
    return [Point(x=n, y=line.get_y(n)) for n in range_val]


def count_points(lines: list[Line]) -> dict[Point, int]:
    """Count up the number of occurences for a given point"""
    counter: dict[Point, int] = defaultdict(int)
    for line in lines:
        points = get_points(line)
        for point in points:
            counter[point] += 1
    return counter


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        parsed_lines = parse_lines(lines)
        filtered_lines = get_horizontal_vertical_lines(parsed_lines)
        point_count = count_points(filtered_lines)
        return sum(1 for n_occurences in point_count.values() if n_occurences >= 2)

    def _solve_part_two(self, lines: StrLines) -> int:
        parsed_lines = parse_lines(lines)
        point_count = count_points(parsed_lines)
        return sum(1 for n_occurences in point_count.values() if n_occurences >= 2)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
