import importlib
from pathlib import Path
from typing import cast

from jinja2 import Environment, PackageLoader, select_autoescape

from aoc.abstracts.solver import SolverModule

templates = Environment(loader=PackageLoader("aoc"), autoescape=select_autoescape())


def get_project_root() -> Path:
    """Get path to the root of the project"""
    return Path(__file__).parents[1]


def get_path_to_input_data(year: int, day: int) -> Path:
    """Get path to static data used as input for problem of the day"""
    return get_project_root() / "data" / str(year) / f"{day:02d}.txt"


def get_path_to_module(year: int, day: int) -> Path:
    """Get path to static data used as input for problem of the day"""
    return get_project_root() / "aoc" / f"year_{year}" / f"day_{day:02d}"


def get_solver_module(year: int, day: int) -> SolverModule:
    """Load solver module dynamically given year and day"""
    try:
        path_to_module = f"aoc.year_{year}.day_{day:02}"
        module = importlib.import_module(f"{path_to_module}.solver")
        return cast(SolverModule, module)
    except ModuleNotFoundError:
        raise ValueError(f"Could not load solver for {year} {day}")


def read_raw_input(year: int, day: int) -> str:
    """Read in input data and transform appropriately"""
    path_to_data = get_path_to_input_data(year, day)
    with path_to_data.open(mode="r") as f:
        return f.read()


def initialize_data_dir(year: int, day: int) -> None:
    """Create directory needed for input data"""
    path_to_data = get_path_to_input_data(year, day)
    path_to_data.parent.mkdir(parents=True, exist_ok=True)
    path_to_data.touch()


def initialize_module_dir(year: int, day: int) -> None:
    """Create directory needed for solution module render Solver template"""
    path_to_module = get_path_to_module(year, day)
    path_to_module.mkdir(parents=True, exist_ok=True)

    init_file = path_to_module / "__init__.py"
    submodule = path_to_module / "solver.py"

    content = templates.get_template("solver.py.j2").render(year=year, day=day)
    if not submodule.exists():
        init_file.touch()
        submodule.touch()
        submodule.write_text(content)
