import copy
from typing import List
from .parse import parse_command, Cmd
from .accumulate import loop_accumulate


def solve(commands: List[Cmd]) -> int:
    """Day 08: Handheld Halting (part 1)"""
    parsed = [parse_command(cmd) for cmd in commands]
    last_cmd_index = len(parsed) - 1
    swapable = [i for i, cmd in enumerate(parsed) if cmd[0] in ("nop", "jmp")]
    for swap_index in swapable:
        commands = copy.deepcopy(parsed)
        cmd, val = commands[swap_index]
        new_cmd = "jmp" if cmd == "nop" else "nop"
        commands[swap_index] = (new_cmd, val)
        idx, acc = loop_accumulate(commands, idx_set=set(), values=(0, 0))
        if idx > last_cmd_index:
            return acc
    return -1
