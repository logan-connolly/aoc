import pytest

from src.day_02 import part_one, part_two


@pytest.mark.parametrize(
    "passwd,expected",
    [("1-3 a: abcde", True), ("1-3 b: cdefg", False), ("2-9 c: ccccccccc", True)],
)
def test_part_one(passwd, expected):
    assert part_one(passwd) == expected


@pytest.mark.parametrize(
    "passwd,expected",
    [("1-3 a: abcde", True), ("1-3 b: cdefg", False), ("2-9 c: ccccccccc", False)],
)
def test_part_two(passwd, expected):
    assert part_two(passwd) == expected
