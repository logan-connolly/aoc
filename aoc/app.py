import argparse

from aoc import year_2020


def parse_args(args):
    """Parse command line arguments from user"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", "-y", help="Get solutions for year", default="2020")
    parser.add_argument("--day", "-d", help="Get solutions for day")
    return parser.parse_args(args)


def get_solutions(args):
    """Based on user input, get requested solutions"""
    solutions = {"2020": year_2020.run}
    try:
        solutions[args.year](args.day)
    except KeyError:
        print(f"No solutions for {args.year!r}")
