def is_lowercase(c):
    return 'a' <= c <= 'z' # yes, this is allowed in Python!


def convert_to_uppercase(s):
    result = ""
    for c in s:
        if is_lowercase(c):
            c = chr(ord(c) - ord('a') + ord('A'))
        result += c

    return result


