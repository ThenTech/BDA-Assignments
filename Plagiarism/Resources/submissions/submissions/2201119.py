def convert_to_uppercase(string):
    word = ""
    for y in string:
        if ord(y) > 64 and ord(y) < 90:
            word += y
        elif ord(y) < 65 or ord(y) > 90 and ord(y) < 97 or ord(y) > 122:
            word += y
        else:
            z = ord(y)-32
            word += chr(z)
    return word