def to_digit(c):
    return ord(c) - ord("0")
def convert(number):
    if len(number) == 1:
        return to_digit(number)
    else:
        last_digit = to_digit(number[len(number) - 1])
        other_digits = convert(number[:len(number) - 1])
        return 10 * other_digits + last_digit