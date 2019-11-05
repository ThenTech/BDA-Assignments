x = int(input("Give a number: "))
total = 0
for i in range(x + 1):
    for j in range(i):
        total += j + 1
print(total)
