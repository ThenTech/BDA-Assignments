def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False



def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    word_counter = 0
    for characters in range(len(string)-1):
        if (not in_alphabet(string[characters]) or characters = 0) and in_alphabet(string[characters+1]):
            word_counter += 1
            
    return(word_counter)
        
                
        
    