def cleanup_spaces(string):
    for i in range(len(string)):
        while i == 0 and string[i] == " ":
            string = string[1:]

    for i in range(len(string)):
        while i == (len(string)-1) and string[i] == " ":
            string = string[:len(string)-2]

    while "  " in string:
        for i in range(len(string)):
            if i > 1:
                if string[i-1] == " " and string[i] == " ":
                    string = string[:i-1] + string[i:]
    return string