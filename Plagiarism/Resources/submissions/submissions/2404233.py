total = 0
n = 0


def convert(number):
    global total
    global n
    if len(number) == 0:
        return
    convert(number[1:])
    total += int(number[0]) * 10 ** n
    n += 1
    return total