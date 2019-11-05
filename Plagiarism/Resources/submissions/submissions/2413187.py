def convert(number):
    if len(number) == 1:
        return int(number)
    return convert(number[:-1]) * 10 + int(number[-1])