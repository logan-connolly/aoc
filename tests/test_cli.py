import pytest

from aoc import cli

DAY = 3
YEAR = 2020
BAD_DAY = 33
BAD_YEAR = 1999


def test_parse_args():
    args = cli.parse_args([str(YEAR), str(DAY)])
    assert args.year == YEAR
    assert args.day == DAY


def test_get_solutions_found():
    cli.get_solutions(YEAR, DAY)


@pytest.mark.parametrize("year,day", [(BAD_YEAR, DAY), (YEAR, BAD_DAY)])
def test_get_solutions_not_found(year, day):
    with pytest.raises(ValueError):
        cli.get_solutions(year, day)


def test_solutions_can_be_displayed():
    solutions = cli.get_solutions(YEAR, DAY)
    cli.display_result(solutions, YEAR, DAY)
