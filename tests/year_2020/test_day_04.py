from aoc.io import read_input
from aoc.year_2020.day_04 import part_one, part_two

TEST_INPUT = read_input(year=2020, day=4, delim="\n\n")


def test_part_one():
    assert part_one.solve(TEST_INPUT) == 202


def test_part_two():
    assert part_two.solve(TEST_INPUT) == 137
