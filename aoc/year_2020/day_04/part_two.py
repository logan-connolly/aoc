from .cleaner import clean_passports
from .validator import validate


def solve(passport_input):
    """Day 4: Passport Processing (part 2)"""
    passports = clean_passports(passport_input)
    return sum(validate(pass_dict, full_check=True) for pass_dict in passports)
