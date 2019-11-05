def convert_to_uppercase(s):
    string2 = ""
    for i in s:
        if 97 <= ord(i) <= 122:
            ascii_n = ord(i)
            ascii_n = ascii_n - 32
            ascii_n = chr(ascii_n)
            string2 += ascii_n

        else:
            string2 += i
    return string2