import importlib

import pytest

from aoc import runner
from aoc.db import data


@pytest.mark.parametrize(
    "year,day,expected_one,expected_two",
    [
        (2021, 1, 1374, 1418),
    ],
)
def test_day(year, day, expected_one, expected_two):
    """Dynamically load part one and two modules for a given day and year"""
    problem_data = data[(year, day)]
    base_module_path = f"aoc.year_{year}.day_{day:02}"
    part_one = importlib.import_module(f"{base_module_path}.part_one")
    part_two = importlib.import_module(f"{base_module_path}.part_two")

    result_one, result_two = runner.run(problem_data, part_one, part_two)

    assert result_one == expected_one
    assert result_two == expected_two
