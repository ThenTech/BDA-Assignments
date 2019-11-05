def cleanup_spaces(s)
    startspace = Fals
    string = ""
    for char in s
        if char == " " and startspace == False:
            string += char
            startspace = True
           
        if char == " ":
            continue
        else
            string += char
    
        