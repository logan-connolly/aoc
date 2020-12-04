from .extract import extract_passwd_data


def solve(passwds):
    """Day 2: Password Philosophy (part 1)"""

    def valid_passwd(passwd_input):
        indices, target, passwd = extract_passwd_data(passwd_input)
        char_min, char_max = indices
        char_count = sum(char == target for char in passwd)
        return char_min <= char_count <= char_max

    return sum(valid_passwd(p) for p in passwds)
