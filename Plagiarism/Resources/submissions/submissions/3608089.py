i = 0
def convert(number):
    while len(number) > 1:
        return int(number[i]) * 10 ** (len(number) - 1) + convert(number[i+1:])
    if len(number) == 1:
        return int(number)
    
    