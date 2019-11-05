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
    decoded = ""
    for i in range(len(value)):
        decoded += ""
    
    for chars in range(1, len(value)-1):
        if value[char] == 2:
            decoded = decoded[:char-1] + "X" + decoded[char] + "X" + decoded[char+2:]
            
    for chars in range(1, len(value)-1):
        if value[char] == 1:
            if not decoded[char-1] == "X" or decoded[char+1] == "X":
                decoded = decoded[:char-1] + "X" + decoded[char:]  
    
    print(decoded)          