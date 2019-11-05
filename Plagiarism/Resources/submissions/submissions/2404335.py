def convert(number):
    if len(number) == 1:
        print(number)
    else:
        print(number[0], end="")
        convert(number[1:])
convert("")