import sys

from aoc import cli

if __name__ == "__main__":
    args = cli.parse_args(sys.argv[1:])
    year, day = args.year, args.day

    if args.new:
        module_path = cli.create_new_day_entry(year, day)
        print(f"Generated module at {module_path}")
        sys.exit(0)

    answers = cli.get_solutions(year, day)
    cli.display_result(answers, year, day)
