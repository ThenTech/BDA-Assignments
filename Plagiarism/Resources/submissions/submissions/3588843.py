def is_palindrome_sentence(sentence):
    if len(sentence) <= 1:
        return True
    
    else:
        if ('a' > s[-1] > 'z' or 'A' > s[-1] > 'Z'):
            return is_palindrome_sentence(sentence[0:-1])
        elif ('a' > s[0] > 'z' or 'A' > s[0] > 'Z'):
            return is_palindrome_sentence(sentence[1:])
        else:
            return sentence[0] == sentence[-1] and is_palindrome_sentence(sentence[1:-1])
        