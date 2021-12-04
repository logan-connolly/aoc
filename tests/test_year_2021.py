import pytest

from aoc.cli import get_solutions


@pytest.mark.parametrize(
    "year,day,expected_one,expected_two",
    [
        (2021, 1, 1374, 1418),
        (2021, 2, 1692075, 1749524700),
        (2021, 3, 4191876, 3414905),
        (2021, 4, 21607, 19012),
    ],
)
def test_solutions(year, day, expected_one, expected_two):
    answers = get_solutions(year, day)
    assert answers.part_one == expected_one
    assert answers.part_two == expected_two
