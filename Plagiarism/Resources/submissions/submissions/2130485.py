x = int(input(""))
y = int(input(""))
count = 0

for i in range(y):
    for j in range(1, x + 1):
        print(str(int(j + count)), end=" ")
    count += 7
    print()