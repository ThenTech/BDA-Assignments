x = int(input("Geef een integer x op: "))
sum = 0
for i in range(1, x+1):
    for j in range(1, i+1):
        sum = sum + j
print(sum)
    