import re

from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_04.txt") as f:
        passport_input = f.read()
        print(f"Day 04 Part 1: {part_one.solve(passport_input)}")
        print(f"Day 04 Part 2: {part_two.solve(passport_input)}")
