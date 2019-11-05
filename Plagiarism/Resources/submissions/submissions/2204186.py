def encode(s):
    lengte = len(s)
    new = ""
    i = 1
    teller = 0
    if lengte == 1:
        new = "0"
        return new
    if lengte == 0:
        return ""
    if s[1] == "X":
        new = str(1)
    else:
        new = str(0)
    while i < lengte:
        teller = 0
        if (i < lengte-1) and s[i+1] == "X":
            teller += 1
        if s[i-1] == "X":
            teller += 1
        new += str(teller)
        i+=1
    return new
def decode(s):
    lengte = len(s)
    i = 0
    uitkomst = " " * lengte
    while i < lengte:
        new =encode(uitkomst)
        if new == s:
            return new
        else:
            j=0
            while j < lengte:
                new = mine_left(new,s,new)
    return uitkomst
    
def mine_left(minefield,s,new):
    i = 0
    while s[i] == new[i]:
        i +=1
    while i < len(minefield) and minefield[i] == "x":
        i +=1
    while i < len(minefield) and minefield[i] == " ":
        minefield = minefield[:i] + "X" + minefield[i+1:]
        return minefield