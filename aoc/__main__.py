import sys

from aoc import cli

if __name__ == "__main__":
    args = cli.parse_args(sys.argv[1:])

    if args.new:
        module_path = cli.create_new_entry(args)
        print(f"Generated module at {module_path}")
        sys.exit(0)

    solutions = cli.get_solutions(args)
    cli.display_solutions(solutions, args)
