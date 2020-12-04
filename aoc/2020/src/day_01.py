from data import DATA_FOLDER


def part_one(nums, target=2020):
    """Day 1: Report Repair (part 1)"""
    target_set = set()
    for num in nums:
        if num in target_set:
            return num * (target - num)
        target_set.add(target - num)
    return None


def part_two(nums):
    """Day 1: Report Repair (part 2)"""
    first, rest = nums[0], nums[1:]
    new_target = 2020 - first
    match_found = part_one(rest, target=new_target)
    if match_found:
        return first * match_found
    return part_two(rest)


if __name__ == "__main__":
    with open(DATA_FOLDER / "day_01.txt") as f:
        nums = [int(n) for n in f.read().splitlines()]
        print(f"Ans 1: {part_one(nums)}")
        print(f"Ans 2: {part_two(nums)}")
