def convert(number):
    digits = "0123456789"
    numberlist = []
    for i in range(len(number)):
        if number[i] in digits:
            numberlist.append(int(number[i]))
    return numberlist
