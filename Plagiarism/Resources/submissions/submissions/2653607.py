def convert(s):
    if s:
        return (ord(s[-1]) - ord('0')) + 10 * convert(s[:-1])
    else:
        return 0