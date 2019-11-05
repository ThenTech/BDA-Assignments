def is_palindrome_sentence(sentence):
    new_string = ""
    for i in sentence:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            new_string += i
    
    newest_string = ""
    for i in new_string:
        if 65 <= ord(i) <= 90:
            x = ord(i) + 32
            newest_string += x
        else:
            newest_string += x
            
    other_string = ""
    for i in range(len(newest_string)):
        x = len(newest_string) - 1 - i
        other_string += newest_string[x]
        
        
    return newest_string == other_string
            
    
    