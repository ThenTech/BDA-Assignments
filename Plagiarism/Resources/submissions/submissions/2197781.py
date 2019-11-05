def woorden_tellen(string):
    alfabet = "azertyuiopqsdfghjklmwxcvbn"
    teller = 0
    begin = 0
    for el in string:
        if el.lower() in alfabet:
            teller = teller + 1
        elif el.lower() not in alfabet:
            print(string[begin:teller], teller)
            teller = teller + 1
            begin = teller + 1
woorden_tellen('aaaappa')