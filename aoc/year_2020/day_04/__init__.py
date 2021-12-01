import re

from aoc.io import read_input
from aoc.year_2020.day_04 import part_one, part_two


def solution():
    passports = read_input(year=2020, day=4, delim="\n\n")
    print(f"Day 04 Part 1: {part_one.solve(passports)}")
    print(f"Day 04 Part 2: {part_two.solve(passports)}")
