from aoc.io import read_input
from aoc.year_2020.day_02 import part_one, part_two

PASSWDS = read_input(year=2020, day=2)


def test_part_one():
    assert part_one.solve(PASSWDS) == 660


def test_part_two():
    assert part_two.solve(PASSWDS) == 530
