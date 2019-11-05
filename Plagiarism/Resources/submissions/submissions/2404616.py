def convert(number):
    result = 0
    if len(number) != 0:
        digit = int(number[0])
        result += digit * 10 ** (len(number)-1)
        result += convert(number[1:])
    return result