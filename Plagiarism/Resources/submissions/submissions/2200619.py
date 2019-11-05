def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwqyz"
    new = ""
    for i in range(len(string)):
        if string[i] not in alphabet:
            new += " "
        else: 
            new += string[i]
    string = new.split()
    woorden = len(string)
    return woorden