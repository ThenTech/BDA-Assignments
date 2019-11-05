def convert_to_uppercase(s):
    new_string = ""
    for i in s:
        if 97 <= ord(i) <= 122:
            x = chr(ord(i) - 32)
            new.string.append(x)
        else:
            new_string.append(i)
    return new_string
            