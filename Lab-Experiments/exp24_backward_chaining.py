facts = {'fever', 'cough', 'loss_of_taste'}

rules = {
    'covid19': ['respiratory_infection', 'loss_of_taste'],
    'respiratory_infection': ['fever', 'cough'],
    'flu': ['fever', 'body_ache']
}

def backward_chaining(goal):
    if goal in facts:
        return True
    if goal in rules:
        return all(backward_chaining(sub_goal) for sub_goal in rules[goal])
    return False

hypothesis = 'covid19'
result = backward_chaining(hypothesis)
print("Known Symptoms:", facts)
print(f"Can we conclude '{hypothesis}'? ->", result)
