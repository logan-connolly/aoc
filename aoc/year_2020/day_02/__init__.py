from aoc.io import read_input
from aoc.year_2020.day_02 import part_one, part_two


def solution():
    passwds = read_input(year=2020, day=2)
    print(f"Day 02 Part 1: {part_one.solve(passwds)}")
    print(f"Day 02 Part 2: {part_two.solve(passwds)}")
