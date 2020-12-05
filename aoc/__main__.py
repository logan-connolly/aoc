import sys

from aoc import app

if __name__ == "__main__":
    args = app.parse_args(sys.argv[1:])
    app.get_solutions(args)
