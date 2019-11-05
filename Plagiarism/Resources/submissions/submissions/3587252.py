def convert_to_uppercase(s):
    tempString = ""
    for i in s:
        if ('a' < i < 'z'):
            tempString += chr(ord(i) - 32)
        else:
            tempString += i
            