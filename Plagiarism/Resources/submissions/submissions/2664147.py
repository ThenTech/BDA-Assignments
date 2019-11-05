def cleanup_spaces(s):
    startspace = False
    string = ""
    for char in s:
        if char == " " and startspace == False:
            string += char
            startspace = True
           
        if char == " ":
            continue
        else
            string += char
    
        