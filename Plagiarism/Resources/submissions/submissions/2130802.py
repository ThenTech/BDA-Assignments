x = int(input("Geef een waarde voor x = "))
y = int(input("Geef een waarde voor y = "))
product = 1

for i in range(y):
    product = product * (x/y)
    x = x - 1
    y = y - 1

print(int(product))
