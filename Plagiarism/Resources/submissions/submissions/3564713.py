x = int(input("x: "))
while x < 1:
    x = int(input("x: "))

sum = 0
total = 0
for i in range(1, x+1):
    sum += i
    total += sum
print(total)