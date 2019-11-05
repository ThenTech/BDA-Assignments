def cleanup_spaces(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    cleaned = ""
    place = -1
    j = 0
    k = 0
    for letter in string:
        if letter in alphabet:
            k = k + 1
        place = place + 1
        part = string[place:]
        for i in part:
            if i in " ":
                j = 0
            else:
                j = j + 1
                break
        if j == 0:
            break
        if letter == " ":
            if string[place + 1] == " ":
                continue
            else:
                cleaned = cleaned + " "
        else:
                cleaned = cleaned + letter
    if k != 0:
        if cleaned[0] == " ":
            cleaned = cleaned[1:]
        return cleaned
