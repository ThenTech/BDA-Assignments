woord = input("geef maar een woord")

i = len (woord)
j = int(i/2)
k=0
varjuist = true

while (j>0):
    
    if woord[i]== woord[k]:
        k += 1
        i -=1
        j -= 1
    else:
        varjuist = false
        break
        print (woord, "is not a palindrome")
    
    
if varjuist == true:
    print (woord, "is a palindrome")