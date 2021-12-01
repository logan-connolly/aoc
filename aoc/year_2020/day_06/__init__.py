from ..resources import read_input
from . import part_one, part_two


def solution():
    answers = read_input(day=6, delim="\n\n")
    print(f"Day 06 Part 1: {part_one.solve(answers)}")
    print(f"Day 06 Part 2: {part_two.solve(answers)}")
