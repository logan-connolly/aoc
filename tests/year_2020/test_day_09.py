import pytest

from aoc.io import read_input
from aoc.year_2020.day_09 import part_one, part_two

NUMS = read_input(year=2020, day=9, as_int=True)


def test_part_one():
    assert part_one.solve(NUMS, preamble=25) == 248131121


def test_part_two():
    assert part_two.solve(NUMS, preamble=25) == 31580383


def test_raises_error_when_answer_not_found():
    with pytest.raises(ValueError):
        part_two.solve([1, 2, 3, 4, 5, 6, 7], preamble=2)
