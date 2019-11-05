x = input("Geef een getal: ")

count = 0
for i in range(len(x)):
    if x[i] % 2 == 0:
        count += 1
print(count)