import pytest

from aoc import cli


def test_parse_args(year, day):
    args = cli.parse_args([str(year), str(day)])
    assert args.year == year
    assert args.day == day


def test_get_solutions_found(year, day):
    cli.get_solutions(year, day)


def test_get_solutions_not_found():
    with pytest.raises(ValueError):
        cli.get_solutions(1900, 1)


def test_solutions_can_be_displayed(year, day):
    solutions = cli.get_solutions(year, day)
    cli.display_result(solutions, year, day)


@pytest.mark.usefixtures("mock_project_root")
def test_create_new_entry(year, day):
    module_path = cli.create_new_day_entry(year, day)
    assert module_path.exists()
