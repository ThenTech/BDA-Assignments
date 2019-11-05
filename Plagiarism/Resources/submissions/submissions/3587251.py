def convert_to_uppercase(s):
    tempString = ""
    for i in s:
        if ('a' < i < 'z'):
            tempString += char(ord(i) - 32)
        else:
            tempString += i
            