x = int(input("x = ?\n"))
y = int(input("y = ?\n"))

prod = 1

for i in range(y):
    prod *= (x-i)/(y-i)

print(int(prod))
