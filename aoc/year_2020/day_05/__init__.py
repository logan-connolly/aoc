from ..resources import RESOURCE_FOLDER
from . import part_one, part_two


def solution():
    with open(RESOURCE_FOLDER / "day_05.txt") as f:
        tickets = f.read().splitlines()
        print(f"Day 05 Part 1: {part_one.solve(tickets)}")
        print(f"Day 05 Part 2: {part_two.solve(tickets)}")
