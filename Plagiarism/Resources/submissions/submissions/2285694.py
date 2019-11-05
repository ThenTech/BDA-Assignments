def create_sequence(string, index, length):
    tevullenwoord = ''
    for x in range(length):
        teller = index % len(string)
        tevullenwoord += string[teller]
        index += 1
    return tevullenwoord