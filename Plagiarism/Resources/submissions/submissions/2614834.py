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
    if string == "":
        return string
    if string[len(string)-1] == " ":
        return string[:len(string)-1]
    return string
