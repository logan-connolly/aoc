from typing import Tuple

Cmd = Tuple[str, int]


def parse_command(command: str) -> Cmd:
    """Parse command input from 'nop +0' to ('nop', 0)"""
    cmd_type, value = command.split()
    sanitized_value = int(value.strip("+"))
    return cmd_type, sanitized_value
