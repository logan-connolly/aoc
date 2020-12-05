from math import ceil

from ..resources import read_input
from . import part_one, part_two


def solution():
    tmap = read_input(day=3)
    print(f"Day 03 Part 1: {part_one.solve(tmap, down=1, right=3)}")
    print(f"Day 03 Part 2: {part_two.solve(tmap)}")
