"""This is the Solution for Year 2021 Day 02"""

from dataclasses import dataclass
from enum import Enum, auto

import aoc


class Direction(Enum):
    forward = auto()
    up = auto()
    down = auto()


@dataclass(frozen=True)
class Command:
    direction: Direction
    value: int


def parse_commands(lines: aoc.StrLines) -> list[Command]:
    """Split string commands into usable units"""
    split_items = (item.split() for item in lines)
    return [Command(direction=Direction[d], value=int(v)) for d, v in split_items]


def calculate_position(commands: list[Command], aim_activated: bool = False) -> int:
    """Based on a list of commands what position do we end up at"""

    x_pos = y_pos = aim = 0

    for command in commands:

        if command.direction is Direction.up:
            if aim_activated:
                aim -= command.value
            else:
                y_pos -= command.value

        elif command.direction is Direction.down:
            if aim_activated:
                aim += command.value
            else:
                y_pos += command.value

        else:
            if aim_activated:
                y_pos += command.value * aim
            x_pos += command.value

    return x_pos * y_pos


@aoc.expect(150)
def part_one(lines: aoc.StrLines) -> int:
    commands = parse_commands(lines)
    return calculate_position(commands)


@aoc.expect(900)
def part_two(lines: aoc.StrLines) -> int:
    commands = parse_commands(lines)
    return calculate_position(commands, aim_activated=True)


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
