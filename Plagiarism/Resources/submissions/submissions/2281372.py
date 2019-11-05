# checken als str met spaties begint --> allemaal wegdoen
# woorden onderscheiden, enkel spatie toestaan, dubbele verwijderen!

def cleanup_spaces(string):
    while True:
        if len(string) == 0 and string == "":
            return string
        if string[0]== " ":
            string = string[1:]
        elif string[0] != " ":
            break

    while True:
        if string[-1]== " ":
            string = string[:-2]
        elif string[-1] != " ":
            break
# buitenkanten zijn klaar
    teller = 0
    while teller < len(string):
        if string[teller] == " ":
            if string[teller+1] == " ":
                string = string[:teller] + string[teller+1:]
                continue
        teller = teller + 1
    return string
