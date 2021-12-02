"""This is the Solution for Year 2021 Day 02"""

from dataclasses import dataclass
from enum import Enum, auto

from aoc.abstracts.solver import Answers, StrLines


class Direction(Enum):
    forward = auto()
    up = auto()
    down = auto()


@dataclass
class Command:
    direction: Direction
    value: int


def parse_commands(lines: StrLines) -> list[Command]:
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


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        commands = parse_commands(lines)
        return calculate_position(commands)

    def _solve_part_two(self, lines: StrLines) -> int:
        commands = parse_commands(lines)
        return calculate_position(commands, aim_activated=True)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
