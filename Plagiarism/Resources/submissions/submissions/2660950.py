def encode(s, n):
    empty_string = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            x = ord(s[i]) + n
            while x > 122:
                x = x - 26
            while x < 97:
                x = x + 26
            empty_string += chr(x)
        else: empty_string += s[i]
    return empty_string

def decode(s, n):
    empty_string = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            x = ord(s[i]) + n
            while x > 122:
                x = x - 26
            while x < 97:
                x = x + 26
            empty_string += chr(x)
        else:
            empty_string += s[i]
    return empty_string