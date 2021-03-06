from .cleaner import clean_passports
from .validator import validate


def solve(passports):
    """Day 4: Passport Processing (part 1)"""
    cleaned = clean_passports(passports)
    return sum(validate(pass_dict) for pass_dict in cleaned)
