# checken als str met spaties begint --> allemaal wegdoen
# woorden onderscheiden, enkel spatie toestaan, dubbele verwijderen!

def cleanup_spaces(string):

    nieuwe_string = ""
    teller = 0

    while True:
        if string[teller] != " ":
            break
        teller = teller + 1

    for el in range(teller, len(string)):
        if string[el] == " ":
            if string[el-1] != " ":
                nieuwe_string = nieuwe_string + " "
        else:
            nieuwe_string = nieuwe_string + string[el]

    return nieuwe_string

print(cleanup_spaces(input()))
