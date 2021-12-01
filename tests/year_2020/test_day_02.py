from aoc.year_2020.day_02 import part_one, part_two
from aoc.year_2020.resources import read_input

PASSWDS = read_input(day=2)


def test_part_one():
    assert part_one.solve(PASSWDS) == 660


def test_part_two():
    assert part_two.solve(PASSWDS) == 530
