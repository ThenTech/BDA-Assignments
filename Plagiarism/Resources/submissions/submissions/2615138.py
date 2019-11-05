def convert(number, result=0):
    if len(number) != 0:
        result += int(number[0]) * (10**(len(number)-1))
        result = convert(number[1:], result)
    return result