alfabet = "abcdefghijklmnopqrstuvwxyz"

def encode(s, n):
    resultaat = ""
    for i in s:
        if i in alfabet:
            indexteller = 0
            for j in alfabet:
                if j == i:
                    break
                indexteller += 1
            nieuweindex = indexteller + n
            while nieuweindex > 25:
                nieuweindex -= 26
            while nieuweindex < 0:
                nieuweindex += 26
            nieuweletter = alfabet[nieuweindex]
            resultaat += nieuweletter
        else:
            resultaat += i
    return resultaat

def decode(s, n):
    resultaat = ""
    for i in s:
        if i in alfabet:
            indexteller = 0
            for j in alfabet:
                if j == i:
                    break
                indexteller += 1
            nieuweindex = indexteller - n
            while nieuweindex > 25:
                nieuweindex -= 26
            while nieuweindex < 0:
                nieuweindex += 26
            nieuweletter = alfabet[nieuweindex]
            resultaat += nieuweletter
        else:
            resultaat += i
    return resultaat