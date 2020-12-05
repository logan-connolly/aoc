def get_seat_id(ticket):
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
