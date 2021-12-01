import re

from aoc.year_2020.day_04 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    passports = read_input(day=4, delim="\n\n")
    print(f"Day 04 Part 1: {part_one.solve(passports)}")
    print(f"Day 04 Part 2: {part_two.solve(passports)}")
