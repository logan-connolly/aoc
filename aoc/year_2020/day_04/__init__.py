import re

from ..resources import read_input
from . import part_one, part_two


def solution():
    passports = read_input(day=4, delim="\n\n")
    print(f"Day 04 Part 1: {part_one.solve(passports)}")
    print(f"Day 04 Part 2: {part_two.solve(passports)}")
