def latest(scores: list):
    return scores[-1]

def personal_best(scores):
    top = sorted(scores, reverse=True)
    return top[0]

def personal_top_three(scores):
    top = sorted(scores, reverse=True)
    return top[0:3]