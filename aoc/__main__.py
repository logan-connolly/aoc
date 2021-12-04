import sys
from typing import Optional, Sequence

from aoc import cli


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Command interface for aoc"""
    args = cli.parse_args(argv)

    if args.new:
        module_path = cli.create_new_day_entry(args.year, args.day)
        print(f"Generated module at {module_path}")
        sys.exit(0)

    answers = cli.get_solutions(args.year, args.day)
    cli.display_result(answers, args.year, args.day)


if __name__ == "__main__":
    main(sys.argv[1:])
