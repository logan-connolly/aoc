import re
from pathlib import Path


def clean_passports(passport_input):
    """Take string input and split into list of passport dictionaries"""

    def extract_data(passport_input):
        individuals = passport_input.split("\n\n")
        return [re.sub(r"\n", " ", ind).strip() for ind in individuals]

    def passport_dict(passport):
        return dict(item.split(":") for item in passport.split())

    return [passport_dict(passport) for passport in extract_data(passport_input)]


def validate(pass_dict, full_check=False):
    """Check that not only all fields are present, but that content is valid"""

    def validate_keys():
        required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        pass_keys = set(pass_dict.keys())
        key_diff = required_keys - pass_keys
        if len(key_diff) > 1:
            return False
        if len(key_diff) == 1:
            return "cid" in key_diff
        return True

    def validate_ecl():
        return pass_dict["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def validate_hcl():
        return re.fullmatch(r"^#(?:[0-9a-fA-F]{3}){1,2}$", pass_dict["hcl"]) is not None

    def validate_hgt():
        hgt = pass_dict["hgt"]
        try:
            hgt_val, _ = hgt.split("cm") if "cm" in hgt else hgt.split("in")
            hgt_min, hgt_max = (150, 193) if "cm" in hgt else (59, 76)
            return hgt_min <= int(hgt_val) <= hgt_max
        except ValueError:
            return False

    def validate_pid():
        return len(pass_dict["pid"]) == 9

    def validate_range(val, min_val, max_val):
        return min_val <= int(val) <= max_val

    if validate_keys():
        if full_check:
            return all(
                [
                    validate_ecl(),
                    validate_hcl(),
                    validate_hgt(),
                    validate_pid(),
                    validate_range(pass_dict["byr"], 1920, 2002),
                    validate_range(pass_dict["iyr"], 2010, 2020),
                    validate_range(pass_dict["eyr"], 2020, 2030),
                ]
            )
        return True
    return False


def part_one(passport_input):
    """Day 4: Passport Processing (part 1)"""
    passports = clean_passports(passport_input)
    return sum(validate(pass_dict) for pass_dict in passports)


def part_two(passport_input):
    """Day 4: Passport Processing (part 2)"""
    passports = clean_passports(passport_input)
    return sum(validate(pass_dict, full_check=True) for pass_dict in passports)


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_04.txt"
    with open(fpath) as f:
        passport_input = f.read()
        print(f"Ans 1: {part_one(passport_input)}")
        print(f"Ans 2: {part_two(passport_input)}")
