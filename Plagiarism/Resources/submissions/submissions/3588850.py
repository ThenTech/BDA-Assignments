def is_palindrome_sentence(sentence):
    if len(sentence) <= 1:
        return True
    
    else:
        if not ('a' < sentence[-1] < 'z' or 'A' < sentence[-1] < 'Z'):
            return is_palindrome_sentence(sentence[0:-1])
        elif not ('a' < sentence[0] < 'z' or 'A' < sentence[0] < 'Z'):
            return is_palindrome_sentence(sentence[1:])
        else:
            return sentence[0] == sentence[-1] and is_palindrome_sentence(sentence[1:-1])
        