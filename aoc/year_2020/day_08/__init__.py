from aoc.year_2020.day_08 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    answers = read_input(day=8)
    print(f"Day 08 Part 1: {part_one.solve(answers)}")
    print(f"Day 08 Part 2: {part_two.solve(answers)}")
