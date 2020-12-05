from ..resources import read_input
from . import part_one, part_two


def solution():
    passwds = read_input(day=2)
    print(f"Day 02 Part 1: {part_one.solve(passwds)}")
    print(f"Day 02 Part 2: {part_two.solve(passwds)}")
