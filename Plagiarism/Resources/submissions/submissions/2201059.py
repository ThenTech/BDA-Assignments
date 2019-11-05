def convert_to_uppercase(string):
    word = ""
    for y in string:
        if ord(y) > 64 and ord(y) < 90:
            word += y
        elif ord(y) < 65 and ord(y) > 0 and ord(y) < 97 and ord(y) > 122:
            word += " "
        else:
            z = ord(y)-32
            word += chr(z)
    return word
