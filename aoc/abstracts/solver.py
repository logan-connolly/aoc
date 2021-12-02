from dataclasses import dataclass
from typing import Protocol, Sequence, Union

Lines = Sequence[Union[int, str]]
IntLines = Sequence[int]
StrLines = Sequence[str]


@dataclass
class Answers:
    """Package answers in an object"""

    part_one: int
    part_two: int


class Solvable(Protocol):
    """Define how a Solution class should look to be passed to runner"""

    data: str

    def _preprocess(self) -> Lines:
        """Take raw string data and convert into processed lines"""
        ...

    def _solve_part_one(self) -> int:
        """Return answer for part one of AOC problem"""
        ...

    def _solve_part_two(self) -> int:
        """Return answer for part two of AOC problem"""
        ...

    def solve(self) -> Answers:
        """Return answers for a given day"""
        ...


class SolverModule(Protocol):
    """Add type for loading solver dynamically with importlib"""

    def Solver(self, data: str) -> Solvable:
        ...
