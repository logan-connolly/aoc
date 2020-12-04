from pathlib import Path


def extract_passwd_data(passwd_input):
    """Helper for formatting input data"""
    _range, target, passwd = passwd_input.split()
    indices = [int(n) for n in _range.split("-")]
    return indices, target.strip(":"), passwd


def part_one(passwd_input):
    """Day 2: Password Philosophy (part 1)"""
    indices, target, passwd = extract_passwd_data(passwd_input)
    char_min, char_max = indices
    char_count = sum(char == target for char in passwd)
    return char_min <= char_count <= char_max


def part_two(passwd_input):
    """Day 2: Password Philosophy (part 2)"""
    indices, target, passwd = extract_passwd_data(passwd_input)
    char_count = sum(target == passwd[idx - 1] for idx in indices)
    return char_count == 1


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_02.txt"
    with open(fpath) as f:
        passwds = f.read().splitlines()
        print(f"Ans 1: {sum(part_one(p) for p in passwds)}")
        print(f"Ans 2: {sum(part_two(p) for p in passwds)}")
