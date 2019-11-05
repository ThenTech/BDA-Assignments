def convert_to_uppercase(s):
    newstring = ""
    for x in s:
        if "a"<=x<="z":
             y = ord(x)
             z = y-32
             newstring +=chr(z)
        else:
             newstring += x
    return newstring