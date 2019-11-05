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
    lengte = len(s)
    if lengte == 0:
        return ""
    if lengte == 1:
        return "X"
    i = 0
    newstring = "X" * lengte
    newencode = encode(newstring)
    while i < lengte -1:
        if newencode[i] != s[i]:
            if s[i] == "2":
                newstring = newstring[:i-1] + "X" + newstring[i:]
                newstring = newstring[:i+1] + "X" + newstring[i+2:]
            elif s[i] == "0":
                newstring = newstring[:i-1] + " " + newstring[i:]
                newstring = newstring[:i+1] + " " + newstring[i+2:]
            else:
                if s[i-1] =="2":
                    newstring = newstring[:i+1] + " " + newstring[i+2:]
                elif s[i+1] =="2":
                    newstring = newstring[:i-1] + " " + newstring[i:]
                else:
                    newstring = newstring[:i+1] + " " + newstring[i+2:]
            newencode = encode(newstring)
        if newencode == s:
            return newstring
        i +=1
    if newencode[lengte-1] != s[lengte -1]:
        newstring = newstring[:i-1] + " " + newstring[i:]
    
    print(newstring)