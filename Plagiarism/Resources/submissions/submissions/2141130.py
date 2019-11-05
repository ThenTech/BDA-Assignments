import math

x = int(input("Give a number: "))
count = 0
for i in range(x):
    count += math.factorial(i + 1)
print(count)