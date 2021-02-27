def largest(min_factor, max_factor):
    return get_palindrome(min_factor, max_factor, small=False)

def smallest(min_factor, max_factor):
    return get_palindrome(min_factor, max_factor)

def get_palindrome(min_f, max_f, small=True):
    if max_f < min_f:
        raise ValueError("max_f < min_f")

    args = (min_f**2, max_f**2 + 1) if small else \
           (max_f**2, min_f**2 - 1, -1)

    for n in range(*args):
        if str(n)==str(n)[::-1]:
            factors = get_factors(n, min_f, max_f)
            if factors:
                return (n, factors)

    return None,[]
    

def get_factors(n, min_f, max_f):
    factors = []
    duplicates = set()

    for i in range(min_f, max_f+1):
        if n % i == 0 and min_f <= n//i <= max_f and \
           i not in duplicates and n//i not in duplicates:
            factors.append([i,n//i])
            duplicates.add(i)
            duplicates.add(n//i)
    
    return factors