def count_words(string):
    woord = 0
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lengte = len(string)-1
    lengtel = len(letter)-1
    letterja = False
    for i in range (1,lengte):
        for j in range (0,lengtel):
            if string[i]== letter[j]:
                if letterja != True:
                    woord+=1
                letterja = True
                break
            letterja = False
    return woord