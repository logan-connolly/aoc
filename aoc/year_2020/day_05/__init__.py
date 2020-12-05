from ..resources import read_input
from . import part_one, part_two


def solution():
    tickets = read_input(day=5)
    print(f"Day 05 Part 1: {part_one.solve(tickets)}")
    print(f"Day 05 Part 2: {part_two.solve(tickets)}")
