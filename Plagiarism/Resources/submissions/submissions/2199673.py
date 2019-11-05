def encode(value):
    encoded_form = ""
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

    if value[len(value)-1] == "X":
        encoded_form += "1"
    elif value[len(value)-1] == " ":
        encoded_form += "0"
    
    return encoded_form

def decode(s, n):
    pass