x= int(input("Geef getal"))
y= int(input("Geef getal"))
resultaat=1
for i in range(0,y):
    resultaat=resultaat*((x-i)/(y-1))
print(resultaat)