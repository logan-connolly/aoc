import argparse

from aoc import year_2020

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", "-y", help="Get solutions for year", default=2020)
    parser.add_argument("--day", "-d", help="Get solutions for day")
    args = parser.parse_args()
    solutions = {"2020": year_2020.run}
    try:
        solutions[args.year](args.day)
    except KeyError:
        print(f"No solutions for {args.year!r}")
