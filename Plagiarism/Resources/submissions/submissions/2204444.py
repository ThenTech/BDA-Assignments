sentence = input("Please enter a sentence")
alphabet = "abcdefghijklmnopqrstuvwxyz"


for i in range(len(alphabet)):
    aantal = 0 
    for k in range(len(sentence)):
        if alphabet[i] == sentence[k]:
            aantal += 1
    print(alphabet[i],": ",aantal,sep="")    
    