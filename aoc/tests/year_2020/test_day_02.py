from aoc.year_2020.day_02 import part_one, part_two

PASSWDS = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_part_one():
    assert part_one.solve(PASSWDS) == 2


def test_part_two():
    assert part_two.solve(PASSWDS) == 1
