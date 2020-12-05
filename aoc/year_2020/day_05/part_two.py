from .finder import get_seat_id


def solve(tickets):
    """Day 05: Binary Boarding (part 2)"""
    seat_ids = [get_seat_id(ticket) for ticket in tickets]
    available_seat_set = set(range(min(seat_ids), max(seat_ids) + 1))
    return (available_seat_set - set(seat_ids)).pop()
