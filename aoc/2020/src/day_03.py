from math import ceil, prod

from data import DATA_FOLDER


def part_one(tmap, down, right):
    """Day 3: Toboggan Trajectory (part 1)"""
    r_index = 0
    tree_count = 0
    for row in tmap[down::down]:
        r_index += right
        if row[r_index] == "#":
            tree_count += 1
    return tree_count


def part_two(tmap):
    """Day 3: Toboggan Trajectory (part 2)"""
    shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (part_one(tmap, down, right) for right, down in shifts)
    return prod(counts)


if __name__ == "__main__":
    with open(DATA_FOLDER / "day_03.txt") as f:
        tmap = f.read().splitlines()
        n_copies = ceil(len(tmap) * round((len(tmap) / 4)))
        tmap_dup = [map_row * n_copies for map_row in tmap]
        print(f"Ans 1: {part_one(tmap_dup, down=1, right=3)}")
        print(f"Ans 2: {part_two(tmap_dup)}")
