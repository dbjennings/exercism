from functools import reduce

def classify(n):
    if n<=0: raise ValueError("Invalid entry")

    factors = set(reduce(list.__add__,
                ([i,n//i] for i in range(1,int(n**0.5)+1) if n%i==0)))
    
    total = sum(factors)-n

    if total==n:
        return "perfect"
    elif total>n:
        return "abundant"
    else:
        return "deficient"