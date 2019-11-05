def is_palindrome_sentence(sentence):
    count = 0
    
    for i in sentence:
        if not('a' < i.lower() < 'z' and i == sentence[len(sentence) - 1 - count]):
            return False
        else:
            count += 1
    return True