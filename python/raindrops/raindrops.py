def convert(number):
    
    pling = (number%3==0) * 'Pling'
    plang = (number%5==0) * 'Plang'
    plong = (number%7==0) * 'Plong'

    drops = f'{pling}{plang}{plong}'
    
    return drops if drops else str(number)