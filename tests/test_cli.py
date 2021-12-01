import pytest

from aoc import cli

DAY = "3"
YEAR = "2020"
BAD_DAY = "33"
BAD_YEAR = "1999"


def test_parse_args():
    args = cli.parse_args([YEAR, DAY])
    assert args.year == int(YEAR)
    assert args.day == int(DAY)


def test_get_solutions_found():
    args = cli.parse_args([YEAR, DAY])
    cli.get_solutions(args)


@pytest.mark.parametrize("bad_args", [[BAD_YEAR, DAY], [YEAR, BAD_DAY]])
def test_get_solutions_not_found(bad_args):
    with pytest.raises(ValueError):
        args = cli.parse_args(bad_args)
        cli.get_solutions(args)


def test_solutions_can_be_displayed():
    args = cli.parse_args([YEAR, DAY])
    solutions = cli.get_solutions(args)
    cli.display_solutions(solutions, args)
