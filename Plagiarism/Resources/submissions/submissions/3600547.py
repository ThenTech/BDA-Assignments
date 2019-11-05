def convert(number):
    i = len(number)
    while True:
        if i == 0:
            return int(number[i]) * (10**len(number) - 1)
        else:
            i = i - 1
            return convert(number[0:len(number) - 2]) + (10**len(number) - i) * int(number[i])
