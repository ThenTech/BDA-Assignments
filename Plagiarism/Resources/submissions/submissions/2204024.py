def encode(s):
    lengte = len(s)
    new = ""
    i = 1
    teller = 0
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
                while s[j] == new[j]:
                    j +=1
                if s[j] != new[j]:
                    uitkomst = uitkomst[:j] + "X" + uitkomst[j+1:]
                    break
        i += 1
    return uitkomst