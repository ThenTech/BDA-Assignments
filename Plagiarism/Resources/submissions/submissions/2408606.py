def convert(number):
    if len(number) == 1:
        return number
    else:
        return int(int(number[0])*(10**(len(number)-1))) + int(convert(number[1:]))
print(convert("123"))