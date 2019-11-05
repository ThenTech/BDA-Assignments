def encode(s, n):
    tempString = ""
    for i in s:
        if 'a' <= i.lower() <= 'z':
            tempString += chr((ord(i) + n) % 26 + ord('a'))  
        else:
            tempString += i
    return tempString


def decode(s, n):
    tempString = ""
    for i in s:
        tempString += chr((ord(i) - n) % 26 + ord('a')) 
    return tempString