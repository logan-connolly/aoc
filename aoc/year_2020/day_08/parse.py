from typing import Tuple

Cmd = Tuple[str, int]


def parse_command(command: str) -> Cmd:
    """Parse command input from 'nop +0' to ('nop', 0)"""
    cmd_type, value = command.split()
    value = int(value[1:]) if "+" in value else int(value)
    return cmd_type, value
