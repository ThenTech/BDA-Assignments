x= int(input("Geef getal"))
y= int(input("Geef getal"))
resultaat=1
for i in range(1,y-1):
    resultaat=resultaat*((x-i)/(y-1))
print(resultaat)