def convert(number):
    numberstring = ""
    if number > 0:
        numberstring += number[0]
        convert(number[1:])
    else:
        return int(numberstring)
