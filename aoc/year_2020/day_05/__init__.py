from aoc.io import read_input
from aoc.year_2020.day_05 import part_one, part_two


def solution():
    tickets = read_input(year=2020, day=5)
    print(f"Day 05 Part 1: {part_one.solve(tickets)}")
    print(f"Day 05 Part 2: {part_two.solve(tickets)}")
