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
    decoded_string = ""
    
    if value[1] == "1":
        tweedebom = True
    
    if value[len(value) -1] == "1":
        voorlaatstebom = True
    
    for i in range(1, len(value)-1):
        if i == 1:    
            if value[i] == "2":
                decoded_string += "X"
            else:
                decoded_string += " "
        
        if value[i-1] == "1" or value[i-1] == "2":
            decoded_string += "X"
        elif value[i+1] == "2":
            decoded_string += "X"
        else:
            decoded_string += " "
        
        
            
    print(decoded_string)
