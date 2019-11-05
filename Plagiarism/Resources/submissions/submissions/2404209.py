def convert(number):
    result = 0
    if len(number) > 0:
        result += int(number[len(number)-1:])
    if len(number) > 1:
        result += convert(number[:len(number)-1]) * 10
    return result