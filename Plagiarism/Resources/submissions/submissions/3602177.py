i = -1
def convert(number):
    while len(number) > 1:
        i=i+1
        return convert(number[0:len(number)-(i+1)]) + (10**i) * int(number[len(number) - i - 1]) 
    pass
    return int(number)

convert("12345")