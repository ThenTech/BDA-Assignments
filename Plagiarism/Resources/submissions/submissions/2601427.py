def convert(number, sum=0):
    if len(number) > 0:
        sum += int(number[0]) * (10 ** (len(number) - 1))
        convert(number[1:], sum)
    return sum