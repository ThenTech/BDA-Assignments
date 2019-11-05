i = 0
def convert(number):
    getal = 0
    if len(number) > 0:
        getal = int(number[i])*10**(len(number) - i - 1) + convert(number[i+1:])
    return getal