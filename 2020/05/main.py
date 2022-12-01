"""This is the Solution for Year 2020 Day 05"""

import aoc


def get_seat_id(ticket: str) -> int:
    """Get seat id based on boarding ticket (ie. 'BBFFBBFRLL')"""

    rows = range(128)
    cols = range(8)

    for letter in ticket:
        if letter in "FB":
            midpoint = len(rows) // 2
            rows = rows[:midpoint] if letter == "F" else rows[midpoint:]
        else:
            midpoint = len(cols) // 2
            cols = cols[:midpoint] if letter == "L" else cols[midpoint:]

    return rows[0] * 8 + cols[0]


@aoc.expect(820)
def part_one(lines: aoc.StrLines) -> int:
    return max(get_seat_id(ticket) for ticket in lines)


@aoc.expect(120)
def part_two(lines: aoc.StrLines) -> int:
    seat_ids = [get_seat_id(ticket) for ticket in lines]
    available_seat_set = set(range(min(seat_ids), max(seat_ids) + 1))
    return (available_seat_set - set(seat_ids)).pop()


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
