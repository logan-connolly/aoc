from aoc.io import read_input
from aoc.year_2020.day_03 import part_one, part_two

TMAP = read_input(year=2020, day=3)


def test_part_one():
    assert part_one.solve(TMAP, down=1, right=3) == 257


def test_part_two():
    tmap = [map_row * 2 for map_row in TMAP]
    assert part_two.solve(tmap) == 1744787392
