def cleanup_spaces(s):
    spatie = True
    string = ""
    for x in s:
        if x == " " and not spatie:
            string = string + " "
        if x == " ":
            spatie = True
        else:
            string = string + x
            spatie = False

    if s[len(x)-1] == " ":
        return string[0:len(string)-1]
    else:
        return string[0:len(string)]