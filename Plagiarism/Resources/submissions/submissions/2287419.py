alfabet="AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn"

def herken_woorden(string):
    string_aangepast = ""       #filtert string van tekens
    for el in string:
        if el == " ":
            continue
        if el in alfabet:
            string_aangepast = string_aangepast + el
        else:
            string_aangepast = string_aangepast + " "           # zet teveel spaties als die teveel moet filteren

    string_print = ""
    string_aangepast = string_aangepast + " "                   # zo wordt ook het laatste woord geprint
    for el in string_aangepast:
        if not el == " ":
            string_print = string_print + el
        elif len(string_print) == 0:
            continue
        else:
            print(string_print, len(string_print))
            string_print = ""

herken_woorden("Python! programming     ....  ROCKS")