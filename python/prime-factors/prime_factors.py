from math import sqrt

def factors(value: int):
    r = []
    for n in range(2,int(sqrt(value))+2):
        while (value%n==0):
            r.append(n)
            value /= n
    if value!=1: r.append(value)
    return r