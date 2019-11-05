def convert(number):
    if "0" < number < "9":
        print(int(number[0]), end="")
        convert(number[1:])
