import functools
from pathlib import Path

from ._typing import IntLines, StrLines


def expect(value):
    """Validate the result of the solution."""

    def inner(solver):
        @functools.wraps(solver)
        def wrapper(*args, **kwargs):
            result = solver(*args, **kwargs)
            assert result == value, f"expected: {value}, got: {result}"
            print(f"{solver.__name__}: {result}")

        return wrapper

    return inner


def read(source_file: str) -> str:
    return (Path(source_file).parent / "input.txt").read_text()


def read_str_lines(source_file: str) -> StrLines:
    return read(source_file).splitlines()


def read_int_lines(source_file) -> IntLines:
    return [int(line) for line in read_str_lines(source_file)]
