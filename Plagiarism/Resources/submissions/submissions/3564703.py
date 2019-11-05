x = int(input("x: "))
while x < 1:
    x = int(input("x: "))
y = int(input("y: "))
while y < 1:
    y = int(input("y: "))

total = 1
for i in range(y):
    total *= (x-i) / (y-i)
print(int(total))