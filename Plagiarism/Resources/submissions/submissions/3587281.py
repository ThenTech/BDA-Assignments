def encode(s, n):
    tempString = ""
    for i in s:
        if 'a' <= i.lower() <= 'z':
            tempString += chr((ord(i) - ord('a') + n) % 25 + ord('a'))  
        else
            tempString += i
    return tempString


def decode(s, n):
    tempString = ""
    for i in s:
        tempString += chr(ord('a') - (n % 25))
    return tempString