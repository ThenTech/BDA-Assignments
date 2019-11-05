alfabet = "azertyuiopqsdfghjklmw<xcvbnAZERTYUIOPMLKJHGFDSQWXCVBN"

def count_words(string):
    if string == " ":
        return 0
    positie = 0
    aantal_woorden = 1
    beginpol = 0
    while positie > len(string):
        if string[positie] != alfabet:
            positie = positie + 1
            beginpol = 1

        if beginpol != 0:
            aantal_woorden = aantal_woorden + 1
    return aantal_woorden