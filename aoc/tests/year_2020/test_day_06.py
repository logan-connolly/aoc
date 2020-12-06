from aoc.year_2020.day_06 import part_one, part_two
from aoc.year_2020.resources import read_input

ANSWERS = read_input(day=6, splitter="\n\n")


def test_part_one():
    assert part_one.solve(ANSWERS) == 6680


def test_part_two():
    assert part_two.solve(ANSWERS) == 3117
