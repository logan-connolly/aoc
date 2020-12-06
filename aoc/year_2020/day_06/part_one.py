import re


def solve(answers):
    """Day 06: Custom Customs (part 1)"""
    cleaned = [re.sub(r"\n", "", ans).strip() for ans in answers]
    return sum(len(set(ans)) for ans in cleaned)
