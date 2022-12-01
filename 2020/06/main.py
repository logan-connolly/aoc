"""This is the Solution for Year 2020 Day 06"""

import re

import aoc


@aoc.expect(11)
def part_one(lines: aoc.StrLines) -> int:
    cleaned = [re.sub(r"\n", "", answer).strip() for answer in lines]
    return sum(len(set(answer)) for answer in cleaned)


@aoc.expect(6)
def part_two(lines: aoc.StrLines) -> int:
    cleaned = [answer.rstrip("\n").split("\n") for answer in lines]
    shared_answer_count = 0
    for group in cleaned:
        shared_answers = set.intersection(*[set(member) for member in group])
        shared_answer_count += len(shared_answers)
    return shared_answer_count


def main():
    lines = aoc.read(__file__).split("\n\n")
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
