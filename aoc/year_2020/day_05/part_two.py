from .finder import get_seat_id


def solve(tickets):
    seat_ids = [get_seat_id(ticket) for ticket in tickets]
    min_seat, max_seat = min(seat_ids), max(seat_ids)
    return (set(range(min_seat, max_seat + 1)) - set(seat_ids)).pop()
