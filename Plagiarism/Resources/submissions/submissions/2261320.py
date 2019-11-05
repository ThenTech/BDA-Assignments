def cleanup_spaces(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in s:
        if i in lower:
            i = ord(i) - 32
            result += chr(i)
    return result     