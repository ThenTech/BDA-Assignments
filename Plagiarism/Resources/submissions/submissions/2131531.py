n = int(input("Give the first number: "))
r = int(input("Give the second number: "))

Output1N = 1
Output2N = 1
z = n - r
Output3N = 1
for x in range(1, n + 1):
    Output1N *= x
for y in range(1, r + 1):
    Output2N *= y
for z in range(1, z + 1):
    Output3N *= z
BinomialCoefficient = round(Output1N / (Output2N * Output3N))
print(BinomialCoefficient)
