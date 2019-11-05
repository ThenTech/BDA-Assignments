x = int(input("x: "))
while x < 1:
    x = int(input("x: "))


def fact(x):
    total = 1
    for i in range(x+1):
        val = i + 1
        total *= val
    return total


total2 = 0

for i in range(x):
    total2 += fact(i)
print(total2)