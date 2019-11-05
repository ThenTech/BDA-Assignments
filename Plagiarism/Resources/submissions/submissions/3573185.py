def convert(number):
    if len(number) == 1:
        return number
    tiental = 10**(len(number)-1)
    sum = tiental * int(number[0])
    return sum + int(convert(number[1:]))