sum = 0
def convert(number):
    global sum
    if len(number) > 0:
        sum += int(number[0]) * (10 ** (len(number) - 1))
        convert(number[1:])
    return sum