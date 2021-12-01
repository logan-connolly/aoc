from aoc.io import read_input
from aoc.year_2020.day_08 import part_one, part_two

LUGGAGE = read_input(year=2020, day=8)


def test_part_one():
    assert part_one.solve(LUGGAGE) == 1528


def test_part_two():
    assert part_two.solve(LUGGAGE) == 640
