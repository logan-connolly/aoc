from pathlib import Path
from typing import Optional, Sequence, Union

Lines = Sequence[Union[str, int]]

DATA_PATH = Path(__file__).parents[1] / "data"


def read_input(
    year: int, day: int, delim: Optional[str] = None, as_int: bool = False
) -> Lines:
    """Read in input data and transform appropriately"""

    path_to_data = DATA_PATH / str(year) / f"{day:02d}.txt"
    with path_to_data.open(mode="r") as f:
        data = f.read()

    lines = data.split(delim) if delim else data.splitlines()
    item_type = int if as_int else str
    return [item_type(line) for line in lines]
