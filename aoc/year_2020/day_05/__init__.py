from aoc.year_2020.day_05 import part_one, part_two
from aoc.year_2020.resources import read_input


def solution():
    tickets = read_input(day=5)
    print(f"Day 05 Part 1: {part_one.solve(tickets)}")
    print(f"Day 05 Part 2: {part_two.solve(tickets)}")
