def cleanup_spaces(s):
    startspace = False
    string = ""
    for char in s:
        if char == " " and startspace == False:
            string += char
            startspace = True
           
        if char == " ":
            continu
            
        else:
            string += char
            startspace = False
    
    return string[1:len(string)-1]