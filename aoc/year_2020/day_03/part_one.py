def solve(tmap, down, right):
    """Day 3: Toboggan Trajectory (part 1)"""
    r_index = 0
    tree_count = 0
    for row in tmap[down::down]:
        r_index += right
        if row[r_index] == "#":
            tree_count += 1
    return tree_count
