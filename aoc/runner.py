def run(data, solution_one, solution_two):
    """Generic runner for output solutions"""
    ans_one = solution_one.solve(data)
    ans_two = solution_two.solve(data)
    return ans_one, ans_two
