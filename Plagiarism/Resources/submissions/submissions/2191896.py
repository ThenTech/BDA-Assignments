def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False



def is_palindrome_sentence(sentence):
    simple_sen = ""
    for characters in sentence:
        if in_alphabet(characters):
            simple_sen += characters
    simple_sen = simple_sen.lower()
    
    for characters in range(len(simple_sen)-1):
        if not simple_sen(characters) == simple_sen(len(simple_sen) -1 - characters):
            return False
            
    return True
        