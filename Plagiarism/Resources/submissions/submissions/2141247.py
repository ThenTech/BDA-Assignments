x = str(input("Geef een getal: "))
sum = 0
for i in range(len(x)):
    if int(x[i]) % 2 == 0:
        sum = sum +1
print(sum)