from pathlib import Path
from typing import Optional, Sequence, Union

Lines = Sequence[Union[str, int]]


def get_project_root() -> Path:
    """Get path to the root of the project"""
    return Path(__file__).parents[1]


def get_path_to_input_data(year: int, day: int) -> Path:
    """Get path to static data used as input for problem of the day"""
    return get_project_root() / "data" / str(year) / f"{day:02d}.txt"


def get_path_to_module(year: int, day: int) -> Path:
    """Get path to static data used as input for problem of the day"""
    return get_project_root() / "aoc" / f"year_{year}" / f"day_{day:02d}"


def read_input(
    year: int, day: int, delim: Optional[str] = None, as_int: bool = False
) -> Lines:
    """Read in input data and transform appropriately"""
    path_to_data = get_path_to_input_data(year, day)
    with path_to_data.open(mode="r") as f:
        data = f.read()

    lines = data.split(delim) if delim else data.splitlines()
    item_type = int if as_int else str
    return [item_type(line) for line in lines]


def generate_files(year: int, day: int, fname: str, content: str) -> None:
    """Generate file structure for a new problem in source code"""
    path_to_data = get_path_to_input_data(year, day)
    path_to_module = get_path_to_module(year, day)

    path_to_data.parent.mkdir(parents=True, exist_ok=True)
    path_to_module.mkdir(parents=True, exist_ok=True)

    init_file = path_to_module / "__init__.py"
    submodule = path_to_module / fname
    if not submodule.exists():
        path_to_data.touch()
        init_file.touch()
        submodule.touch()
        submodule.write_text(content)
