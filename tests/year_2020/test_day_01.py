from aoc.year_2020.day_01 import part_one, part_two
from aoc.year_2020.resources import read_input

NUMS = read_input(day=1, as_int=True)


def test_part_one():
    assert part_one.solve(NUMS) == 494475


def test_part_two():
    assert part_two.solve(NUMS) == 267520550
