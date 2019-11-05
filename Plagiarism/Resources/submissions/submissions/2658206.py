def count_words(string):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    word = 0
    for in range(len(string) - 2):
        if i == 0:
            if string[i] in alfabet and string[i + 1] in alfabet:
                word += 1
        else:
            if string[i] in alfabet and string[i + 1] in alfabet and string[i - 1] not in alfabet:
                word += 1
    return word
        
        
