x = int(input("Give a number: "))
y = int(input("Give a number: "))
count = 1
for i in range(y):
    for j in range(x):
        print(count, end=" ")
        count += 1
    print()