sentence = input("Please enter a sentence")
alphabet = "abcdefghijklmnopqrstuvwxyz"


for i in alphabet:
    aantal = 0 
    for k in sentence:
        if i == k:
            aantal += 1
    print(i, ": ", aantal, sep="")    
    