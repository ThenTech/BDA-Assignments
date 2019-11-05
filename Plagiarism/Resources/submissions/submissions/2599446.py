x = int(input("x"))
y = int(input("y"))

number = 0
for i in range(y):
    for j in range(x):
        number += 1
        print(number, end=" ",)
    print()
