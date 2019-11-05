def convert(number):
    if len(number) == 1:
        print(int(number[0]))
    else:
        print(int(number[0]), end="")
        convert(number[1:])

convert("123456")