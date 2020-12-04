from math import ceil

from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_03.txt") as f:
        tmap = f.read().splitlines()
        n_copies = ceil(len(tmap) * round((len(tmap) / 4)))
        tmap_dup = [map_row * n_copies for map_row in tmap]
        print(f"Day 03 Part 1: {part_one.solve(tmap_dup, down=1, right=3)}")
        print(f"Day 03 Part 2: {part_two.solve(tmap_dup)}")
