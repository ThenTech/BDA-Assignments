def convert(number):
    numbers = "0123456789"
    if number in numbers:
        return int(number[0]) + convert(number)
    else:
        return(int(number[0]))