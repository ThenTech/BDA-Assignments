x = int(input("Give an x: "))

som = 0
result = 1
for i in range(1, x + 1):
    result *= i
    som += result
print(som)
