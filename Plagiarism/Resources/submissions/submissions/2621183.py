def convert_to_uppercase(string):
    new_str = ""
    for i in string:
        if 97 <= ord(i) <= 122:
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    return new_str