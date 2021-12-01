from math import ceil

from aoc.year_2020.day_03 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    tmap = read_input(day=3)
    print(f"Day 03 Part 1: {part_one.solve(tmap, down=1, right=3)}")
    print(f"Day 03 Part 2: {part_two.solve(tmap)}")
