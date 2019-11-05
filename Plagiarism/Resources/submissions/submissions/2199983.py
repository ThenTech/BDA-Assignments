def encode(value):
    encoded_form = ""
    
    if len(value) == 1:
        return "0"
        
    if len(value) == 0:
        return ""
    
    
    if value[1] == "X":
        encoded_form += "1"
    elif value[1] == " ":
        encoded_form += "0"
    
    for chars in range(1, len(value)-1):
        mines = 0
        if value[chars-1] == "X":
            mines += 1
        if value[chars+1] == "X":
            mines += 1
        encoded_form += str(mines)   

    if value[len(value)-2] == "X":
        encoded_form += "1"
    elif value[len(value)-2] == " ":
        encoded_form += "0"
    
    return encoded_form

def decode(value):
    tweedebom = False
    voorlaatstebom = False
    decoded_string = " "
    
    if value[1] == 1:
        tweedebom = True
    
    if value[len(value) -1] == 1:
        voorlaatstebom = True
    
    for i in range(1, len(value)):
        bomverder = False
        bomterug = False
    
        if value[i] == 1:
            bomverder = True
        if value[i] == 2:
            bomterug == True
            bomverder == True
        
        if bomterug == True:
            decoded_string = decodedstring[:i-1] + "X"
        if bomverder == True:
            decoded_string += " X"
        if bomterug == False and bomverder == False:
            decoded_string += "  "
            
    return decoded_string
    
    