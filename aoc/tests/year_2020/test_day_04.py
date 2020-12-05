from aoc.year_2020.day_04 import part_one, part_two
from aoc.year_2020.resources import read_input

TEST_INPUT = read_input(day=4, splitter="\n\n")


def test_part_one():
    assert part_one.solve(TEST_INPUT) == 202


def test_part_two():
    assert part_two.solve(TEST_INPUT) == 137
