def count_words(string):
    words = 0
    for i in string:
        if 'A' > i > 'Z' or 'a' > i > 'z':
            words += 1
    
    print(words)

            
    
    