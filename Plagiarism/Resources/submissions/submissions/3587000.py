def is_palindrome_sentence(sentence):
    countForward = 0
    countBackward = len(sentence) - 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    while countForward < countBackward:
        if sentence[countForward].lower() in alphabet and not(sentence[countBackward].lower in alphabet):
            countBackward -= 1
        elif not(sentence[countForward].lower() in alphabet) and sentence[countBackward].lower in alphabet:
            countForward += 1
        else:
            if sentence[countForward].lower() != sentence[countBackward].lower():
                return False
            else:
                countForward += 1
                countBackward -= 1
            
    return True