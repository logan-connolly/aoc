def solve(answers):
    """Day 06: Custom Customs (part 2)"""
    shared_answer_count = 0
    cleaned_answers = [ans.rstrip("\n").split("\n") for ans in answers]
    for group in cleaned_answers:
        shared_answers = set.intersection(*[set(member) for member in group])
        shared_answer_count += len(shared_answers)
    return shared_answer_count
