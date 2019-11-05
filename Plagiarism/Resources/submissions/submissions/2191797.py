def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False



def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    word_counter = 0
    for characters in range(string-1):
        if not in_alphabet(string[characters]) and in_alphabet([characters]):
            word_counter += 1
            
    print(word_counter)
        
                
        
    