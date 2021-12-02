from dataclasses import dataclass, field

from aoc.abstracts.solver import Answers, StrLines


@dataclass
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


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        passwords = [extract_password(raw_pw) for raw_pw in lines]
        return sum(validate_password_p1(pw) for pw in passwords)

    def _solve_part_two(self, lines: StrLines) -> int:
        passwords = [extract_password(raw_pw) for raw_pw in lines]
        return sum(validate_password_p2(pw) for pw in passwords)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
