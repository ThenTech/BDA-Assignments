def convert(number):
    if len(number) > 0:
        output = int(number[0])
        convert(number[1:])
        return output
    