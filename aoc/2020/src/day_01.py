from pathlib import Path


def part_one(lst):
    """Day 1: Report Repair (part 1)"""
    first, rest = lst[0], lst[1:]
    for item in rest:
        if first + item == 2020:
            return first * item
    return part_one(rest)


def part_two(lst):
    """Day 1: Report Repair (part 2)"""
    first, rest = lst[0], lst[1:]
    for idx, i in enumerate(rest):
        for j in rest[idx:]:
            if first + i + j == 2020:
                return first * i * j
    return part_two(rest)


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_01.txt"
    with open(fpath) as f:
        nums = [int(n) for n in f.read().splitlines()]
        print(f"Ans 1: {part_one(nums)}")
        print(f"Ans 2: {part_two(nums)}")
