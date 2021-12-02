from typing import Optional


def compare(prev: Optional[int], curr: int) -> bool:
    if prev is not None:
        return curr > prev
    return False


def create_three_measurement_window(data: list[int]) -> list[int]:
    new_data = []
    for start_idx, _ in enumerate(data[:-2]):
        subset = data[start_idx : start_idx + 3]
        new_data.append(sum(subset))
    return new_data
