def cleanup_spaces(string):
    count = False
    cleaned = ""
    
    for letter in string:
        if letter == " ":
            count = False
            cleaned = cleaned + ""
        else:
            if count == False:
                cleaned = cleaned + " "
            cleaned = cleaned + letter
            count = True