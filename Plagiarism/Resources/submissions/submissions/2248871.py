def cleanup_spaces_vanvoor(s):
    inword = False
    string = ""

    for i in s:
        if "a"<= i <= "z" or "A"<= i <= "Z":
            inword = True
            string += i
        elif i == " " and not inword:
            inword = False
        else:
            string += i
    return  string


def cleanup_spaces_vanachter(s):
    inword = False
    string = ""
    i = len(s)

    while i > 0:
        i -= 1
        if s[i] != " ":
            inword = True
            string += s[i]
        elif s[i] == " " and not inword:
            inword = False
        else:
            string += s[i]

    string_goed = ""
    j = len(string)
    while j > 0:
        j -= 1
        string_goed += string[j]

    return string_goed


def cleanup_spaces_sides(s):
    s = cleanup_spaces_vanvoor(s)
    s = cleanup_spaces_vanachter(s)
    return s


def cleanup_spaces_middle(s):
    spatie = False
    string = ""

    for i in s:
        if i == " " and not spatie :
            spatie = True
            string += i
        elif i == " " and spatie:
            spatie = True
        else:
            spatie = False
            string += i
    return string


def cleanup_spaces(s):
    s = cleanup_spaces_sides(s)
    s = cleanup_spaces_middle(s)
    return s
print(cleanup_spaces("    Complex example   String !  "))