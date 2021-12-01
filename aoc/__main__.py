import sys

from aoc import cli

if __name__ == "__main__":
    args = cli.parse_args(sys.argv[1:])
    solutions = cli.get_solutions(args)
    cli.display_solutions(solutions, args)
