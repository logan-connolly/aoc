import pytest

from aoc.app import get_solutions, parse_args

DAY = "3"
YEAR = "2020"
BAD_DAY = "33"
BAD_YEAR = "1999"


def test_parse_args():
    input_args = [YEAR, DAY]
    args = parse_args(input_args)
    assert args.year == YEAR
    assert args.day == DAY


@pytest.mark.parametrize("good_args", [[YEAR], [YEAR, DAY]])
def test_get_solutions_found(good_args):
    args = parse_args(good_args)
    get_solutions(args)


@pytest.mark.parametrize("bad_args", [[BAD_YEAR, DAY], [YEAR, BAD_DAY]])
def test_get_solutions_not_found(bad_args):
    args = parse_args(bad_args)
    get_solutions(args)
