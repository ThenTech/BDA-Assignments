def convert(number):
    if len(number) == 1:
        return int(number)
    else:
        return convert(number[0:len(number) - 2] + int(number[len(number) - 1])
        
convert("12345")