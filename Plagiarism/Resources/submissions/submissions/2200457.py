def letter(x):
    alfabet = "azertyuiopqsdfghjklmw<xcvbnAZERTYUIOPMLKJHGFDSQWXCVBN"
    return x in alfabet

def count_words(string):
    if string == "" or string == " ":
        return 0

    zuiver = ""
    aantal_woorden = 1
    for el in string:
        if letter(el) == True:
            zuiver = zuiver + el
        else:
            zuiver = zuiver + " "

    for el in zuiver:
        if el == " ":
            aantal_woorden = aantal_woorden + 1
    return aantal_woorden

print(count_words('onetwo'))