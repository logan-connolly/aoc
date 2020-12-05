from math import ceil

from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_03.txt") as f:
        tmap = f.read().splitlines()
        print(f"Day 03 Part 1: {part_one.solve(tmap, down=1, right=3)}")
        print(f"Day 03 Part 2: {part_two.solve(tmap)}")
