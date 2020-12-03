from pathlib import Path


def part_one(passwd_input):
    """Day 2: Password Philosophy (part 1)"""
    c_range, c_target, passwd = passwd_input.split()
    c_min, c_max = [int(n) for n in c_range.split("-")]
    c_target = c_target.strip(":")
    c_count = sum(c == c_target for c in passwd)
    if c_count < c_min or c_count > c_max:
        return False
    return True


def part_two(passwd_input):
    """Day 2: Password Philosophy (part 2)"""
    c_range, c_target, passwd = passwd_input.split()
    c_idx = [int(n) for n in c_range.split("-")]
    c_target = c_target.strip(":")
    c_count = sum(c_target == passwd[idx - 1] for idx in c_idx)
    if c_count == 1:
        return True
    return False


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_02.txt"
    with open(fpath) as f:
        passwds = f.read().splitlines()
        print(f"Ans 1: {sum(part_one(p) for p in passwds)}")
        print(f"Ans 2: {sum(part_two(p) for p in passwds)}")
