def convert(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[0] + convert(s[1:])