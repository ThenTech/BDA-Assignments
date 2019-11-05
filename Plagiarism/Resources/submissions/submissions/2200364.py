def is_palindrome_sentence(sentence):
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lengte = len(sentence)-1
    lengtel = len(letter)
    
    
    for i in range (1,lengte):
        for j in range (0,lengtel):
            if j == lengtel-1:
                break
            if sentence[i]== letter[j]:
                woordzonder += letter[j]
                break
            
    