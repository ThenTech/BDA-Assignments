digits = input("kom maar op")
i=0
aantal=0
while (i<len(digits)):
    getal = int(digits[i]) 
    if (getal%2==0):
        aantal+=1
print (aantal)