
alfabet = "abcdefghijklmnopqrstuvwxyz"

def encode(s, n):
    positie_el = 0
    encoded_zin = ""
    for el in s:
        teller = 0
        if el == " " or (el in ",.:?!"):
            encoded_zin = encoded_zin + el
            continue
        for pos in alfabet:
            if el == pos:
                positie_el = teller
            teller = teller + 1
        nieuwe_pos = positie_el + n
        el = alfabet[nieuwe_pos]
        encoded_zin = encoded_zin + el
    return encoded_zin



def decode(s, n):
    s = encode(s,-n)
    return s