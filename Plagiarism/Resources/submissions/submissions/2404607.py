def convert(number):
    if len(number) == 1:
        print(number[0])
    else:
        print(int(number[0]), end="")
        convert(number[1:])