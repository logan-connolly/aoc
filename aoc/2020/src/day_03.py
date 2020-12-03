from math import ceil, prod
from pathlib import Path


def part_one(tmap):
    """Day 3: Toboggan Trajectory (part 1)"""
    r_index = 0
    tree_count = 0
    for row in tmap[1:]:
        r_index += 3
        if row[r_index] == "#":
            tree_count += 1
    return tree_count


def part_two(tmap):
    """Day 3: Toboggan Trajectory (part 2)"""

    def count_trees(right, down):
        r_index = 0
        tree_count = 0
        for row in tmap[down::down]:
            r_index += right
            if row[r_index] == "#":
                tree_count += 1
        return tree_count

    shifts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (count_trees(r, d) for r, d in shifts)
    return prod(counts)


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data/day_03.txt"
    with open(fpath) as f:
        tmap = f.read().splitlines()
        n_copies = ceil(len(tmap) * round((len(tmap) / 4)))
        tmap_dup = [map_row * n_copies for map_row in tmap]
        print(f"Ans 1: {part_one(tmap_dup)}")
        print(f"Ans 2: {part_two(tmap_dup)}")
