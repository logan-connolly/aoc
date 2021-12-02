import pytest

from aoc.cli import get_solutions


@pytest.mark.parametrize(
    "year,day,expected_one,expected_two",
    [
        (2020, 1, 494475, 267520550),
        (2020, 2, 660, 530),
        (2020, 3, 257, 1744787392),
        (2020, 4, 202, 137),
        (2020, 5, 987, 603),
        (2020, 6, 6680, 3117),
        (2020, 8, 1528, 640),
        (2020, 9, 248131121, 31580383),
    ],
)
def test_solutions(year, day, expected_one, expected_two):
    answers = get_solutions(year, day)
    assert answers.part_one == expected_one
    assert answers.part_two == expected_two
