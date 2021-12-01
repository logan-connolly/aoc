from aoc.io import read_input
from aoc.year_2020.day_08 import part_one, part_two


def solution():
    answers = read_input(year=2020, day=8)
    print(f"Day 08 Part 1: {part_one.solve(answers)}")
    print(f"Day 08 Part 2: {part_two.solve(answers)}")
