from aoc.io import read_input
from aoc.year_2020.day_05 import part_one, part_two

TICKETS = read_input(year=2020, day=5)


def test_part_one():
    assert part_one.solve(TICKETS) == 987


def test_part_two():
    assert part_two.solve(TICKETS) == 603
