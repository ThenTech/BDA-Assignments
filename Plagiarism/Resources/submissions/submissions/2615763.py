x = int(input("geef nummer: "))
y = int(input("geef nummer: "))

totaal =1
for i in range(0, y ):
    totaal *=  (x-i)/(y-i)
print(totaal)
# write your code here