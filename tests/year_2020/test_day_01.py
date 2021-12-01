from aoc.io import read_input
from aoc.year_2020.day_01 import part_one, part_two

NUMS = read_input(year=2020, day=1, as_int=True)


def test_part_one():
    assert part_one.solve(NUMS) == 494475


def test_part_two():
    assert part_two.solve(NUMS) == 267520550
