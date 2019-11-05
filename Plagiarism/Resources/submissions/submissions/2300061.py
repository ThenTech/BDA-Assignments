def create_sequence(input, start, amount):
    first_char = len(input)+start
    char = first_char
    for i in range(0,amount):
        if char > len(input)-1:
            char = 0
        print(input[char], end="")
        char += 1