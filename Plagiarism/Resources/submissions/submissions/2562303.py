# No recursion
def convert(number):
    j = 0
    sign = 1
    if number[0] == "-":
        number = number[1:]
        sign = -1
    for i in number:
        j = j*10  + ord(i) - ord("0")
        j = sign * j

    return j