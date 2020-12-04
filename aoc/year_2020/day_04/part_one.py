from .cleaner import clean_passports
from .validator import validate


def solve(passport_input):
    """Day 4: Passport Processing (part 1)"""
    passports = clean_passports(passport_input)
    return sum(validate(pass_dict) for pass_dict in passports)
