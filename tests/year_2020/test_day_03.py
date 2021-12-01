from aoc.year_2020.day_03 import part_one, part_two
from aoc.year_2020.resources import read_input

TMAP = read_input(day=3)


def test_part_one():
    assert part_one.solve(TMAP, down=1, right=3) == 257


def test_part_two():
    tmap = [map_row * 2 for map_row in TMAP]
    assert part_two.solve(tmap) == 1744787392
