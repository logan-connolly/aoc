from . import day_01, day_02, day_03, day_04

solutions = {
    "1": day_01.solution,
    "2": day_02.solution,
    "3": day_03.solution,
    "4": day_04.solution,
}


def run(day=None):
    if day:
        try:
            solutions[day]()
        except KeyError:
            print(f"Could not find {day!r} in 2020")
    else:
        for solution in solutions.values():
            solution()
