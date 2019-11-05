def convert_to_uppercase (s):
    string = ''
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    for i in s:
        if i in alfabet:
            i = ord(i) - 32
            i = chr(i)
            string += i
        else:
            string += i
    return string
