def convert(number):
    if number == "":
        return "" 
    else:
        a = str(ord(number[0])) + str(cod(number[1:]))
        return int(a)