from aoc.year_2020.day_05.finder import get_seat_id


def solve(tickets):
    """Day 05: Binary Boarding (part 1)"""
    return max(get_seat_id(ticket) for ticket in tickets)
