def is_palindrome_sentence(sentence):
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lengte = len(sentence)-1
    lengtel = len(letter)
    woordzonder = ""
    
    for i in range (1,lengte):
        for j in range (0,lengtel):
            if j == lengtel-1:
                break
            if sentence[i]== letter[j]:
                woordzonder += letter[j]
                break
    woordzonderiets = woordzonder.upper()
    lengtew = len (woordzonderiets)
    for i in range (0, lengtew//2):
        if woordzonderiets[i]!==woordzonderiets[lengtew-i]:
            return False
    return True