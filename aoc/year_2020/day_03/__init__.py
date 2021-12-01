from math import ceil

from aoc.io import read_input
from aoc.year_2020.day_03 import part_one, part_two


def solution():
    tmap = read_input(year=2020, day=3)
    print(f"Day 03 Part 1: {part_one.solve(tmap, down=1, right=3)}")
    print(f"Day 03 Part 2: {part_two.solve(tmap)}")
