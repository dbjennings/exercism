def square(number):
    if not 0<number<65:
        raise ValueError('Not in valid range: 1-64')
    
    return 2**(number-1)

def total():
    return sum(square(n) for n in range(1,65))
