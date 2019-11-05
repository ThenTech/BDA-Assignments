i = 0 
def convert(number):
    while len(number) <> 0:
        return convert(number[0:len(number)-(i+1)]) + (10**i) * int(number[len(number) - i - 1]) 
    pass
    return int(number)

convert("12345")