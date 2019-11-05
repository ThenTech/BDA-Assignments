def convert(number):
    if int(number) == 0:
        return 0

    elif number[0] != "0":
        return int(number)

    elif number[0] == "0":
        convert(number[1:])