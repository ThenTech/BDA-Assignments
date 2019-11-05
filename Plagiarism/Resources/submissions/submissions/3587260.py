def encode(s, n):
    tempString = ""
    for i in s:
        tempString += 'a' + (n % 25)
    return tempString


def decode(s, n):
    tempString = ""
    for i in s:
        tempString += 'a' - (n % 25)
    return tempString