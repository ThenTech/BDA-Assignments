def convert(number):
    return convert_helper(number, 1)


def convert_helper(number, multiply):
    total = 0
    if len(number) != 0:
        last_digit = int(number[-1])
        rest = number[:-1]
        total = last_digit * multiply
        total += convert_helper(rest, multiply * 10)
    return total