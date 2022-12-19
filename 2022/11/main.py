"""This is the Solution for Year 2022 Day 11"""

from __future__ import annotations

import dataclasses
from collections.abc import Callable

import aoc


@dataclasses.dataclass
class Monkey:
    operation: Callable[[int], int]
    predicate: Callable[[int], int]
    items: list[int] = dataclasses.field(default_factory=list)
    items_seen: int = 0

    @staticmethod
    def _parse_operation(input: str) -> Callable[[int], int]:
        _, func_as_str = input.split(" = ")
        return eval(f"lambda old: {func_as_str}")

    @staticmethod
    def _parse_predicate(input: list[str]) -> Callable[[int], int]:
        raw_disible_by, raw_truthy, raw_falsey = input
        divisible_by = int(raw_disible_by.split()[-1])
        truthy = int(raw_truthy.split()[-1])
        falsey = int(raw_falsey.split()[-1])
        return eval(f"lambda n: {falsey} if n % {divisible_by} else {truthy}")

    @staticmethod
    def _parse_items(input: str) -> list[int]:
        *_, raw_numbers = input.split(": ")
        return [int(n) for n in raw_numbers.split(",")]

    @classmethod
    def build(cls, input: str) -> Monkey:
        _, raw_itemset, raw_op, *raw_pred = input.splitlines()
        return cls(
            operation=cls._parse_operation(raw_op),
            predicate=cls._parse_predicate(raw_pred),
            items=cls._parse_items(raw_itemset),
        )


MonkeyMap = dict[int, Monkey]


def play_round(mm: MonkeyMap) -> MonkeyMap:
    for m in mm.values():
        while m.items:
            item = m.items.pop(0)
            m.items_seen += 1
            val = m.operation(item) // 3
            monkey_id = m.predicate(val)
            mm[monkey_id].items.append(val)

    return mm


@aoc.expect(10605)
def part_one(lines: aoc.StrLines) -> int:
    mm = {idx: Monkey.build(line) for idx, line in enumerate(lines)}

    for _ in range(20):
        play_round(mm)

    *_, p2, p1 = sorted([monkey.items_seen for monkey in mm.values()])
    return p1 * p2


@aoc.expect(4)
def part_two(lines: aoc.StrLines) -> int:
    # not completed
    return -1


def main():
    text = aoc.read(__file__)
    lines = text.split("\n\n")

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
