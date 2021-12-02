import copy

from aoc.abstracts.solver import Answers, StrLines

Command = tuple[str, int]
Result = tuple[int, int]


def parse_command(command: str) -> Command:
    """Parse command input from 'nop +0' to ('nop', 0)"""
    cmd_type, value = command.split()
    sanitized_value = int(value.strip("+"))
    return cmd_type, sanitized_value


def accumulate(commands: list[Command], idx_set: set[int], values: Result) -> Result:
    """Accummulate values while iterating/jumping through commands"""
    idx, acc = values
    if idx in idx_set:
        return idx, acc
    idx_set.add(idx)
    try:
        cmd, val = commands[idx]
        idx += 1 if cmd in ("nop", "acc") else val
        acc += val if cmd == "acc" else 0
        return accumulate(commands, idx_set, values=(idx, acc))
    except IndexError:
        return idx, acc


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        parsed_commands = [parse_command(cmd) for cmd in lines]
        _, acc = accumulate(parsed_commands, idx_set=set(), values=(0, 0))
        return acc

    def _solve_part_two(self, lines: StrLines) -> int:
        parsed = [parse_command(cmd) for cmd in lines]
        last_cmd_index = len(parsed) - 1
        swapable = [i for i, cmd in enumerate(parsed) if cmd[0] in ("nop", "jmp")]
        answer = -1

        for swap_index in swapable:
            commands = copy.deepcopy(parsed)
            cmd, val = commands[swap_index]
            new_cmd = "jmp" if cmd == "nop" else "nop"
            commands[swap_index] = (new_cmd, val)
            idx, acc = accumulate(commands, idx_set=set(), values=(0, 0))
            if idx > last_cmd_index:
                answer = acc
                break

        return answer

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
