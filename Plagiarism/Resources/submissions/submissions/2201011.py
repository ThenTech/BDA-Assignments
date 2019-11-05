def convert_to_uppercase(string):
    word = ""
    for y in string:
        if ord(y) > 64 and ord(y) < 91:
            word += y
        elif y == " ":
            word += " "
        else:
            z = ord(y)-32
            word += chr(z)
    return word