def encode(s):
    lengte = len(s)
    if lengte == 0:
        return "0"
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


def decode(s, n):
    pass