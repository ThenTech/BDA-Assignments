def is_palindrome_sentence(sentence):
    count = 0
    
    for i in sentence:
        backwardsLetter = sentence[len(sentence) - 1 - count]
        if not('a' < i.lower() < 'z' and i == backwardsLetter and 'a' < backwardsLetter.lower() < 'z'):
            return False
        else:
            count += 1
    return True