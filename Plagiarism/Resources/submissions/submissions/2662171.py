def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    start_word = False
    end_word = False
    
    for char in string:
        if char in alphabet:
            start_word = True
        
        elif start_word == True and (char not in alphabet or char == string[len(string)-1]):
            end_word = True
        
        if end_word == True:
            count +=1
    
    print(count)