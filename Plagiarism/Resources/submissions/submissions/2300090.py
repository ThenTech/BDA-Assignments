def create_sequence(input, start, amount):
    returnString = ""
    first_char = len(input)+start
    char = first_char
    for i in range(0,amount):
        if char > len(input)-1:
            char = 0
        returnString += input[char]
        char += 1
    return returnString