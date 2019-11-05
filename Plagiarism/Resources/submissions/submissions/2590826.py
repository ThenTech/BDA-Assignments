def count_words(string):
    alphabet = "abcdefghijklmnopqrstuwxyz"
    symbols = "1234567890!,.;!@#$%^&()*_= |"
    i = 0
    counter = 0
    while i < len(string) - 1:
        if string[i] in alphabet:
            if string[i + 1] in symbols:
                counter += 1
            elif i == (len(string) - 2):
                counter += 1
        i += 1
    return counter