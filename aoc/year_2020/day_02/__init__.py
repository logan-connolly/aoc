from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_02.txt") as f:
        passwds = f.read().splitlines()
        print(f"Day 02 Part 1: {part_one.solve(passwds)}")
        print(f"Day 02 Part 2: {part_two.solve(passwds)}")
