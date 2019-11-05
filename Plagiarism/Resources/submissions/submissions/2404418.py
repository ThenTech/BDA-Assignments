def convert(number):
    global x
    x = 0
    counter = 10**(len(number)-1)
    if len(number) != 1:
        convert(number[1:])
    x += int(number[0])*counter
    return x
print(convert("123"))