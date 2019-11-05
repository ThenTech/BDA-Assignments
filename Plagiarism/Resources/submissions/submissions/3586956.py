def is_palindrome_sentence(sentence):
    count = 0
    
    for i in sentence:
        backwardsLetter = sentence[len(sentence) - 1 - count]
        if 'a' < i.lower() < 'z' and 'a' < backwardsLetter.lower() < 'z':
            if (i == backwardsLetter):
                count += 1
            else:
                return False

    return True