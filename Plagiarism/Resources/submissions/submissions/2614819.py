def cleanup_spaces(s):
    spatie = True
    string = ""
    for i in s:
        if i != " ":
            spatie = False
            string += i
        else:
            while not spatie:
                spatie = True
                string += " "
    return string