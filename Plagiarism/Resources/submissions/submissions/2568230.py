number = str(input("number: "))


def to_digit(character):
    return ord(character) - ord("0")

def convert(number):
    if (len(number) == 1):
        return to_digit(number)
    else:
        last_digit = to_digit(number[len(number) - 1])
        other_digits = convert(number[:len(number) - 1])
        return 10 * other_digits + last_digit


convert(number)