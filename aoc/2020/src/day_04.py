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


def base_validator(pass_dict):
    """Validate that all required fields are present"""
    keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    pass_keys = set(pass_dict.keys())
    key_diff = keys - pass_keys

    if len(key_diff) > 1:
        return False
    if len(key_diff) == 1:
        return "cid" in key_diff
    return True


def complex_validator(pass_dict):
    """Check that not only all fields are present, but that content is valid"""

    def validate_ecl(ecl):
        ecl_set = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        return ecl in ecl_set

    def validate_hcl(hcl):
        return re.fullmatch(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hcl) is not None

    def validate_hgt(hgt):
        if "cm" in hgt:
            hgt_val, _ = hgt.split("cm")
            return 150 <= int(hgt_val) <= 193
        if "in" in hgt:
            hgt_val, _ = hgt.split("in")
            return 59 <= int(hgt_val) <= 76
        return False

    if not base_validator(pass_dict):
        return False
    if not validate_ecl(pass_dict["ecl"]):
        return False
    if not validate_hcl(pass_dict["hcl"]):
        return False
    if not validate_hgt(pass_dict["hgt"]):
        return False
    if not 1920 <= int(pass_dict["byr"]) <= 2002:
        return False
    if not 2010 <= int(pass_dict["iyr"]) <= 2020:
        return False
    if not 2020 <= int(pass_dict["eyr"]) <= 2030:
        return False
    if len(str(pass_dict["pid"])) != 9:
        return False
    return True


def part_one(passport_input):
    """Day 4: Passport Processing (part 1)"""
    passports = clean_passports(passport_input)
    return sum(base_validator(pass_dict) for pass_dict in passports)


def part_two(passport_input):
    """Day 4: Passport Processing (part 2)"""
    passports = clean_passports(passport_input)
    return sum(complex_validator(pass_dict) for pass_dict in passports)


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_04.txt"
    with open(fpath) as f:
        passport_input = f.read()
        print(f"Ans 1: {part_one(passport_input)}")
        print(f"Ans 2: {part_two(passport_input)}")
