def convert(number):
    if len(number) != 0:
        integer = (int(number[0]) * 10^(len(number)-1)) + convert(number[1:])
        return integer
    return 0
    
    