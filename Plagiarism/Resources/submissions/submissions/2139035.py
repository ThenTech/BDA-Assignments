# write your code here
getal= str(input())
lengthe= len(str(getal))
teller = 0
i=0
deelgetal= int(getal[i])
while i+1<lengthe:
    if deelgetal%2 == 0:
        teller +=1
        i+=1
        deelgetal= int(getal[i])
    else:
        i+=1
        deelgetal= int(getal[i])
print(teller)