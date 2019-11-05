x = int(input("x: "))
while x < 1:
    x = int(input("x: "))

total = 1

for i in range(x):
    val = i + 1
    total *= val
print(total)