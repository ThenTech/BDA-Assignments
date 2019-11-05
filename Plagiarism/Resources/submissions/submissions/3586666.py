def count_words(string):
    words = 0
    validLetters = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in string:
        if i in alphabet or i.lower() in alphabet:
            validLetters += 1
        elif validLetters > 0:
            words += 1
            validLetters = 0
    
    if validLetters > 0:
        words += 1
        
    return words
            
    
    