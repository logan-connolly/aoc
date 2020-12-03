from src.day_01 import part_one, part_two


def test_part_one():
    lst = [1721, 979, 366, 299, 675, 1456]
    assert part_one(lst) == 514579


def test_solution():
    lst = [1721, 979, 366, 299, 675, 1456]
    assert part_two(lst) == 241861950
