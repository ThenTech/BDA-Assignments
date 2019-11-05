def convert_to_uppercase(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in s:
        if i in lower:
            i = ord(i) - 32
            result += chr(i)
        else:
            result += i
    return result     