from aoc.io import read_input
from aoc.year_2020.day_06 import part_one, part_two


def solution():
    answers = read_input(year=2020, day=6, delim="\n\n")
    print(f"Day 06 Part 1: {part_one.solve(answers)}")
    print(f"Day 06 Part 2: {part_two.solve(answers)}")
