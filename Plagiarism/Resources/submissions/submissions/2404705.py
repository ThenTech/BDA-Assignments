total = 0


def convert(number):
    global total
    total = 0
    calc_total(number, len(number)-1)
    return total


def calc_total(number, n):
    global total
    if number == '':
        return
    calc_total(number[1:], n-1)
    total += int(number[0]) * 10 ** n

print(convert('12345'))