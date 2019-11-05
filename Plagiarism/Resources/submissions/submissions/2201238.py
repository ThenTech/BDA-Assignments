def encode(s, n):
    niet = ''',?;.:/"<>[]^!'“”’ '''
    nieuw = ""
    for i in s:
        if i in niet:
            nieuw += i
        else:
            getal = ord(i) + n
            if getal > 26:
                getal -= 26
                if getal > 26:
                    getal -= 26
            elif getal < 0:
                getal += 26
                if getal < 0:
                    getal += 26
            nieuw += chr(getal)
    return nieuw

def decode(s, n):
    pass