def create_sequence(input, start, amount):
    returnString = ""
    if start > 0:
        first_char = start
    else:
        first_char = len(input)+start
    char = first_char
    for i in range(0,amount):
        if char > len(input)-1:
            char = 0
        returnString += input[char]
        char += 1
    return returnString