from typing import List, Set, Tuple

from aoc.year_2020.day_08.parse import Cmd

Result = Tuple[int, int]


def loop_accumulate(commands: List[Cmd], idx_set: Set[int], values: Result) -> Result:
    """Accummulate values while iterating/jumping through commands"""
    idx, acc = values
    if idx in idx_set:
        return idx, acc
    idx_set.add(idx)
    try:
        cmd, val = commands[idx]
        idx += 1 if cmd in ("nop", "acc") else val
        acc += val if cmd == "acc" else 0
        return loop_accumulate(commands, idx_set, values=(idx, acc))
    except IndexError:
        return idx, acc
