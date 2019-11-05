def encode(s, n):
    lengte = len(s)
    if s[1] == "X":
        newstring = "1"
    else:
        newstring = "0"
    i = 1
    while i < lengte-2:
        teller = 0
        if s[i-1] == "X":
            teller +=1
        if s[i+1] == "X":
            teller +=1
        string += str(teller)
    if s[i-2] == "X":
        string += "1"
    else:
        string += "0"


def decode(s, n):
    pass