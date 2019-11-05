def cleanup_spaces(string):
    cleaned = ""
    place = -1
    j = 0
    for letter in string:
        place = place + 1
        part = string[place:]
        for i in part:
            if i in " ":
                j = 0
            else:
                j = j + 1
                break
        if j == 0:
            exit()
        if letter == " ":
            if string[place + 1] == " ":
                continue
            else:
                cleaned = cleaned + " "
        else:
                cleaned = cleaned + letter
    if cleaned[0] == " ":
        cleaned = cleaned[1:]
    return cleaned