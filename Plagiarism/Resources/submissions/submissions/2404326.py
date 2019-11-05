
def convert(number):
    if len(number) > 1:

        return ((int(number[0]))*(10**(len(number)-1))) + int(convert(number[1:]))
    else:
        return int(number)