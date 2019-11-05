def convert_to_uppercase(stringToConvert):
    uppercase = ""
    for i in stringToConvert:
        if 97 <= ord(i) <= 122:
            uppercase += chr(ord(i) - 32)
        else:
            uppercase += i
    return uppercase
