def convert(number):
    
    pling = int(not number%3==0) * "Pling"

    return f'{pling}'

print(convert(3))