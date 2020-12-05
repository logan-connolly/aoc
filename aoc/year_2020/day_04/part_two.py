from .cleaner import clean_passports
from .validator import validate


def solve(passports):
    """Day 4: Passport Processing (part 2)"""
    cleaned = clean_passports(passports)
    return sum(validate(pass_dict, full_check=True) for pass_dict in cleaned)
