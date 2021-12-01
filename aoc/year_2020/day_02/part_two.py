from aoc.year_2020.day_02.extract import extract_passwd_data


def solve(passwds):
    """Day 2: Password Philosophy (part 2)"""

    def valid_password(passwd_input):
        indices, target, passwd = extract_passwd_data(passwd_input)
        char_count = sum(target == passwd[idx - 1] for idx in indices)
        return char_count == 1

    return sum(valid_password(p) for p in passwds)
