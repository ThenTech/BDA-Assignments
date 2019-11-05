def count_words(string):
    words = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i not in alphabet or i.lower() not in alphabet:
            if i+1 in alphabet or (i+1).lower() in alphabet:
                words += 1
    return words
            
    
    