from aoc.year_2021.day_01.util import compare, create_three_measurement_window


def solve(data):
    """Year 2021 Day 1 Part 2"""
    window_data = create_three_measurement_window(data)
    lagged = [None, *window_data[:-1]]
    return sum(compare(prev, curr) for prev, curr in zip(lagged, window_data))
