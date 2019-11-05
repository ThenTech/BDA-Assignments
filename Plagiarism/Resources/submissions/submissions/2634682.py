x = int(input(""))
y = int(input(""))

for k in range(1, x * y + 1):
    if k % y == 0:
        print(str(k)+ " ")
    else:
        print(k, end=" ")