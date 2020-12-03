from pathlib import Path


def part_one(lst, target=2020):
    """Day 1: Report Repair (part 1)"""
    if len(lst) < 2:
        return None

    first, rest = lst[0], lst[1:]
    for item in rest:
        if first + item == target:
            return first * item
    return part_one(rest, target)


def part_two(lst):
    """Day 1: Report Repair (part 2)"""
    first, rest = lst[0], lst[1:]
    new_target = 2020 - first
    match_found = part_one(rest, target=new_target)
    if match_found:
        return first * match_found
    return part_two(rest)


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_01.txt"
    with open(fpath) as f:
        nums = [int(n) for n in f.read().splitlines()]
        print(f"Ans 1: {part_one(nums)}")
        print(f"Ans 2: {part_two(nums)}")
