from aoc.year_2020.day_09 import part_one, part_two
from aoc.year_2020.resources import read_input

NUMS = read_input(day=9, as_int=True)


def test_part_one():
    assert part_one.solve(NUMS, preamble=25) == 248131121


def test_part_two():
    assert part_two.solve(NUMS, preamble=25) == 31580383
