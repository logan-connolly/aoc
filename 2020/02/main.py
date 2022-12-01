"""This is the Solution for Year 2020 Day 02"""

from dataclasses import dataclass, field

import aoc


@dataclass(frozen=True)
class PasswordData:
    indices: list[int] = field(default_factory=list)
    target: str = ""
    password: str = ""


def extract_password(raw_pw: str) -> PasswordData:
    _range, raw_target, password = raw_pw.split()
    indices = [int(n) for n in _range.split("-")]
    target = raw_target.strip(":")
    return PasswordData(indices, target, password)


def validate_password_p1(pw: PasswordData) -> bool:
    char_min, char_max = pw.indices
    char_count = sum(char == pw.target for char in pw.password)
    return char_min <= char_count <= char_max


def validate_password_p2(pw: PasswordData) -> bool:
    char_count = sum(pw.target == pw.password[idx - 1] for idx in pw.indices)
    return char_count == 1


@aoc.expect(2)
def part_one(lines: aoc.StrLines) -> int:
    passwords = (extract_password(raw_pw) for raw_pw in lines)
    return sum(validate_password_p1(pw) for pw in passwords)


@aoc.expect(1)
def part_two(lines: aoc.StrLines) -> int:
    passwords = (extract_password(raw_pw) for raw_pw in lines)
    return sum(validate_password_p2(pw) for pw in passwords)


def main():
    lines = aoc.read_str_lines(__file__)
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
