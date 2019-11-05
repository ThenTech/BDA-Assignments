def encode(s, n):
    tempString = ""
    for i in s:
        if 'a' <= i.lower() <= 'z':
            tempString += chr((ord(i) + n - 97) % 26 + 97)
        else:
            tempString += i
    return tempString


def decode(s, n):
    tempString = ""
    for i in s:
        tempString += chr((ord(i) - n - 97) % 26 + 97)
    return tempString