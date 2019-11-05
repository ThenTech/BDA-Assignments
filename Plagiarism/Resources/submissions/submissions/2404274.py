def convert(number):
    numbers = "0123456789"
    if number[0] in numbers:
        return int(number[0]) + convert(number[1:])
    else:
        return(int(number[0]))