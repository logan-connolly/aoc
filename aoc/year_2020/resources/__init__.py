from pathlib import Path
from typing import Optional, Sequence, Union

Lines = Sequence[Union[str, int]]


def read_input(day: int, delim: Optional[str] = None, as_int: bool = False) -> Lines:
    """Read in input data and transform appropriately"""

    with open(Path(__file__).parent / f"day_{day:02d}.txt") as f:
        data = f.read()

    lines = data.split(delim) if delim else data.splitlines()
    item_type = int if as_int else str
    return [item_type(line) for line in lines]
