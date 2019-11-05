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

    if s[len(x)-1] == " ":
        print(string[0:len(string)-1])
        return string[0:len(string)-1]
    else:
        print(string[0:len(string)])
        return string[0:len(string)]