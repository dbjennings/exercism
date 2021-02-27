valid_digits = '1234567890X'

def is_valid(isbn: str) -> bool:
    values = [int(v.replace('X','10')) for v in isbn if v in valid_digits]

    if len(values)!=10 or max(values[:-1])>9: return False
    
    isbn_sum = sum([v*d for (v,d) in zip(values,range(10,0,-1))])
    return (isbn_sum%11==0)