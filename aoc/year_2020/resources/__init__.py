from pathlib import Path
from typing import List


def read_input(day: int, splitter: str = None, as_int: bool = False) -> List[str]:
    """Read in input data"""
    with open(Path(__file__).parent / f"day_{day:02d}.txt") as f:
        lines = f.read().split(splitter) if splitter else f.read().splitlines()
        return [int(line) for line in lines] if as_int else lines
