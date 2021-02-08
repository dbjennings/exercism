import math

def score(x, y):
    dist = math.sqrt(x*x+y*y)

    s = 1 if dist<=10 else 0
    s += 4 if dist<=5 else 0
    s += 5 if dist<=1 else 0

    return s