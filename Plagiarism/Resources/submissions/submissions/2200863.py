sentence = input("geefma")
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lengte = len(sentence)-1
lengtel = len(letter)
woordzonder = ""
count = 0    
for i in range (0,lengte):
    for j in range (0,lengtel):
        if j == lengtel-1:
            if count != 0:
                print (woordzonder, str(count))
                count = 0
                woordzonder = ""
            break
        if sentence[i]== letter[j]:
            woordzonder += letter[j]
            count +=1
            break
    if i == lengte and count != 0:
        print (woordzonder, str(count))
    