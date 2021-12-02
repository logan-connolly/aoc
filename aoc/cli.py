import argparse
import importlib

from jinja2 import Environment, PackageLoader, select_autoescape

from aoc import db, io, runner

templates = Environment(loader=PackageLoader("aoc"), autoescape=select_autoescape())


def parse_args(args):
    """Parse command line arguments from user"""
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="Which year to fetch solution from")
    parser.add_argument("day", type=int, help="Which day of Advent")
    parser.add_argument("--new", dest="new", action="store_true", help="Create entry")
    return parser.parse_args(args)


def create_new_entry(args):
    """Create necessary files via templating for solving problem"""
    year, day = args.year, args.day
    content_one = templates.get_template("part_one.py.j2").render(year=year, day=day)
    content_two = templates.get_template("part_two.py.j2").render(year=year, day=day)
    io.generate_files(year, day, "part_one.py", content_one)
    io.generate_files(year, day, "part_two.py", content_two)
    return io.get_path_to_module(year, day)


def get_solutions(args):
    """Based on user input, get requested solutions"""
    base_module_path = f"aoc.year_{args.year}.day_{args.day:02}"
    try:
        part_one = importlib.import_module(f"{base_module_path}.part_one")
        part_two = importlib.import_module(f"{base_module_path}.part_two")
    except ModuleNotFoundError:
        raise ValueError(f"Could not load solution for {args.year} {args.day}")
    input_data = db.data[(args.year, args.day)]
    return runner.run(input_data, part_one, part_two)


def display_solutions(solutions, args):
    """Pretty print the results"""
    ans_one, ans_two = solutions
    print()
    print(f"Year {args.year} Day {args.day}:")
    print(f"  Part One: {ans_one}")
    print(f"  Part Two: {ans_two}")
    print()
