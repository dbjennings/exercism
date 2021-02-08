def is_armstrong_number(number):
    num_s = str(number)
    n = [int(s)**len(num_s) for s in num_s]
    return True if sum(n)==number else False