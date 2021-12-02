import argparse
from pathlib import Path

from aoc import io, runner
from aoc.abstracts.solver import Answers


def parse_args(args: list[str]) -> argparse.Namespace:
    """Parse command line arguments from user"""
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="Which year to fetch solution from")
    parser.add_argument("day", type=int, help="Which day of Advent")
    parser.add_argument("--new", dest="new", action="store_true", help="Create entry")
    return parser.parse_args(args)


def create_new_day_entry(year: int, day: int) -> Path:
    """Create necessary files via templating for solving problem"""
    io.initialize_data_dir(year, day)
    io.initialize_module_dir(year, day)
    return io.get_path_to_module(year, day)


def get_solutions(year: int, day: int) -> Answers:
    """Based on user input, get requested solutions"""
    solver_module = io.get_solver_module(year, day)
    raw_input_data = io.read_raw_input(year, day)
    solver = solver_module.Solver(data=raw_input_data)
    return runner.run(solver)


def display_result(answers: Answers, year: int, day: int) -> None:
    """Pretty print the results"""
    print()
    print(f"Year {year} Day {day}:")
    print(f"  Part One: {answers.part_one}")
    print(f"  Part Two: {answers.part_two}")
    print()
