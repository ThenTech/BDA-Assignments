def encode(s, n):
    tempString = ""
    for i in s:
        tempString += chr(ord('a') + (n % 25))
    return tempString


def decode(s, n):
    tempString = ""
    for i in s:
        tempString += chr(ord('a') - (n % 25))
    return tempString