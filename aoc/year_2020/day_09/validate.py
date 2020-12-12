def valid_preamble(subset, target):
    """Check if the sum of two numbers in subset equal target"""
    target_set = set()
    for num in subset:
        if num in target_set:
            return True
        target_set.add(target - num)
    return False
