def solve(tmap, down, right):
    """Day 3: Toboggan Trajectory (part 1)"""
    row_index = 0
    tree_count = 0
    for row in tmap[down::down]:
        row_index += right
        if row[row_index % len(row)] == "#":
            tree_count += 1
    return tree_count
