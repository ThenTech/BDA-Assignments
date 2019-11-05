def letter(x):
    alfabet = "azertyuiopqsdfghjklmw<xcvbnAZERTYUIOPMLKJHGFDSQWXCVBN"
    return x in alfabet

def count_words(string):
    aantal_woorden = 1
    for el in string:
        if letter(el) == False:
            aantal_woorden = aantal_woorden + 1
    return aantal_woorden
print(count_words('one two'))