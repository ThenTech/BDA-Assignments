woord = input("geef maar een woord")

i = len (woord)-1
j = int(i/2)
k=0
varjuist = True

while (j>0):
    
    if woord[i]== woord[k]:
        k += 1
        i -=1
        j -= 1
    else:
        varjuist = False
        break
        print (woord, "is not a palindrome")
    
    
if varjuist == True:
    print (woord, "is a palindrome")