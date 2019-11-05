def encode(s):
    lengte = len(s)
    if lengte == 0:
        return ""
    if lengte == 1:
            return "0"
    if s[1] == "X":
        newstring = "1"
    else:
        newstring = "0"
    i = 1
    while i < lengte-1:
        teller = 0
        if s[i-1] == "X":
            teller +=1
        if s[i+1] == "X":
            teller +=1
        newstring += str(teller)
        i += 1
    if s[i-1] == "X":
        newstring += "1"
    else:
        newstring += "0"
    return newstring


def decode(s):
    return None
    lengte = len(s)
    if lengte == 0:
        return ""
    if lengte == 1:
        return "X"
    i = 0
    newstring = "X" * lengte
    while True:
        newencode = encode(newstring)
        if newencode[i] != s[i]:
            newstring = newstring[:i+1] + " " + newstring[i+2:]
        if newencode == s:
            return newstring
        i +=1
    return newstring