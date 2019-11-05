def convert(number):
    if len(number) == 0:
        return number[0]
    else:
        return number[0] * (10**(len(number) - 1)) + convert(number[1:])