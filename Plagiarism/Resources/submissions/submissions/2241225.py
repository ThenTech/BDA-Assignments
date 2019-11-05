def cleanup_spaces(s):
    spatie = True
    x = s[0]
    string = ""
    for x in s:
        if x == " " and not spatie:
            string = string + " "
        if x == " ":
            spatie = True
        else:
            string = string + x
            spatie = False
    return string[0:len(string)-1]