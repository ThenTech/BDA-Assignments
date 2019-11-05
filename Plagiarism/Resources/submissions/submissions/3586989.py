def is_palindrome_sentence(sentence):
    countForward = 0
    countBackward = len(sentence) - 1
    
    while countForward < countBackward:
        if 'a' < sentence[countForward].lower() < 'z' and not('a' < sentence[countBackward].lower() < 'z'):
            countBackward -= 1
        elif not('a' < sentence[countForward].lower() < 'z') and 'a' < sentence[countBackward].lower() < 'z':
            countForward += 1
        else:
            if sentence[countForward].lower() != sentence[countBackward].lower():
                return False
            else:
                countForward += 1
                countBackward -= 1
            
    return True