x = int(input("x = ?\n"))

sum = 0

for i in range(1, x+1):
    prod = 1
    for j in range(1, i+1):
        prod *= j

    sum += prod

print(sum)
