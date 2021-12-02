from aoc.abstracts.solver import Answers, Solvable


def run(solver: Solvable) -> Answers:
    """Generic runner that receives Solvable object and returns answer"""
    return solver.solve()
