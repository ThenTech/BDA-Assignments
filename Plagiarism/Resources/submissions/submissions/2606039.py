def mod_words(string):
    fouten_oprij = 0
    alfabet = "azertyuiopmlkjhgfdsqwxcvbn"
    nieuwe_string = ""
    for el in string:
        if el not in alfabet:
            if fouten_oprij == 0:
                nieuwe_string = nieuwe_string + "X"
                fouten_oprij +=1
        else:
            fouten_oprij = 0
            nieuwe_string = nieuwe_string + el
    return nieuwe_string


def check(string):
    if len(string) < 1:
        return False

    alfabet = "azertyuiopqsdfghklmwxcvbn"
    teller = 0
    for el in string:
        if not el in alfabet:
            teller = teller + 1

    if teller == len(string):
        return False

    return True


def count_words(string):
    if check(string) == False:
        return 0
    modded = mod_words(string)
    woorden = 1
    for el in modded[:-1]:
        if el == "X":
            woorden = woorden +  1
    return  woorden

#print(count_words("five 6 seven,eight!nine"))