def to_digit(number):
    return ord(number) - ord("0")




def convert(number):
    if len(number) == 1:
        last_digit = to_digit(number[0])
    else:
        last_digit = to_digit(number[len(number)-1])
        other_digits = convert(number[:len(number) - 1]
        return 10 * other_digits + last_digit
