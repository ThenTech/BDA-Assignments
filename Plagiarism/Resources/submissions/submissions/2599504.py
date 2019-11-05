x = int(input("x"))
y = int(input("y"))
total = 1
for i in range(y):
    total *= ((x-i)/(y-i))
print(int(total))