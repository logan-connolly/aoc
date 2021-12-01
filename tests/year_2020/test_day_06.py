from aoc.io import read_input
from aoc.year_2020.day_06 import part_one, part_two

ANSWERS = read_input(year=2020, day=6, delim="\n\n")


def test_part_one():
    assert part_one.solve(ANSWERS) == 6680


def test_part_two():
    assert part_two.solve(ANSWERS) == 3117
