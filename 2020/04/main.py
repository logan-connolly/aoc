"""This is the Solution for Year 2020 Day 04"""

import re

import aoc

Passport = dict[str, str]


def parse_passport(passport: str) -> Passport:
    """Convert passport string into dictionary"""
    items = [item.split(":") for item in passport.split() if ":" in item]
    return {key: val for key, val in items}


def validate_passport(passport: Passport, full_check: bool = False) -> bool:
    """Check that not only all fields are present, but that content is valid"""

    def validate_keys() -> bool:
        required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        key_diff = required_keys - set(passport.keys())
        if len(key_diff) > 1:
            return False
        if len(key_diff) == 1:
            return "cid" in key_diff
        return True

    def validate_ecl() -> bool:
        return passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def validate_hcl() -> bool:
        return re.fullmatch(r"^#(?:[0-9a-fA-F]{3}){1,2}$", passport["hcl"]) is not None

    def validate_hgt() -> bool:
        hgt = passport["hgt"]
        try:
            hgt_val, _ = hgt.split("cm") if "cm" in hgt else hgt.split("in")
            hgt_min, hgt_max = (150, 193) if "cm" in hgt else (59, 76)
            return hgt_min <= int(hgt_val) <= hgt_max
        except ValueError:
            return False

    def validate_pid() -> bool:
        return len(passport["pid"]) == 9

    def validate_range(key: str, min_val: int, max_val: int) -> bool:
        return min_val <= int(passport[key]) <= max_val

    if validate_keys():
        if full_check:
            return all(
                [
                    validate_ecl(),
                    validate_hcl(),
                    validate_hgt(),
                    validate_pid(),
                    validate_range("byr", 1920, 2002),
                    validate_range("iyr", 2010, 2020),
                    validate_range("eyr", 2020, 2030),
                ]
            )
        return True
    return False


@aoc.expect(2)
def part_one(lines: aoc.StrLines) -> int:
    passports = [parse_passport(passport) for passport in lines]
    return sum(validate_passport(p) for p in passports)


@aoc.expect(2)
def part_two(lines: aoc.StrLines) -> int:
    passports = [parse_passport(passport) for passport in lines]
    return sum(validate_passport(p, full_check=True) for p in passports)


def main():
    content = aoc.read(__file__)
    lines = [re.sub(r"\n", " ", p).strip() for p in content.split("\n\n")]
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
