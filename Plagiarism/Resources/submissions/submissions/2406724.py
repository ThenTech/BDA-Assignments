def convert(number):
    converted_number = 0
    if len(number) > 0:
        converted_number += int(number[0]) * (10 ** (len(number) - 1))
        converted_number += convert(number[1:])

    return converted_number