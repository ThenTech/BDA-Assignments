def cleanup_spaces(s):
    nieuwe_string = ""
    teller = 0

    while True:
        if s[teller] != " ":
            break
        teller = teller + 1

    for el in range(teller, len(s)):
        if s[el] == " ":
            if s[el-1] != " " and s[el+1] != " ":
                nieuwe_string = nieuwe_string + " "
        else:
            nieuwe_string = nieuwe_string + s[el]

    return nieuwe_string


