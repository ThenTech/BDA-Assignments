x = int(input())
sum = 0
prod = 1
for s in range(1, x + 1):
    prod = 1
    for p in (1, s + 1):
        prod = prod * p
    sum = sum + prod
print(sum)
