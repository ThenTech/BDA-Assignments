x = int(input("geef nummer: "))
totaal =1
sum = 0
for i in range(1, x + 1 ):
    totaal *=  i
    sum += totaal

print(sum)