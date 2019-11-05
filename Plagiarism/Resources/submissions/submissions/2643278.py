x = int(input("give an x: ")
sum = 0
for i in range(1, x + 1):
    fact = 1
    for j in range(1, i + 1):
        fact += j
    sum += fact
print(sum)
    