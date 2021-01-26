def convert(number):
    
    pling = int(number%3==0) * 'Pling'
    plang = int(number%5==0) * 'Plang'
    plong = int(number%7==0) * 'Plong'

    if pling or plang or plong:
        return f'{pling}{plang}{plong}'
    else:
        return str(number)