def convert(s):
    getal = 0
    if len(s) == 1:
        getal += int(s)
    else:
        getal += int(s[0])*10**(len(s) - 1) + int(convert(s[1:]))
    return getal