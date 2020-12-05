from .finder import get_seat_id


def solve(tickets):
    return max(get_seat_id(ticket) for ticket in tickets)
