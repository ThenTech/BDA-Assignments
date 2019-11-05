def cleanup_spaces(string):
    count = False
    begin = "yes"
    cleaned = ""

    for letter in string:
        if letter == " ":
            count = False
            cleaned = cleaned + ""
        else:
            if count == False and begin != "yes":
                cleaned = cleaned + " "
            cleaned = cleaned + letter
            count = True
            begin = "no"       
    return cleaned