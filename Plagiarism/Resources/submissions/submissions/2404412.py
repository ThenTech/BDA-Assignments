def convert(number):
    if len(number) > 0:
        output = number[0]
        convert(number[1:])
        return output
    