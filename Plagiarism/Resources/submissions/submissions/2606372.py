def cleanup_spaces(string):
    spaties = 0
    nieuwe_string=""
    for el in string:
        if el == " ":
            if spaties == 0:
                nieuwe_string = nieuwe_string + el
                spaties += 1
        elif el != " ":
            spaties = 0
            nieuwe_string = nieuwe_string + el

    if nieuwe_string[0] == " ":
        nieuwe_string = nieuwe_string[1:]
    if nieuwe_string[-1] == " ":
        nieuwe_string = nieuwe_string[:-1]

    return nieuwe_string

