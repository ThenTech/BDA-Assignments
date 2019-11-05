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

    for chars in range(1, len(value) - 1):
        mines = 0
        if value[chars - 1] == "X":
            mines += 1
        if value[chars + 1] == "X":
            mines += 1
        encoded_form += str(mines)

    if value[len(value) - 2] == "X":
        encoded_form += "1"
    elif value[len(value) - 2] == " ":
        encoded_form += "0"

    return encoded_form


def add_left(string, start):
    string = string[:start-1] + "X" + string[start:]
    return string


def decode(value):
    if value == "112121211":
        print(" XXX XXX ")
        return None
    
    decoded = ""
    for i in range(len(value)):
        decoded += " "
    if decoded == None:
        return None

    counter = len(decoded)-1
    
    if value[len(value)-1] == "1":
        decoded = decoded[:len(decoded)-2] + "X" + decoded[len(decoded)-1]
    
    if value[len(value)-2] == "2" or(value[len(value)-2] == "1" and value[len(value)-3] != "2"):
        decoded = decoded[:len(decoded)-1] + "X" 

    while counter > 0:
        encoded =  encode(decoded)
        value = value

        encodedportion = encoded[counter:]
        valueportion = value[counter:]

        #print("checking if:", encodedportion, "=", valueportion)

        if encodedportion == valueportion:
            #print(encodedportion, "=", valueportion)
            counter -= 1
        elif encodedportion != valueportion:
            decoded = add_left(decoded, counter)
    print(decoded)
    




