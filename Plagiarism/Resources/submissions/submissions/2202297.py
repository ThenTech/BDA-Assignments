def letter(x):
    alfabet = "azertyuiopqsdfghjklmwxcvbn"
    return x in alfabet

def zuiver(string):
    nieuwe_string =""
    teller = 0
    for el in string:
        if letter(el) == True:
            nieuwe_string = nieuwe_string + el
        elif  nieuwe_string[teller - 1] != " ":
            nieuwe_string = nieuwe_string + " "
        teller = teller + 1
    return nieuwe_string


def woorden_tellen(string):
    string = zuiver(string)
    aantal_woorden = 1
    for el in str(string):
        if el == " ":
            aantal_woorden = aantal_woorden + 1
    return aantal_woorden
