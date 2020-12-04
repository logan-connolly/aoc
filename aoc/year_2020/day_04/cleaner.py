import re


def clean_passports(passport_input):
    """Take string input and split into list of passport dictionaries"""

    def extract_data(passport_input):
        individuals = passport_input.split("\n\n")
        return [re.sub(r"\n", " ", ind).strip() for ind in individuals]

    def passport_dict(passport):
        return dict(item.split(":") for item in passport.split())

    return [passport_dict(passport) for passport in extract_data(passport_input)]
