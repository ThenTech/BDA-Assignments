def is_palindrome_sentence(sentence):
    if len(sentence) <= 1:
        return True
    
    else:
        return (sentence[0] == sentence[-1] and is_palindrome_sentence(sentence[1:-1]))
        