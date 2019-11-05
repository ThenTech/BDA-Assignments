def convert(number):
    if len(number) > 0:
        if number[0] != 0:
            output = number[0]
        convert(number[1:])
return int(output)
    