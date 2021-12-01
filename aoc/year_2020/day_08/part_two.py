import copy

from aoc.year_2020.day_08.accumulate import loop_accumulate
from aoc.year_2020.day_08.parse import parse_command


def solve(str_commands: list[str]) -> int:
    """Day 08: Handheld Halting (part 2)"""

    parsed = [parse_command(cmd) for cmd in str_commands]
    last_cmd_index = len(parsed) - 1
    swapable = [i for i, cmd in enumerate(parsed) if cmd[0] in ("nop", "jmp")]
    answer = -1

    for swap_index in swapable:
        commands = copy.deepcopy(parsed)
        cmd, val = commands[swap_index]
        new_cmd = "jmp" if cmd == "nop" else "nop"
        commands[swap_index] = (new_cmd, val)
        idx, acc = loop_accumulate(commands, idx_set=set(), values=(0, 0))
        if idx > last_cmd_index:
            answer = acc
            break

    return answer
