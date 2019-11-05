def is_letter(ch):
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def count_words(string):
    i = 0
    counter = 0
    while i < len(string):
        while is_letter(string[i]):
            i += 1
            if not is_letter(string[i+1]):
                counter += 1
                i += 1
        while not is_letter(string[i]):
            i += 1
        counter += 1
        
        