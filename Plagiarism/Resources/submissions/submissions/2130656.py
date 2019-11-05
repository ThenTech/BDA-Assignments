x=int(input("geef getal"))
y=int(input("geef getal"))
resultaat=1
for i in (0,y):
    resultaat=resultaat*((x-i)/(y-i))
print(int(resultaat))