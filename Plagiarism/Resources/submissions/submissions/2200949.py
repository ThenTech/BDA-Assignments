def encode(s, n):
    niet = ''',?;.:/"<>[]^!'“”’ '''
    nieuw = ""
    for i in s:
        if i in niet:
            nieuw += i
        else:
            getal = ord(s) + n
            nieuw += ord(getal)
    return nieuw


def decode(s, n):
    pass