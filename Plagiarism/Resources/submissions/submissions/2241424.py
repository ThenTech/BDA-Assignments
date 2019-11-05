def convert_to_uppercase(s):
    string = ""
    for x in s:
        if 'a' <= x <= 'z':
            y = chr(ord(x) - ord('a') + ord('A'))
            string = string + y
        else:
            string = string + x
    return string