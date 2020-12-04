from aoc.year_2020.day_01 import part_one, part_two


def test_part_one():
    lst = [1721, 979, 366, 299, 675, 1456]
    assert part_one.solve(lst) == 514579


def test_part_two():
    lst = [1721, 979, 366, 299, 675, 1456]
    assert part_two.solve(lst) == 241861950
