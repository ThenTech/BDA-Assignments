alfabet = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
cijfer = "1234567890"

def count_words(string):
    if string == " " or string == "" or string in cijfer:
        return 0
    positie = 0
    aantal_woorden = 1
    pol_oud = 0
    pol_nieuw = 0
    while positie < len(string):
        if string[positie] not in alfabet or string == " ":
           pol_nieuw = 1
        elif string[positie] in alfabet:
            pol_nieuw = 0

        if pol_oud != pol_nieuw:
            aantal_woorden = aantal_woorden + 1
        positie = positie + 1
        pol_oud = pol_nieuw
    return aantal_woorden

count_words("five 6 seven,eight")