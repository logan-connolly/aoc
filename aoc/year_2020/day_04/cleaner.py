import re


def clean_passports(passports):
    """Take string input and split into list of passport dictionaries"""

    def passport_dict(passport):
        return dict(item.split(":") for item in passport.split())

    cleaned = [re.sub(r"\n", " ", p).strip() for p in passports]
    return [passport_dict(passport) for passport in cleaned]
